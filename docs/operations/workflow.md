# Portfolio workflow

1. **Research:** collect dated primary sources, alternatives, licensing constraints and enterprise use cases in docs/research.
2. **Decide:** record architecture choices and rejected alternatives in a product ADR. Unsettled research is not an approved implementation constraint.
3. **Plan:** create a product milestone and issues with user outcome, acceptance criteria, dependencies, security effects and verification steps.
4. **Build:** one branch per change; assign ownership before parallel agent work. Keep work scoped to the registered repository.
5. **Review:** an independent reviewer checks requirements, tests, migration safety, accessibility when relevant, and dependency licenses.
6. **Release:** require reproducible install, upgrade/rollback, backup/restore, security checks, license notices and versioned release notes. Use the release-readiness skill.
7. **Operate:** triage bugs and vulnerabilities, maintain compatibility and support policies, and update registry maturity using evidence.

## Roles

The founder is the initial maintainer and final decision maker. The coordinator decomposes work and integrates it. Research agents cite primary sources. Product and engineering agents implement accepted issues. Security and verification agents audit evidence independently. Agents do not substitute for accountable human ownership.

## Repository settings baseline

Public product repositories; issues enabled; squash merges; delete merged branches; GitHub Actions read-only by default. Enable dependency graph and vulnerability alerts where supported. Protect main with required CI when supported by account settings. Until a second maintainer exists, avoid mandatory independent approvals that lock the sole maintainer out; maintain review evidence in PRs.

## Secrets and access

Use repository/environment secrets for CI credentials. No tokens in prompts, registry or source control. Release credentials should have minimum scope and prefer short-lived authentication. Publishing packages, incurring costs and changing production access require task authorization.
