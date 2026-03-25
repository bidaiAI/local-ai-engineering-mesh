# Security Rules

- Never hardcode secrets or tokens.
- Validate all external input at trust boundaries.
- Prefer parameterized queries over string-built SQL.
- Require explicit auth and permission checks on state-changing paths.
- Avoid leaking sensitive internals in logs, errors, screenshots, or artifacts.
- Review third-party dependencies before adopting them.
