# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please report it
**privately** rather than opening a public issue.

Send your report to: zeloras@devjcat.com

Please include:
- A description of the vulnerability and its potential impact
- Steps to reproduce or a proof of concept
- Your assessment of severity

We will acknowledge receipt within 48 hours and aim to provide an initial
assessment within one week.

## Scope

This policy covers:
- Software dependencies with known vulnerabilities
- CI/CD pipeline security issues
- Bugs in the Python tooling (sweep map, simulator, translation pipeline)
- Repository configuration issues that could lead to unauthorized access

**Physical safety** of the hardware rig is covered separately in
[docs/02-safety.md](../docs/02-safety.md) — the high-voltage driver and piezo
transducer handling guidelines are not part of this software security policy.

## Disclosure

We follow coordinated disclosure: once a fix is available, we will publish
a security advisory on GitHub and credit the reporter (unless they prefer
to remain anonymous).