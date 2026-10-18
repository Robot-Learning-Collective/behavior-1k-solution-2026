"""Compute normalization statistics for BEHAVIOR-1K dataset.

Computes mean, std, min, max from dataset in parallel.
Supports per-timestamp normalization and action correlation matrices.
State q01/q99 hold min/max: the state is scaled to [-1, 1] over this envelope.
"""

import numpy as np
import pandas as pd
import tyro
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp

import openpi.models.model as _model
import openpi.transforms as transforms

# Import B1K-specific modules  
from b1k.shared import normalize
from b1k.shared.trunk2dof import env_to_model
from b1k.policies.b1k_policy import extract_state_from_proprio
from b1k.training.data_loader import episode_arrays
from b1k.training.yaml_train_config import resolve_train_config


def get_delta_transform_from_config(config):
    """Get the delta action transform from the config."""
    data_config = config.data.create(config.assets_dirs, config.model)
    
    # Find the DeltaActions transform in the data transforms
    delta_transform = None
    for transform in data_config.data_transforms.inputs:
        if isinstance(transform, transforms.DeltaActions):
            delta_transform = transform
            break
    
    if delta_transform is None:
        raise ValueError("No DeltaActions transform found in config")
    
    return delta_transform


def process_parquet_file(args):
    """Statistics and sampled action chunks of all episodes in one LeRobot V3 data file.

    Samples are paired as in training (realign_obs_timing) and chunks are anchored only at frames up to the
    task completion. mean/std use those frames too; min/max (the state envelope) use all frames.
    """
    parquet_file, src, delta_mask, action_horizon, collect_chunks, sample_fraction = args
    
    try:
        df = pd.read_parquet(parquet_file, columns=["action", "observation.state", "episode_index", "next.terminated"])
        mask = np.asarray(delta_mask)
        dims = mask.shape[-1]
        stats_list, chunk_list = [], []
        for episode_index, group in df.groupby("episode_index"):
            if src.episodes is not None and int(episode_index) not in src.episodes:
                continue
            terminated = np.array([np.asarray(x).reshape(-1)[0] for x in group["next.terminated"]], dtype=bool)
            if not src.zero_weight_after_termination:
                terminated[:] = False
            raw_states, raw_actions, last = episode_arrays(
                np.stack(group["observation.state"].to_numpy()), np.stack(group["action"].to_numpy()),
                terminated, src.realign_obs_timing,
            )
            # Model layout: trunk as (translate, tilt)
            states = env_to_model(extract_state_from_proprio(raw_states))
            raw_actions = env_to_model(raw_actions)
            actions = raw_actions.copy()
            actions[:, :dims] = np.where(mask, raw_actions[:, :dims] - states[:, :dims], raw_actions[:, :dims])
            n = last + 1
            stats_list.append({
                key: {"count": n, "sum": x[:n].sum(0), "sum_sq": (x[:n] ** 2).sum(0), "min": x.min(0), "max": x.max(0)}
                for key, x in (("state", states), ("actions", actions))
            })

            if collect_chunks and len(raw_actions) >= action_horizon:
                # Chunks of absolute actions relative to the chunk's first state: [N-H+1, H, D]
                windows = np.lib.stride_tricks.sliding_window_view(raw_actions, action_horizon, axis=0).transpose(0, 2, 1)
                chunks = np.where(mask, windows - states[: len(windows), None, :], windows)[:n]
                rng = np.random.RandomState(hash(f"{parquet_file}:{episode_index}") % (2**31))
                n_samples = max(1, int(len(chunks) * sample_fraction))
                if n_samples < len(chunks):
                    chunks = chunks[rng.choice(len(chunks), size=n_samples, replace=False)]
                chunk_list.append(chunks)

        if not stats_list:
            return None, None
        merged = {
            key: {
                "count": sum(s[key]["count"] for s in stats_list),
                "sum": np.sum([s[key]["sum"] for s in stats_list], axis=0),
                "sum_sq": np.sum([s[key]["sum_sq"] for s in stats_list], axis=0),
                "min": np.min([s[key]["min"] for s in stats_list], axis=0),
                "max": np.max([s[key]["max"] for s in stats_list], axis=0),
            }
            for key in ("state", "actions")
        }
        all_chunks = np.concatenate(chunk_list) if chunk_list else None
        return merged, (all_chunks, all_chunks)
        
    except Exception as e:
        print(f"Error processing {parquet_file}: {e}")
        return None, None


