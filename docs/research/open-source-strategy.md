# Open-source strategy

Research date: 2026-09-08. Recommendations below are project decisions to evaluate, not evidence of customer demand, legal clearance, or production readiness.

## Recommended starting position

Use Apache-2.0 for the umbrella repository and both products. Keep self-hosting, export, authentication, authorization, audit events, and backup/restore in the open-source product. Sell managed operation, support, migration, and deployment expertise when the capability exists. This is a proposed business model, not an existing commercial offering.

Apache-2.0 permits commercial redistribution and modification, includes an express patent license with termination conditions, requires preservation of applicable notices, and does not grant general trademark rights. It does not require downstream proprietary modifications to be published. These provisions make it a reasonable starting choice for reusable enterprise infrastructure; the adoption benefit is our inference, not a measured result. [Apache license text](https://www.apache.org/licenses/LICENSE-2.0)

| Choice | Benefit | Tradeoff | Recommendation |
| --- | --- | --- | --- |
| Apache-2.0 | Permissive reuse; express patent terms | Competitors can offer proprietary modifications | Default for all three repositories |
| AGPL-3.0 | Modified network services must offer corresponding source to interacting users under its terms | Customers need to evaluate their modification/integration obligations | Consider only if reciprocal source sharing is more important than permissive integration |
| Source-available restrictions on competitors or fields of use | Can constrain a particular business model | Conflicts with an unrestricted open-source promise | Do not describe such a license as open source |

The AGPL's additional obligation concerns modified versions used interactively over a network; it is not a blanket obligation to publish all software inside a company. Dependency combinations need individual review. [GNU AGPL text](https://www.gnu.org/licenses/agpl.en.html), [GNU license FAQ](https://www.gnu.org/licenses/gpl-faq.en.html)

The Open Source Definition requires free redistribution and prohibits discrimination against persons, groups, and fields of endeavor. Being downloadable or having a public repository alone does not establish those freedoms. [OSI definition](https://opensource.org/osd)

Before importing code, record its license and attribution requirements. A new root license does not relicense third-party material. Do not promise future dual licensing without understanding contributor rights; DCO signoff is a provenance certification, not copyright assignment. [Developer Certificate of Origin](https://developercertificate.org/)

## Enterprise adoption plan

Treat enterprise readiness as a verified release property. A repository scaffold is not enterprise software. First recruit design partners and validate their deployment constraints; no market sizing or willingness-to-pay evidence has been collected here.

For each product, require reproducible installation on a clean machine, explicit resource requirements, upgrade and rollback instructions, backup restoration into a fresh environment, tenant isolation tests, RBAC tests, secret management instructions, auditability, supported-version policy, and dependency inventories before a production recommendation. Publish the evidence with the release. For Zettel, test export/import and identity lifecycle. For Carthouse, test retries, cancellation, idempotency, recovery after worker loss, credential boundaries, and reproducibility of runs.

Use OpenSSF's published criteria as a maturity checklist for documentation, contribution process, releases, tests, and vulnerability handling. A checklist does not mean the project has earned a badge or certification. [OpenSSF criteria](https://www.bestpractices.dev/en/criteria?details=true)

## Governance and contribution

Start with founder-led governance, public design proposals, and documented reasons for decisions. Do not invent a foundation, board, independent maintainers, support team, or service-level agreement. Give contributors a clear path from reviewed contributions to narrowly scoped maintenance responsibility. Keep human review accountable even when agents prepare code.

Use inbound-equals-outbound licensing and DCO signoff. Review generated contributions for provenance, correctness, dependencies, tests, and sensitive data just like human-authored work. Keep architectural decisions and repository ownership discoverable in this umbrella repository; product issues belong to their product repository.

Enable GitHub private vulnerability reporting on each public repository and verify the reporting entry point. A SECURITY.md file alone does not enable it. If it is unavailable, GitHub recommends asking maintainers for a security contact without disclosing the vulnerability. [GitHub configuration](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository), [reporting guidance](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately)

## Names and trademarks

Keep the requested repository slugs `zettel` and `carthouse` while treating branding as provisional. Search performed: public web queries for Zettel GitHub notes, Carthouse software, and Carthouse software GitHub. Zettel is already used by multiple note-related projects, including [AlexW00/Zettel](https://github.com/AlexW00/Zettel) and [slhnx/zettel](https://github.com/slhnx/zettel). This establishes practical collision and discoverability risk; it does not establish infringement or registered trademark ownership. Use “Zinnober Haus Zettel” in descriptive copy during validation.

The limited Carthouse queries returned no useful exact software collision evidence. Absence in these results is not proof of availability. Neither name has received a comprehensive registry, domain, package registry, international, or common-law clearance search. No trademark filing has been made.

Before investing in launch branding, search relevant classes and similar marks in intended markets, including the [USPTO trademark database](https://www.uspto.gov/trademarks/search), and evaluate domains, package registries, and unregistered commercial usage. The Linux Foundation's release guide also recommends name checks and a trademark policy. [Linux Foundation release guide](https://www.linuxfoundation.org/hubfs/LF%20Research/LFResearch_AI_Data_Releasing_Internal_Code_Report.pdf)

## Launch gates

1. Public repository license, contribution instructions, governance, security policy, and accurate project status.
2. Working clean-machine quickstart with a tagged version and verified checks.
3. Export and operational recovery appropriate to each product.
4. Public roadmap distinguishing implemented, experimental, and planned features.
5. Verified private vulnerability reporting and clearly stated maintenance scope.
6. Branding clearance work before claims of exclusive names or significant brand spending.

These gates define future release evidence. This research document does not claim they already pass.
