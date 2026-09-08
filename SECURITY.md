# Security policy

This repository contains orchestration, guidance, and automation. Product repositories must publish their own support and reporting details. There are currently no stable releases or long-term support commitments for this umbrella repository; security fixes target the current default branch.

Do not disclose exploitable vulnerabilities, credentials, or customer data in public issues or pull requests.

Use the repository's **Security → Advisories → Report a vulnerability** entry point when available. Include affected revision, impact, prerequisites, a minimal reproduction, and suggested mitigation. Share only the sensitive information required to investigate.

If private reporting is unavailable, open a public issue titled “Private security contact requested” containing no vulnerability details. Wait for the maintainer to provide a private channel. No dedicated security email address or response SLA is currently advertised.

The maintainer will assess reports, coordinate a fix and disclosure with the reporter where possible, and publish relevant mitigation or upgrade guidance. There is no bug bounty promise. Test only systems you own or have permission to assess; do not access other users' data or disrupt services.

Maintainers should enable and verify private reporting before public product releases, revoke exposed credentials promptly, and assess workflow permissions and dependency changes during review.