def aggregate_episode_stats(episode_stats_list, all_data_list, config, compute_correlation=False, max_correlation_samples=2000000, compute_quantiles_sample_size=1000000):
    """Aggregate statistics from multiple episodes."""
    
    # Collect per-timestamp data if available
    per_timestamp_chunks = []
    for data in all_data_list:
        if data is not None and len(data) > 0 and data[0] is not None:
            per_timestamp_chunks.append(data[0])
    
    # Collect correlation chunks if available
    correlation_chunks = []
    for data in all_data_list:
        if data is not None and len(data) > 1 and data[1] is not None:
            correlation_chunks.append(data[1])
    
    # Collect raw data for quantile computation (sample if too large)
    state_data_for_quantiles = []
    action_data_for_quantiles = []
    
    for data in all_data_list:
        if data is not None and len(data) > 0 and data[0] is not None:
            # data[0] is per_timestamp chunks: [N, H, D]
            chunks = data[0]
            # For actions, we have action chunks
            # For states, we would need separate collection (skip for now, use min/max)
            action_data_for_quantiles.append(chunks)
    
    # Aggregate counts, sums, etc.
    final_stats = {"state": {}, "actions": {}}
    
    for key in ["state", "actions"]:
        total_count = sum(stats[key]["count"] for stats in episode_stats_list if stats is not None)
        total_sum = np.sum([stats[key]["sum"] for stats in episode_stats_list if stats is not None], axis=0)
        total_sum_sq = np.sum([stats[key]["sum_sq"] for stats in episode_stats_list if stats is not None], axis=0)
        global_min = np.min([stats[key]["min"] for stats in episode_stats_list if stats is not None], axis=0)
        global_max = np.max([stats[key]["max"] for stats in episode_stats_list if stats is not None], axis=0)
        
        # Compute final statistics
        mean = total_sum / total_count
        variance = (total_sum_sq / total_count) - mean**2
        std = np.sqrt(np.maximum(0, variance))
        
        # Compute actual percentiles for actions (sample if needed for memory efficiency)
        if key == "actions" and action_data_for_quantiles:
            print(f"Computing actual percentiles for actions...")
            # Concatenate all action chunks and flatten to [N*H, D]
            all_action_data = np.vstack(action_data_for_quantiles)  # [N, H, D]
            all_action_data_flat = all_action_data.reshape(-1, all_action_data.shape[-1])  # [N*H, D]
            
            # Sample if too large for memory
            if len(all_action_data_flat) > compute_quantiles_sample_size:
                print(f"  Sampling {compute_quantiles_sample_size:,} from {len(all_action_data_flat):,} data points")
                rng = np.random.RandomState(42)
                indices = rng.choice(len(all_action_data_flat), size=compute_quantiles_sample_size, replace=False)
                all_action_data_flat = all_action_data_flat[indices]
            
            q01 = np.percentile(all_action_data_flat, 1, axis=0)
            q99 = np.percentile(all_action_data_flat, 99, axis=0)
            print(f"  Computed q01/q99 from {len(all_action_data_flat):,} samples")
        else:
            # Fallback to min/max for state (no chunks collected)
            q01 = global_min
            q99 = global_max
        
        final_stats[key] = {
            "mean": mean,
            "std": std,
            "q01": q01,
            "q99": q99,
        }
    
    # Compute per-timestamp statistics for actions if available
    per_timestamp_stats = None
    if per_timestamp_chunks and key == "actions":
        # Combine all chunks: (num_episodes * num_chunks_per_episode, action_horizon, action_dim)
        all_chunks = np.vstack(per_timestamp_chunks)
        
        # Compute statistics for each timestamp
        action_horizon, action_dim = all_chunks.shape[1], all_chunks.shape[2]
        per_timestamp_mean = np.zeros((action_horizon, action_dim))
        per_timestamp_std = np.zeros((action_horizon, action_dim))
        per_timestamp_q01 = np.zeros((action_horizon, action_dim))
        per_timestamp_q99 = np.zeros((action_horizon, action_dim))
        
        for t in range(action_horizon):
            timestep_data = all_chunks[:, t, :]  # Shape: (num_chunks, action_dim)
            per_timestamp_mean[t] = np.mean(timestep_data, axis=0)
            per_timestamp_std[t] = np.std(timestep_data, axis=0)
            per_timestamp_q01[t] = np.percentile(timestep_data, 1, axis=0)
            per_timestamp_q99[t] = np.percentile(timestep_data, 99, axis=0)
        
        per_timestamp_stats = {
            "per_timestamp_mean": per_timestamp_mean,
            "per_timestamp_std": per_timestamp_std,
            "per_timestamp_q01": per_timestamp_q01,
            "per_timestamp_q99": per_timestamp_q99,
        }
    
    # Compute full correlation matrix for actions if available
    correlation_stats = None
    if compute_correlation and not correlation_chunks:
        raise RuntimeError(
            "Correlation computation was requested but no correlation chunks were collected. "
            "This indicates an issue with episode processing or insufficient data."
        )
    
    if correlation_chunks:
        print("Computing full action correlation matrix...")
        # Combine all chunks: (num_episodes * num_chunks_per_episode, action_horizon, action_dim)
        all_corr_chunks = np.vstack(correlation_chunks)
        action_horizon, action_dim = all_corr_chunks.shape[1], all_corr_chunks.shape[2]
        target_action_dim = config.model.action_dim  # 32 (with padding)
        
        print(f"Total action chunks available: {all_corr_chunks.shape[0]} of shape ({action_horizon}, {action_dim})")
        
        # PAD action dimensions BEFORE computing correlations
        if action_dim < target_action_dim:
            print(f"Padding actions from {action_dim}D to {target_action_dim}D...")
            # Pad with zeros: (num_samples, action_horizon, action_dim) -> (num_samples, action_horizon, target_action_dim)
            padding = np.zeros((all_corr_chunks.shape[0], action_horizon, target_action_dim - action_dim))
            all_corr_chunks_padded = np.concatenate([all_corr_chunks, padding], axis=2)
            print(f"Padded chunks shape: {all_corr_chunks_padded.shape}")
        else:
            all_corr_chunks_padded = all_corr_chunks[:, :, :target_action_dim]
        
        # Flatten chunks to (num_samples, action_horizon * target_action_dim)
        flattened_chunks = all_corr_chunks_padded.reshape(-1, action_horizon * target_action_dim)
        total_samples = flattened_chunks.shape[0]
        
        # Subsample if we have too many samples (for computational efficiency)
        if total_samples > max_correlation_samples:
            print(f"Subsampling {max_correlation_samples} random chunks for correlation computation (from {total_samples})")
            print(f"This provides ~{100 * max_correlation_samples / total_samples:.1f}x speedup with negligible accuracy loss")
            rng = np.random.RandomState(42)  # Fixed seed for reproducibility
            sample_indices = rng.choice(total_samples, size=max_correlation_samples, replace=False)
            flattened_chunks = flattened_chunks[sample_indices]
            print(f"Using {flattened_chunks.shape[0]} sampled chunks for correlation matrix computation")
        else:
            print(f"Using all {total_samples} chunks (no subsampling needed)")
        
        # Normalize each dimension to zero mean and unit variance for correlation computation
        # This ensures the correlation matrix captures pure correlation structure
        chunk_mean = np.mean(flattened_chunks, axis=0)
        chunk_std = np.std(flattened_chunks, axis=0)
        
        # Identify constant dimensions (std ≈ 0, including padded dimensions)
        constant_dims = chunk_std < 1e-6
        print(f"Found {np.sum(constant_dims)} constant/padded dimensions (will be set to identity)")
        
        # Normalize non-constant dimensions
        normalized_chunks = flattened_chunks.copy()
        normalized_chunks[:, ~constant_dims] = (flattened_chunks[:, ~constant_dims] - chunk_mean[~constant_dims]) / chunk_std[~constant_dims]
        # Constant dimensions stay as 0 (already centered at 0 due to padding)
        
        # Compute empirical covariance matrix
        # For normalized data, covariance = correlation
        cov_matrix = np.cov(normalized_chunks, rowvar=False)  # Shape: [H*D, H*D]
        print(f"Covariance matrix shape: {cov_matrix.shape}")
        
        # Enforce diagonal = 1 for all dimensions (standard correlation matrix property)
        # Handle constant dimensions carefully (avoid division by zero)
        diag_vals = np.diag(cov_matrix).copy()
        print(f"Diagonal before correction: min={np.min(diag_vals):.6f}, max={np.max(diag_vals):.6f}")
        
        # Identify truly constant dimensions (diagonal ≈ 0)
        constant_mask = diag_vals < 1e-10
        num_constant = np.sum(constant_mask)
        print(f"Found {num_constant} dimensions with zero variance on diagonal")
        
        # Normalize correlation matrix (avoid division by zero)
        diag_vals_safe = diag_vals.copy()
        diag_vals_safe[constant_mask] = 1.0  # Prevent division by zero
        
        normalizer = np.sqrt(diag_vals_safe[:, None] @ diag_vals_safe[None, :])
        cov_matrix = cov_matrix / normalizer
        
        # For constant dimensions: set their rows/columns to 0, diagonal to 1
        cov_matrix[constant_mask, :] = 0.0
        cov_matrix[:, constant_mask] = 0.0
        np.fill_diagonal(cov_matrix, 1.0)
        
        print(f"Diagonal after correction: min={np.min(np.diag(cov_matrix)):.6f}, max={np.max(np.diag(cov_matrix)):.6f}")
        print(f"Matrix check: has NaN={np.any(np.isnan(cov_matrix))}, has Inf={np.any(np.isinf(cov_matrix))}")
        
        # Add regularization for numerical stability
        epsilon = 1e-6
        cov_matrix_reg = cov_matrix + epsilon * np.eye(cov_matrix.shape[0])
        
        # Check eigenvalues for positive definiteness
        eigenvalues = np.linalg.eigvalsh(cov_matrix_reg)
        min_eigenvalue = np.min(eigenvalues)
        print(f"Min eigenvalue after regularization: {min_eigenvalue:.6e}")
        
        if min_eigenvalue <= 0:
            print(f"WARNING: Matrix not positive definite! Adding stronger regularization...")
            # Add stronger regularization if needed
            epsilon = max(1e-5, -min_eigenvalue + 1e-5)
            cov_matrix_reg = cov_matrix + epsilon * np.eye(cov_matrix.shape[0])
            eigenvalues = np.linalg.eigvalsh(cov_matrix_reg)
            min_eigenvalue = np.min(eigenvalues)
            print(f"New min eigenvalue: {min_eigenvalue:.6e}")
        
        # Compute Cholesky decomposition
        try:
            chol_lower = np.linalg.cholesky(cov_matrix_reg)
            print(f"Cholesky decomposition successful! Shape: {chol_lower.shape}")
            
            # Verify reconstruction: L @ L.T ≈ Σ
            reconstructed = chol_lower @ chol_lower.T
            reconstruction_error = np.linalg.norm(reconstructed - cov_matrix_reg, 'fro') / np.linalg.norm(cov_matrix_reg, 'fro')
            print(f"Cholesky reconstruction error: {reconstruction_error:.6e}")
            
            # Compute averaged spatial correlation (dim × dim)
            # Average correlation across all timesteps
            print("\nComputing averaged spatial correlation (dim × dim)...")
            spatial_corrs = []
            for t in range(action_horizon):
                start_idx = t * target_action_dim
                end_idx = (t + 1) * target_action_dim
                timestep_data = normalized_chunks[:, start_idx:end_idx]
                corr_t = np.cov(timestep_data, rowvar=False)
                
                # Normalize to ensure diagonal = 1
                diag_t = np.diag(corr_t)
                corr_t = corr_t / np.sqrt(diag_t[:, None] @ diag_t[None, :])
                
                spatial_corrs.append(corr_t)
            
            avg_spatial_corr = np.mean(spatial_corrs, axis=0)  # (target_action_dim, target_action_dim)
            # Final diagonal enforcement
            np.fill_diagonal(avg_spatial_corr, 1.0)
            print(f"Averaged spatial correlation shape: {avg_spatial_corr.shape}")
            
            # Compute averaged temporal correlation (time × time)
            # Average correlation across all NON-CONSTANT dimensions only
            print("Computing averaged temporal correlation (time × time)...")
            temporal_corrs = []
            
            # Identify which dimensions are constant (per original dimension, before flattening)
            dim_is_constant = []
            for d in range(target_action_dim):
                # Check if this dimension is constant across all timesteps
                dim_indices_check = [t * target_action_dim + d for t in range(action_horizon)]
                dim_std = chunk_std[dim_indices_check]
                # Dimension is constant if std < 1e-6 for all its timesteps
                dim_is_constant.append(np.all(dim_std < 1e-6))
            
            num_constant = np.sum(dim_is_constant)
            print(f"  Excluding {num_constant} constant dimensions from temporal averaging")
            
            for d in range(target_action_dim):
                if dim_is_constant[d]:
                    continue  # Skip constant dimensions
                    
                dim_indices = [t * target_action_dim + d for t in range(action_horizon)]
                dim_data = normalized_chunks[:, dim_indices]
                corr_d = np.cov(dim_data, rowvar=False)
                
                # Normalize to ensure diagonal = 1
                diag_d = np.diag(corr_d)
                corr_d = corr_d / np.sqrt(diag_d[:, None] @ diag_d[None, :])
                
                temporal_corrs.append(corr_d)
            
            if len(temporal_corrs) > 0:
                avg_temporal_corr = np.mean(temporal_corrs, axis=0)  # (action_horizon, action_horizon)
                # Final diagonal enforcement
                np.fill_diagonal(avg_temporal_corr, 1.0)
                print(f"Averaged temporal correlation shape: {avg_temporal_corr.shape}")
            else:
                # All dimensions are constant - use identity
                avg_temporal_corr = np.eye(action_horizon)
                print(f"All dimensions constant - using identity for temporal correlation")
            
            # Store correlation matrices
            # Beta shrinkage will be applied at model load time
            correlation_stats = {
                "action_correlation_cholesky": chol_lower,
                "action_correlation_spatial": avg_spatial_corr,    # (D, D) - averaged spatial
                "action_correlation_temporal": avg_temporal_corr,  # (H, H) - averaged temporal
            }
        except np.linalg.LinAlgError as e:
            raise RuntimeError(
                f"Cholesky decomposition failed: {e}. "
                "This indicates the covariance matrix is not positive definite even after regularization. "
                "This is a critical error that needs investigation."
            )
    
    return final_stats, per_timestamp_stats, correlation_stats


