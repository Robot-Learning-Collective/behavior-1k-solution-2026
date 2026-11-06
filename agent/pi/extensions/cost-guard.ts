/**
 * cost-guard — stop a pi session when its cost breaches a limit.
 *
 * - Tracks cost from assistant message usage (message_end), rebuilds on session_start.
 * - Footer status: `cost $12.34/$150`.
 * - At the next LLM call after breach (turn_start), pauses the run with an overlay:
 *   continue (+$50 ratchet), set an explicit limit, disable for the session, or stop.
 * - `/cost` opens the same overlay anytime with a cost breakdown (input/output/cache, per model).
 * - Ratcheted limit / disable persist in the session (survives resume/fork/reload).
 *
 * Config: hardcoded DEFAULT_LIMIT / STEP below. PI_COST_LIMIT env var overrides the
 * default limit (used for live verification with cent-level limits).
 */
import type { ExtensionAPI, ExtensionContext } from "@earendil-works/pi-coding-agent";
import { Key, matchesKey, truncateToWidth } from "@earendil-works/pi-tui";

const DEFAULT_LIMIT = 400; // USD per session; PI_COST_LIMIT overrides
const STEP = 50; // USD ratchet increment
const STATE_ENTRY_TYPE = "cost-guard";

interface Buckets {
	input: number;
	output: number;
	cacheRead: number;
	cacheWrite: number;
}

interface CostState {
	cost: Buckets & { total: number };
	tokens: Buckets;
	byModel: Map<string, number>; // model id -> cost
}

type OverlayAction = "continue" | "setLimit" | "disable" | "close";

function emptyState(): CostState {
	return {
		cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, total: 0 },
		tokens: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
		byModel: new Map(),
	};
}

function num(value: unknown): number {
	return typeof value === "number" && Number.isFinite(value) ? value : 0;
}

function accumulate(state: CostState, message: Record<string, any>): void {
	if (message?.role !== "assistant") return;
	const usage = message.usage as Record<string, any> | undefined;
	if (!usage) return;
	const cost = (usage.cost ?? {}) as Record<string, unknown>;
	state.cost.input += num(cost.input);
	state.cost.output += num(cost.output);
	state.cost.cacheRead += num(cost.cacheRead);
	state.cost.cacheWrite += num(cost.cacheWrite);
	state.cost.total += num(cost.total);
	state.tokens.input += num(usage.input);
	state.tokens.output += num(usage.output);
	state.tokens.cacheRead += num(usage.cacheRead);
	state.tokens.cacheWrite += num(usage.cacheWrite);
	const model = typeof message.model === "string" && message.model ? message.model : "unknown";
	state.byModel.set(model, (state.byModel.get(model) ?? 0) + num(cost.total));
}

function usd(value: number): string {
	return `$${value.toFixed(2)}`;
}

function tok(value: number): string {
	if (value >= 1_000_000) return `${(value / 1_000_000).toFixed(1)}M`;
	if (value >= 1_000) return `${(value / 1_000).toFixed(0)}K`;
	return `${value}`;
}

function defaultLimit(): number {
	const env = Number(process.env.PI_COST_LIMIT);
	return Number.isFinite(env) && env > 0 ? env : DEFAULT_LIMIT;
}

/** Interactive overlay: cost breakdown + actions. */
class CostOverlay {
	public onDone?: (action: OverlayAction) => void;

	constructor(
		private state: CostState,
		private limit: number,
		private breach: boolean,
		private theme: any,
	) {}

	handleInput(data: string): void {
		if (data === "c" || data === "C") this.onDone?.("continue");
		else if (data === "l" || data === "L") this.onDone?.("setLimit");
		else if (data === "d" || data === "D") this.onDone?.("disable");
		else if (matchesKey(data, Key.escape) || data === "q") this.onDone?.("close");
	}

	render(width: number): string[] {
		const t = this.theme;
		const dim = (s: string) => t.fg("dim", s);
		const accent = (s: string) => t.fg("accent", s);
		const warn = (s: string) => t.fg("error", s);
		const row = (label: string, tokens: string, cost: string, extra = "") =>
			`  ${label.padEnd(12)} ${tokens.padStart(10)}  ${cost.padStart(9)}${extra ? `  ${dim(extra)}` : ""}`;

		const header = this.breach
			? warn(`COST LIMIT BREACHED — ${usd(this.state.cost.total)} / ${usd(this.limit)}`)
			: accent(`cost-guard — ${usd(this.state.cost.total)} / ${usd(this.limit)}`);

		const cacheDenom = this.state.tokens.cacheRead + this.state.tokens.input;
		const hitRate = cacheDenom > 0 ? `${Math.round((this.state.tokens.cacheRead / cacheDenom) * 100)}% hit` : "";

		const lines: string[] = [
			"",
			`  ${header}`,
			"",
			row("input", `${tok(this.state.tokens.input)} tok`, usd(this.cost("input"))),
			row("output", `${tok(this.state.tokens.output)} tok`, usd(this.cost("output"))),
			row("cache read", `${tok(this.state.tokens.cacheRead)} tok`, usd(this.cost("cacheRead")), hitRate),
			row("cache write", `${tok(this.state.tokens.cacheWrite)} tok`, usd(this.cost("cacheWrite"))),
			"",
			`  ${dim("by model")}`,
		];
		const models = [...this.state.byModel.entries()].sort((a, b) => b[1] - a[1]).slice(0, 6);
		if (models.length === 0) lines.push(`   ${dim("(no usage yet)")}`);
		for (const [model, cost] of models) {
			lines.push(`   ${model.padEnd(24)} ${usd(cost).padStart(9)}`);
		}
		lines.push("");
		lines.push(
			`  ${accent("[c]")} continue +${usd(STEP)}  ${accent("[l]")} set limit  ${accent("[d]")} disable session`,
		);
		lines.push(`  ${accent("[esc]")} ${this.breach ? warn("stop the run") : "close"}`);
		lines.push("");
		return lines.map((line) => truncateToWidth(line, width));
	}

