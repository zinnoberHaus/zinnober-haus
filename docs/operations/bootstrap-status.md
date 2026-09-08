# Bootstrap status — 2026-09-08

## Established

- Public product repositories: Zettel and Carthouse, with product research, community policies, Apache-2.0 license and planning-artifact CI.
- Portfolio registry, shared agent roles, two validated repository skills and operating workflow.
- Research preserves the full product ambitions and separates proposed capabilities from implemented software.

## Cleanup blocker

The initial inventory contained 13 repositories. Preserve zinnober-haus; exclude microyee-ai and mircoyee-ai everywhere. The 12 other original repositories were mirrored locally and all mirrors passed `git fsck --full`. Issue, pull-request and release metadata were also exported. Backups remain outside this public repository.

The first deletion attempt returned HTTP 403 because the active GitHub credential lacks `delete_repo`. No repository was deleted. The account owner must authenticate with that scope before cleanup can proceed. Do not broaden access to unrelated accounts.

These backups preserve Git history and selected metadata, not all GitHub-hosted state (settings, secrets, packages, release binaries, LFS and discussions are not comprehensively backed up).

## Product readiness

Both products remain in planning. Implementation, installable distributions, enterprise validation and feature parity are not complete. Follow the research delivery gates and product issues before making readiness claims.