def main(
    config_name: str, 
    num_workers: int | None = None, 
    per_timestamp: bool = False, 
    correlation: bool = True,
    max_correlation_samples: int = 2000000,
    sample_fraction: float = 0.1
):
    """Compute normalization statistics quickly for B1K config using parallel processing.
    
    Args:
        config_name: Name of the training config or a YAML recipe path
        num_workers: Number of parallel workers (None = auto)
        per_timestamp: Whether to compute per-timestamp statistics
        correlation: Whether to compute action correlation matrix
        max_correlation_samples: Maximum number of samples to use for correlation computation
                                  (subsampling for efficiency, 2M is typically sufficient)
        sample_fraction: Fraction of action chunks to sample from each episode for 
                        correlation/per-timestamp stats (default 0.1 = 10%, use 1.0 for no sampling).
                        Note: mean/std/min/max are ALWAYS computed over ALL data.
    """
    
    config = resolve_train_config(config_name)
    data_config = config.data.create(config.assets_dirs, config.model)
    
    # Get the delta transform from config
    delta_transform = get_delta_transform_from_config(config)
    print(f"Using delta transform with mask: {delta_transform.mask}")
    
    # Check if we should compute per-timestamp stats
    compute_per_timestamp = per_timestamp or data_config.use_per_timestamp_norm
    compute_correlation = correlation
    action_horizon = config.model.action_horizon
    collect_chunks = compute_per_timestamp or compute_correlation
    
    work_units = []
    for src in data_config.data_sources:
        files = sorted(Path(src.root).expanduser().glob("data/*/*.parquet"))
        print(f"Source {src.repo_id}: {len(files)} parquet files")
        work_units += [(f, src, delta_transform.mask, action_horizon, collect_chunks, sample_fraction) for f in files]
    if not work_units:
        raise ValueError("No data parquet files found")
    
    # Set up parallel processing
    num_workers = max(1, num_workers or min(mp.cpu_count(), len(work_units)))
    print(f"Processing {len(work_units)} files with {num_workers} workers")
    
    episode_stats_list = []
    all_data_list = []
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for future in as_completed([executor.submit(process_parquet_file, args) for args in work_units]):
            episode_stats, episode_data = future.result()
            if episode_stats is not None:
                episode_stats_list.append(episode_stats)
                all_data_list.append(episode_data)
    print(f"Successfully processed {len(episode_stats_list)} files")
    
    # Aggregate all statistics
    print("Aggregating statistics...")
    final_stats, per_timestamp_stats, correlation_stats = aggregate_episode_stats(
        episode_stats_list, all_data_list, 
        config,
        compute_correlation=compute_correlation,
        max_correlation_samples=max_correlation_samples
    )
    
    # Prepare correlation matrix if computed
    correlation_matrix = None
    if compute_correlation:
        if correlation_stats is None:
            raise RuntimeError(
                "Correlation computation was requested (--correlation) but correlation_stats is None. "
                "This indicates an unexpected error in the correlation computation pipeline."
            )
        print("Adding action correlation matrix...")
        chol_matrix = correlation_stats["action_correlation_cholesky"]
        print(f"Correlation matrix shape: {chol_matrix.shape}")
        
        # Verify size matches expected (should already be correct from padding before computation)
        expected_dim = action_horizon * config.model.action_dim
        if chol_matrix.shape[0] != expected_dim:
            raise ValueError(
                f"Correlation matrix has unexpected size {chol_matrix.shape[0]}, "
                f"expected {expected_dim} (action_horizon={action_horizon} × action_dim={config.model.action_dim})"
            )
        
        correlation_matrix = chol_matrix
    elif correlation_stats is not None:
        # This shouldn't happen but handle it gracefully
        print("WARNING: Correlation matrix was computed but --correlation flag was False. Ignoring correlation matrix.")
    
    # Create NormStats objects with proper structure
    norm_stats_dict = {}
    
    for key in ["state", "actions"]:
        # Prepare basic statistics
        stats_kwargs = {}
        for stat_type in ["mean", "std", "q01", "q99"]:
            stat_value = final_stats[key][stat_type]
            padded_value = transforms.pad_to_dim(stat_value, config.model.action_dim)
            stats_kwargs[stat_type] = padded_value
        
        # Add per-timestamp statistics if computed and this is actions
        if per_timestamp_stats is not None and key == "actions":
            print("Adding per-timestamp statistics...")
            for stat_type in ["per_timestamp_mean", "per_timestamp_std", "per_timestamp_q01", "per_timestamp_q99"]:
                stat_value = per_timestamp_stats[stat_type]
                # Pad each timestamp to model action dimension
                padded_value = []
                for t in range(stat_value.shape[0]):
                    padded_timestep = transforms.pad_to_dim(stat_value[t], config.model.action_dim)
                    padded_value.append(padded_timestep)
                stats_kwargs[stat_type] = np.array(padded_value)
        
        # Add correlation matrices if computed and this is actions
        if correlation_matrix is not None and key == "actions":
            stats_kwargs["action_correlation_cholesky"] = correlation_matrix
            # Also add averaged spatial and temporal correlations if available
            if correlation_stats and "action_correlation_spatial" in correlation_stats:
                stats_kwargs["action_correlation_spatial"] = correlation_stats["action_correlation_spatial"]
            if correlation_stats and "action_correlation_temporal" in correlation_stats:
                stats_kwargs["action_correlation_temporal"] = correlation_stats["action_correlation_temporal"]
        
        # Create NormStats object
        norm_stats_dict[key] = normalize.NormStats(**stats_kwargs)
    
    # Save statistics
    output_path = config.assets_dirs / data_config.asset_id
    output_path.mkdir(parents=True, exist_ok=True)
    normalize.save(output_path, norm_stats_dict)
    
    # Print summary for verification
    print("\nStatistics Summary (first 23 dims):")
    state_means = np.array(norm_stats_dict["state"].mean[:23])
    action_means = np.array(norm_stats_dict["actions"].mean[:23])
    differences = np.abs(state_means - action_means)
    
    print("State means:  ", state_means)
    print("Action means: ", action_means)
    print("Differences:  ", differences)
    print("Max difference:", np.max(differences))
    print("\nNote: For actions, q01/q99 are actual percentiles. For state, q01/q99 contain min/max values.")
    
    if per_timestamp_stats is not None:
        print(f"\nPer-timestamp statistics computed for {action_horizon} timesteps")
        # Show first few timesteps for verification
        per_ts_means = np.array(norm_stats_dict["actions"].per_timestamp_mean)
        print(f"Per-timestamp means shape: {per_ts_means.shape}")
        print("First 3 timesteps, first 5 dims:")
        for t in range(min(3, per_ts_means.shape[0])):
            print(f"  t={t}: {per_ts_means[t, :5]}")
    
    if compute_correlation:
        print(f"\nCorrelation matrices computed!")
        
        # Full correlation matrix
        corr_matrix = np.array(norm_stats_dict["actions"].action_correlation_cholesky)
        print(f"  Full correlation (Cholesky): {corr_matrix.shape}")
        print(f"    Memory: {corr_matrix.nbytes / 1024 / 1024:.2f} MB")
        
        # Averaged spatial correlation
        if hasattr(norm_stats_dict["actions"], 'action_correlation_spatial') and \
           norm_stats_dict["actions"].action_correlation_spatial is not None:
            spatial = np.array(norm_stats_dict["actions"].action_correlation_spatial)
            print(f"  Spatial (dim×dim, averaged): {spatial.shape}")
            print(f"    Memory: {spatial.nbytes / 1024:.2f} KB")
            print(f"    Sample correlation (d0 vs d1): {spatial[0, 1]:.4f}")
        
        # Averaged temporal correlation
        if hasattr(norm_stats_dict["actions"], 'action_correlation_temporal') and \
           norm_stats_dict["actions"].action_correlation_temporal is not None:
            temporal = np.array(norm_stats_dict["actions"].action_correlation_temporal)
            print(f"  Temporal (time×time, averaged): {temporal.shape}")
            print(f"    Memory: {temporal.nbytes / 1024:.2f} KB")
            print(f"    Sample correlation (t0 vs t1): {temporal[0, 1]:.4f}")
        
        print("\nNote: Beta shrinkage will be applied at model load time (not during stats computation)")
    else:
        print("\nCorrelation matrix computation was disabled (--no-correlation)")
    
    print(f"\nStatistics saved to: {output_path}")


if __name__ == "__main__":
    tyro.cli(main)