	private cost(key: keyof Buckets): number {
		return this.state.cost[key];
	}
}

export default function costGuardExtension(pi: ExtensionAPI) {
	let state = emptyState();
	let limit = defaultLimit();
	let disabled = false;
	let overlayOpen = false;

	function updateStatus(ctx: ExtensionContext) {
		if (!ctx.hasUI) return;
		if (disabled) {
			ctx.ui.setStatus("cost", "cost off");
			return;
		}
		const text = `cost ${usd(state.cost.total)}/${usd(limit)}`;
		ctx.ui.setStatus("cost", state.cost.total >= limit ? ctx.ui.theme.fg("error", text) : text);
	}

	function persist() {
		pi.appendEntry(STATE_ENTRY_TYPE, { limit, disabled, at: Date.now() });
	}

	function rebuild(ctx: ExtensionContext) {
		state = emptyState();
		limit = defaultLimit();
		disabled = false;
		// Sum cost over ALL entries (abandoned branches cost real money too),
		// and restore the last persisted limit/disable decision.
		for (const entry of ctx.sessionManager.getEntries() as Array<Record<string, any>>) {
			if (entry.type === "message") {
				accumulate(state, entry.message as Record<string, any>);
			} else if (entry.type === "custom" && entry.customType === STATE_ENTRY_TYPE) {
				const data = entry.data as { limit?: number; disabled?: boolean } | undefined;
				if (typeof data?.limit === "number" && data.limit > 0) limit = data.limit;
				if (typeof data?.disabled === "boolean") disabled = data.disabled;
			}
		}
		updateStatus(ctx);
	}

	async function showOverlay(ctx: ExtensionContext, breach: boolean): Promise<OverlayAction> {
		if (ctx.mode !== "tui") {
			// RPC fallback: yes/no dialog. Print/JSON: no UI -> stop.
			if (ctx.hasUI) {
				const ok = await ctx.ui.confirm(
					`Cost limit breached (${usd(state.cost.total)} / ${usd(limit)})`,
					`Continue with a +${usd(STEP)} higher limit?`,
				);
				return ok ? "continue" : "close";
			}
			return "close";
		}
		return await ctx.ui.custom<OverlayAction>(
			(_tui, theme, _keybindings, done) => {
				const overlay = new CostOverlay(state, limit, breach, theme);
				overlay.onDone = (action) => done(action);
				return overlay;
			},
			{
				overlay: true,
				overlayOptions: { width: "60%", minWidth: 52, anchor: "center" },
			},
		);
	}

	async function runOverlayFlow(ctx: ExtensionContext, breach: boolean): Promise<"resume" | "stop"> {
		if (overlayOpen) return "resume";
		overlayOpen = true;
		try {
			for (;;) {
				const action = await showOverlay(ctx, breach);
				if (action === "continue") {
					// Raise to at least limit+STEP, and always clear the current cost.
					limit = Math.max(limit + STEP, Math.floor(state.cost.total / STEP) * STEP + STEP);
					disabled = false;
					persist();
					updateStatus(ctx);
					ctx.ui.notify(`cost-guard: limit raised to ${usd(limit)}`, "info");
					return "resume";
				}
				if (action === "setLimit") {
					const raw = await ctx.ui.input("cost-guard", `New limit in USD (current ${usd(limit)}):`);
					const value = Number(raw);
					if (Number.isFinite(value) && value > 0) {
						limit = value;
						disabled = false;
						persist();
						updateStatus(ctx);
						ctx.ui.notify(`cost-guard: limit set to ${usd(limit)}`, "info");
						if (!breach || state.cost.total < limit) return "resume";
						continue; // still breached -> re-show
					}
					ctx.ui.notify("cost-guard: invalid amount", "error");
					continue;
				}
				if (action === "disable") {
					disabled = true;
					persist();
					updateStatus(ctx);
					ctx.ui.notify("cost-guard: disabled for this session", "info");
					return "resume";
				}
				// close
				return breach ? "stop" : "resume";
			}
		} finally {
			overlayOpen = false;
		}
	}

	pi.on("session_start", async (_event, ctx) => {
		rebuild(ctx);
	});

	pi.on("message_end", async (event, ctx) => {
		if (event.message.role !== "assistant") return;
		accumulate(state, event.message as unknown as Record<string, any>);
		updateStatus(ctx);
	});

	// Gate: before each LLM call. Pauses the agent loop while the overlay is open;
	// "continue"/"set limit"/"disable" resume the run seamlessly, close/esc aborts it.
	pi.on("turn_start", async (_event, ctx) => {
		if (disabled || state.cost.total < limit) return;
		const verdict = await runOverlayFlow(ctx, true);
		if (verdict === "stop") {
			ctx.ui.notify(
				`cost-guard: run stopped at ${usd(state.cost.total)} (limit ${usd(limit)}). Use /cost to raise the limit.`,
				"error",
			);
			ctx.abort();
		}
	});

	pi.registerCommand("cost", {
		description: "Show session cost breakdown and manage the cost limit",
		handler: async (_args, ctx) => {
			if (!ctx.hasUI) return;
			// From /cost, "continue" and "set limit" also re-enable a disabled guard.
			await runOverlayFlow(ctx, !disabled && state.cost.total >= limit);
			updateStatus(ctx);
		},
	});
}
