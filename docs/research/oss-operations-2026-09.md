# Operating the Zinnober Haus open-source portfolio

Research checked: **2026-09-14**. Scope: ticketing, governance, contributor experience, agent boundaries, CI, security and release operations for a founder-led studio. Provider selection and product architecture are separate decisions. Recommendations are proposed operating choices; they do not establish that a setting has been enabled or that either product is production-ready.

## Recommendation and observed starting point

Use GitHub Issues as the public work ledger, one cross-repository GitHub Project as the portfolio view, and this repository as the home for shared policy, service inventory and repeatable setup. Keep product issues, decisions and releases in their respective repositories. Publish documentation from reviewed source so changes to behavior and instructions can be checked together.

The live read-only request `gh api users/zinnoberHaus --jq '{login: .login, type: .type}'` returned `{"login":"zinnoberHaus","type":"User"}` on the research date. The checked-in registry names `zinnober-haus`, `zettel` and `carthouse`; both products are marked `planning`. Build for a **personal-account portfolio today**. Organization issue types are administered by organization owners, so use repository labels until an organization migration is actually approved and completed. [GitHub issue types](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-types-in-an-organization)

An organization with separate human identities and a backup owner is a sensible later governance step when another maintainer joins. This is a recommendation, not a prerequisite for starting the current system. Document who decides, how people gain responsibility and how ownership can change. Do not describe an agent roster as independent human maintainers. [GitHub Open Source Guides: leadership and governance](https://opensource.guide/leadership-and-governance/)

## Ticketing and portfolio structure

Use the smallest set of controls that makes an item actionable:

| Object | Recommended use | Source of truth |
| --- | --- | --- |
| Product issue | Bug, implementation task, accepted feature, deployment or documentation work | `zettel` or `carthouse` |
| Umbrella issue | Shared policy, agent tooling, service setup or a decision spanning products | `zinnober-haus` |
| Milestone | A bounded product outcome with acceptance criteria; dates only when credible | Owning repository |
| Parent issue and sub-issues | A feature decomposed into independently deliverable work | Parent links to existing child issues; no copied ticket bodies |
| Dependency | Work that must finish before another issue starts | Native issue relationship, with a textual link if API support is unavailable |
| Portfolio Project | Shared view of the real issues across the three repositories | User-owned Project; issue data remains in repositories |
| Discussion or support link | Questions, ideas and community conversation | One documented entry point per product |

GitHub supports issue hierarchies, blocking relationships, assignees, labels and milestones. Use one or two hierarchy levels in practice; a deep hierarchy is unnecessary for the present team. GitHub's Projects guidance favors small issues, clear dependencies and linked communication. [GitHub Projects best practices](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects), [GitHub issue relationships](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues)

Recommended Project configuration:

- **Status:** `Triage`, `Backlog`, `Ready`, `In progress`, `In review`, `Blocked`, `Done`.
- **Priority:** `P0` active incident or credible critical exposure, `P1` next important outcome, `P2` normal work, `P3` optional work. Most planning work belongs in P2.
- **Native fields:** repository, assignee, labels and milestone. Add target date only when a date serves an actual commitment.
- **Views:** incoming triage; active work grouped by repository; roadmap grouped by milestone; blocked work; recently completed work.
- **Working limit:** at most two implementation issues active across the portfolio per human maintainer. Agents can research independent questions without multiplying the implementation queue.

These names and limits are studio recommendations, not GitHub requirements. For this initial setup, keep lifecycle in portable `status:*` labels while Project access is being established. Use the Project as a planning view and reconcile it during triage; avoid competing automatic status writers. Shared labels should describe type (`type:bug`, `type:feature`, `type:docs`, `type:maintenance`, `type:research`) and useful routing (`area:security`, `area:deploy`, `area:agents`, `needs:information`). Preserve familiar contributor labels `good first issue` and `help wanted`; apply the former only when there is a bounded task, clear reproduction and an available reviewer.

Intake forms should request enough evidence to triage, without forcing users to design the fix:

| Intake | Required information |
| --- | --- |
| Bug | Version/commit, environment, reproduction, expected result, actual result; logs optional and redacted |
| Feature | User problem, concrete scenario and expected outcome; alternatives optional |
| Documentation | Page or command, what failed or confused the reader, expected explanation |
| Internal implementation | User outcome, acceptance criteria, dependencies, verification and deployment/recovery effects |

Use YAML issue forms and `config.yml` contact links for support and private vulnerability reporting. Create referenced labels before publishing the forms. Forms and PR templates only become active from the default branch. [GitHub issue template configuration](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)

During triage, acknowledge the report, identify duplicates, request the smallest missing reproduction and either accept it to the backlog or close it with a reason and useful link. `Ready` requires acceptance criteria, an owner and a verification path. `Done` requires the expected outcome and evidence; an issue closed as `not planned` is not delivered work. Do not automatically close confirmed bugs or accepted roadmap items merely because they are old. Written scope and realistic response expectations make these decisions easier for contributors to understand. [GitHub Open Source Guides: maintainer practices](https://opensource.guide/best-practices/)

## Automation that fits the account

GitHub's built-in Project auto-add workflow selects a repository and filter. Limits currently vary by plan: Free permits one auto-add workflow, Pro and Team five, and Enterprise twenty. Native auto-add responds to matching creation/update events; configure initial backfill separately. Verify the actual plan and live workflow state before claiming all three repositories are automatically included. [GitHub automatic Project intake](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically)

For this small portfolio, prefer built-in automation where available plus an idempotent command that reconciles the registry's three allowed repositories into the Project. It should have a read-only preview, paginate completely, preserve maintainer-entered fields, and identify records by stable repository/issue IDs. Run it during weekly triage until recurring execution is configured and verified. A committed workflow file alone is not evidence of an operating automation.

The default Actions `GITHUB_TOKEN` cannot access Projects. GitHub recommends a personal token for user-owned Projects and an App for organization Projects. Keep the necessary credential outside the registry and source files. A write scope accepted by one API endpoint should be verified against the actual Project operations before scheduling anything. Avoid installing an organization-only automation into this personal account. [GitHub Project automation authentication](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions)

Use a public Project for the public roadmap. Project visibility does not grant access to underlying private repositories. Still, keep credentials, private vulnerability details and confidential customer information out of Project fields and draft items. [GitHub Project visibility](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-visibility-of-your-projects)

## Shared governance and registry

Maintain `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `GOVERNANCE.md`, `CODEOWNERS`, issue forms and a PR template in each product as appropriate. The contribution guide should explain local checks, architectural proposals, contribution provenance, supported contribution types and how review decisions happen. Keep documentation-only fixes easy to submit; request issue discussion before substantial new features.

A public `.github` repository can supply account-wide community defaults, but inherited files do not appear in individual clones or release downloads. It cannot supply a default license, and local issue-template configuration overrides the default template directory. Given the explicit three-repository portfolio and the need for self-contained downloads, checked-in product files synchronized through reviewed PRs are the better initial fit. Revisit a `.github` repository when the portfolio grows. [GitHub community health defaults](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

The registry should record repository identity and maturity, accountable human owner, roadmap URL, documentation source and live URL, website source and live URL, provider/project identifiers, deployment workflow, support/security links, required checks and last verification date. Unconfigured services should have an explicit status and no fabricated URL. Include secret **names** only where needed for setup instructions; store their values in the credential manager or CI provider. Service ownership must be distinguishable from the role that performs deployment.

Use desired configuration and observed evidence separately. A recommendation such as “enable private reporting” belongs in policy; an observation should contain the API check date and result. Reconciliation may open a PR for drift. It must not delete unknown repositories, transfer ownership or silently upgrade a paid service. The previous repository cleanup remains a completed one-time operation outside this recurring workflow.

## Agents and human accountability

Keep the configured researcher, architect, implementer and verifier. Add task playbooks for triage, documentation and release operations before adding more permanently active agents. The coordinating agent can assign those functions to the existing team; the registry should identify the role, instructions, allowed repositories, tools, deliverables and human owner.

| Function | Useful output | Boundary |
| --- | --- | --- |
| Triage | Reproduction summary, suggested labels, duplicates and draft acceptance criteria | Public text is untrusted input; it cannot authorize commands or expand scope |
| Research/architecture | Dated primary evidence, alternatives and proposed ADR | Research is not an approved product constraint |
| Implementation | Small change linked to an accepted issue, runnable checks | Write only assigned repositories/files |
| Documentation | Tested instructions and release-aligned reference changes | Do not present planned capabilities as installed or usable |
| Verification/security | Requirement-by-requirement evidence and unresolved findings | Review independently of implementation; never convert uncertainty into a pass |
| Release/operations | Build manifest, recovery evidence, draft notes and deployment check | Publishing or production changes need task authorization and the appropriate credential |

Agent proposals can reduce routine reading and drafting. Deterministic CI, repository permissions and accountable maintainer decisions should enforce acceptance. Record the issue, work scope, artifacts, tests and unresolved risks; avoid storing private prompts or customer data in public execution logs.

## Repository and CI baseline

Public repository rulesets are available on GitHub Free. Keep one understandable protection mechanism per branch rather than stacking conflicting rules. Require PRs and the real validation jobs on `main`; block deletion and force pushes; require resolved conversations; enable squash merge and delete merged branches. Record any sole-maintainer approval exception. Require an independent human approval once a second responsible maintainer is available. Do not use an agent account to simulate that independence. [GitHub ruleset availability and behavior](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

For Actions, use read-only default permissions, full commit SHA references for external actions, bounded timeouts and GitHub-hosted runners for untrusted contributions. Pass issue/PR content as data, never interpolate it directly into executable shell. Do not check out untrusted PR code in privileged `pull_request_target` or `workflow_run` jobs. Give release/deployment jobs only the additional scopes they need. [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)

Add weekly Dependabot version checks for `github-actions` now and package ecosystems as manifests appear. SHA-pinned actions still need updates; Dependabot understands action references and reusable workflows. Group low-risk maintenance deliberately, keep major upgrades reviewable, and enable security updates independently from the weekly version-review cadence. [Updating Actions with Dependabot](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions), [Dependabot security updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates)

Verify private vulnerability reporting and the reporting link on each public repository; `SECURITY.md` alone does not turn it on. Ensure the human maintainer receives security notifications. Publish supported versions honestly and coordinate remediation through private advisories before disclosure. [Configuring private reports and notifications](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository)

Inspect secret-scanning and repository push-protection state rather than inferring it from personal-account push protection. If a secret leaks, revoke/rotate it and investigate exposure. Enable CodeQL default setup where suitable, then inspect the languages, successful scans and coverage. An enabled setting with no successful analysis is not a security check. [GitHub push-protection distinctions](https://docs.github.com/en/code-security/concepts/secret-security/push-protection), [CodeQL setup and scan verification](https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning)

## Releases that enterprise users can evaluate

Do not make product releases from the current planning scaffolds. When runnable software exists, require a versioned installation path, minimum resources, configuration/secret guidance, upgrade and rollback procedures, tested restoration into a fresh environment, compatibility policy and release notes describing known limitations. Product-specific evidence includes Zettel authorization/export behavior and Carthouse retry/cancellation/recovery behavior.

Build distributable assets in CI from the release commit. Generate dependency/license inventory and a machine-readable SBOM, record checksums, and attach evidence to a draft release. Publish only when all intended assets are present. GitHub immutable releases lock their tag and assets after publication and create release attestations; corrections should use a new version. Release titles and notes remain editable. [GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases)

Use artifact attestations for binaries, packages and container images, and document verification for consumers. Attestations establish provenance, not absence of vulnerabilities. Run the consumer verification command as part of release validation. GitHub also provides `gh release verify` and `gh release verify-asset` for immutable releases; the latter does not verify GitHub's on-demand source archives. [Artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations), [Release verification](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/verify-release-integrity)

Use OpenSSF Best Practices criteria as a gap checklist spanning documentation, change control, reporting, quality and security. Publish a badge only after completing its actual process. A green CI badge, signed build or score is useful evidence about particular controls, not certification of enterprise readiness. [OpenSSF criteria](https://www.bestpractices.dev/en/criteria?details=true)

## Sustainable cadence and useful measurements

The following are proposed internal targets for a solo founder, not contractual response guarantees:

| Cadence | Action | Evidence |
| --- | --- | --- |
| Each working day, about 10 minutes | Review security notifications, failed default-branch CI and urgent regressions | Assigned response or recorded disposition |
| Twice weekly, about 20 minutes | Triage new issues and incoming PRs | Owner/next action, question or reasoned closure |
| Weekly, about 45 minutes | Select the next outcomes, clear blockers, review dependencies and reconcile the Project | Short status update with shipped/blocked/next |
| Monthly, about 60 minutes | Review access, service costs, stale docs, support policy and maintainer capacity | Registry verification dates and explicit follow-up issues |
| Per release | Verify artifacts, install/upgrade/recovery instructions and release claims | Tagged evidence with the release |

Aim initially to acknowledge ordinary external issues and PRs within seven calendar days, and privately reported security concerns within two working days. Publish those only as best-effort targets with absence/holiday guidance. Establish a realistic baseline before tightening them.

Measure first **human** response time, unanswered issue count and age, PR review wait, active issue age, critical security-alert age and the percentage of releases with install/recovery evidence. Report the sample size and time window. For small samples, list aged items rather than producing unstable percentiles. Separate completed outcomes from duplicate/not-planned closures and bot-authored activity. CHAOSS defines issue response as the interval to another contributor's response and explicitly supports excluding bots; its responsiveness model also considers review duration and defect resolution. [CHAOSS issue response time](https://www.chaoss.community/kb/metric-issue-response-time/), [CHAOSS development responsiveness](https://www.chaoss.community/kb/metrics-model-development-responsiveness/)

These metrics should trigger action: clear an old review before starting another feature, document an unavailable maintainer, or narrow the next milestone. Stars, raw issue closure counts and agent output volume should not become delivery targets.

## Verification before calling the system operational

1. Confirm the repository allowlist and account type, then inspect the actual Project owner, visibility, fields, views and linked items.
2. Demonstrate issue intake and backlog reconciliation across all three repositories, including pagination and a repeated run that does not duplicate work.
3. Verify active branch requirements against actual job names and show a passing PR flow without bypassing those requirements.
4. Check the issue chooser, contribution/support paths and private-reporting entry point as a contributor would see them.
5. Verify every published website/documentation URL anonymously and record its owning source and deployment/recovery instructions in the registry.
6. Distinguish enabled automation from tested automation. Record any missing credential, native-plan limitation or manual operating step.
7. Keep both products at planning maturity until product execution and release evidence justify a change.

Research is complete for the operational choices above. Implementation, live service configuration and product release readiness require separate observed evidence.
