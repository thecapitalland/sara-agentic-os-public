# Security Policy

## Supported version

| Version | Supported |
|---|---|
| 2.x | Yes |
| 1.x and earlier | No |

Core rules:
- least privilege for write-capable actions;
- no credential material in repository evidence;
- explicit human gates for protected actions;
- independent review for material sensitive changes;
- context and memory never create authority;
- rollback/recovery before high-impact stateful change.

For a suspected vulnerability, open a minimal report without publishing credentials, exploit data against real systems, or sensitive project information.
