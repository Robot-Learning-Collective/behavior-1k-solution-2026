"""Credential-value redaction for authorized private session exports.

Preserves prompt context, paths, op:// references, images and entry structure.
This is a bounded pattern scanner, not a guarantee that arbitrary secrets can be
recognized. Reports contain counts and locations, never credential values.
"""
import collections
import re

PATTERNS = {
    'private_key': re.compile(r'-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----[\s\S]*?-----END (?:[A-Z ]+ )?PRIVATE KEY-----'),
    'provider_token': re.compile(r'\b(?:sk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|xox[baprs]-[A-Za-z0-9-]{20,})\b'),
    'jwt': re.compile(r'\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\b'),
    'authorization': re.compile(r'(?i)(\b(?:Bearer|Basic)\s+)([A-Za-z0-9_+/.=-]{24,})'),
    'credential_assignment': re.compile(r'''(?i)(["']?\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password|passwd|cookie|set-cookie|authorization|aws_secret_access_key)["']?\s*[:=]\s*["'])([^"'\n]{8,})(["'])'''),
}


def credential_literal(value):
    if value.startswith(('op://', '$', '<', '/', 'http://', 'https://')):
        return False
    # Task text can contain the physical object named cookie; prose is not auth.
    if any(c.isspace() for c in value) and not (value.startswith(('Bearer ', 'Basic ')) or ('=' in value and ';' in value)):
        return False
    if any(x in value.lower() for x in ('placeholder', 'replace_', 'example', 'redacted', 'your_', 'process.env', 'os.environ')):
        return False
    return len(value) >= 20 and (any(c.isdigit() for c in value) or '=' in value or '.' in value)


def scrub_text(text, counts=None):
    counts = collections.Counter() if counts is None else counts
    for name, pattern in PATTERNS.items():
        def replace(match):
            if name == 'credential_assignment':
                if not credential_literal(match[2]):
                    return match[0]
                counts[name] += 1
                return match[1] + '[REDACTED_CREDENTIAL]' + match[3]
            counts[name] += 1
            return (match[1] if name == 'authorization' else '') + '[REDACTED_CREDENTIAL]'
        text = pattern.sub(replace, text)
    return text


def scrub(value, counts=None):
    counts = collections.Counter() if counts is None else counts
    if isinstance(value, str):
        return scrub_text(value, counts)
    if isinstance(value, list):
        return [scrub(x, counts) for x in value]
    if isinstance(value, dict):
        # Images/signatures are opaque, not credential stores. Never corrupt them.
        image = value.get('type') in ('image', 'input_image')
        out = {}
        for key, item in value.items():
            if (image and key in ('data', 'image_url')) or key in ('thoughtSignature', 'thinkingSignature'):
                out[key] = item
            elif re.fullmatch(r'(?i)(api_?key|access_?token|refresh_?token|client_?secret|password|cookie|authorization)', key) and isinstance(item, str) and credential_literal(item):
                counts['credential_field'] += 1
                out[key] = '[REDACTED_CREDENTIAL]'
            else:
                out[key] = scrub(item, counts)
        return out
    return value


if __name__ == '__main__':
    c = collections.Counter()
    result = scrub({'text': 'op://vault/item/key sk-proj-' + 'a2'*25,
                    'access_token': 'eyJ' + 'a'*30 + '.' + 'b'*30 + '.' + 'c'*30}, c)
    assert result['text'].startswith('op://vault/item/key [REDACTED')
    assert result['access_token'] == '[REDACTED_CREDENTIAL]' and sum(c.values()) == 2
    assert scrub({'type': 'image', 'data': 'sk-' + 'a'*30})['data'].startswith('sk-')
    print('SCRUB_SELF_TEST_PASS')
