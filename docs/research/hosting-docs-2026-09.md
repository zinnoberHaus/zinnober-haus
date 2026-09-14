# Public hosting and documentation research

Reviewed: **2026-09-14**. Scope: the Zinnober Haus public project hub and contributor documentation, with a path to separate Zettel and Carthouse product documentation. Sources are vendor documentation, official pricing pages, and upstream licenses checked on that date. Prices and program availability can change; no account signup, paid plan, domain purchase, or sponsorship acceptance is implied by this document.

## Recommendation

Start with an **Astro Starlight site built from this repository and published through GitHub Actions to GitHub Pages**. Use it for the open-source project directory, research, contribution guidance, agent handbook, public roadmap links, and operating documentation. This fits the present planning-stage products, uses the existing GitHub ownership boundary, and keeps documentation content and rendered output portable. It is our recommendation based on the comparisons below, not a vendor claim or a measured performance result.

Use **a separate Zinnober Haus Vercel Pro team** if the site becomes a commercial service storefront or needs Vercel's application deployment features. Cloudflare Pages is another static-hosting option when a Zinnober Haus account is available. Keep the build independent of either provider. Evaluate **Mintlify Starter** when browser-based editing and its managed documentation experience save enough maintenance effort; evaluate paid Mintlify only against a concrete need for its additional features. Starlight is the default because contributors can build and serve the complete static site without a documentation SaaS account.

The website is not a product runtime. It must describe Zettel and Carthouse as planning-stage projects until their repositories contain verified working releases. Product databases, workers, customer authentication, DAG execution, and enterprise deployments require their own architecture and operating evidence.

An open-source project can use a hosted service without making that service open source. GitHub Pages, Vercel and Cloudflare Pages are operated hosting services; the proposed portability comes from owning the source, dependency lockfile and static output. Mintlify is likewise a platform choice. Starlight and Docusaurus are the MIT-licensed software choices evaluated here.

## Hosting comparison

| Option | Verified entry cost and limits | Fit and tradeoff for this studio |
| --- | --- | --- |
| GitHub Pages | Available for public repositories on GitHub Free. Published site at most 1 GB; soft bandwidth limit 100 GB/month; deployments time out after 10 minutes. The soft 10-builds/hour limit excludes custom Actions builds. | Best initial home for a public OSS project hub and documentation. GitHub states Pages must not be used to run an online business, e-commerce, or a site primarily facilitating commercial transactions or commercial SaaS. It is static hosting, not the Zettel or Carthouse service runtime. [Availability](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [limits and permitted use](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Vercel Hobby | Free; restricted to personal, non-commercial use. | Do not assume Apache-2.0 licensing makes a business deployment eligible. A commercial studio website should use Pro or an explicitly approved program. [Hobby plan](https://vercel.com/docs/plans/hobby) |
| Vercel Pro | USD $20/month platform fee includes one deploying seat and $20/month usage credit; additional deploying seats cost $20/month each. Extra usage and add-ons are billable; taxes excluded. | Good managed choice when the studio needs commercial hosting, application deployments and collaboration. Keep the account/team separate from excluded projects and configure spend management before paid usage. [Pro plan](https://vercel.com/docs/plans/pro-plan) |
| Cloudflare Pages Free | Free tier; 500 builds/month, one concurrent build, 20-minute build timeout, 100 custom domains/project, 20,000 files/site and 25 MiB maximum per asset. Static requests are free and unlimited; Functions are metered under Workers rules. | Strong alternative for a static public site and docs with Git integration and previews. A distinct Cloudflare account/integration is required. Free static delivery does not mean free application compute or an enterprise SLA. [Pages limits](https://developers.cloudflare.com/pages/platform/limits/), [Functions and static pricing](https://developers.cloudflare.com/pages/functions/pricing/) |

The GitHub Pages recommendation is specifically for project information and public documentation. Revisit hosting when adding checkout, paid-service onboarding, or commercial application access. GitHub explicitly presents Pages as a way to publish information about a person, organization, or project; that does not remove its use restrictions. [What GitHub Pages hosts](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

Cloudflare's Pages product page advertises Git integration, protected sharing links, SSL and unmetered static delivery. Its more specific limits document still imposes project/build/file limits. Use the limits document for capacity planning, not the word “unlimited” alone. This research does not infer an unrestricted commercial-use guarantee from a missing restriction on a pricing page. [Pages overview](https://www.cloudflare.com/products/pages/)

Cloudflare also offers **Workers Static Assets**, which can serve files without invoking Worker code and combine static files with Worker routes. Evaluate it before starting a new dynamic Cloudflare application, rather than assuming Pages is the only Cloudflare deployment model. It is unnecessary for the initial project hub. [Static Assets](https://developers.cloudflare.com/workers/static-assets/)

## Documentation comparison

| Option | Source and hosting model | Capabilities relevant now | Main cost or operational tradeoff |
| --- | --- | --- | --- |
| Astro Starlight | MIT-licensed documentation framework; source and built site can be self-hosted. | Markdown/MDX, navigation, internationalization, typography, code highlighting and built-in Pagefind full-text search. | Maintain Node dependencies, build checks and hosting. Best initial fit for one public handbook with a small team. [Features](https://starlight.astro.build/), [search](https://starlight.astro.build/guides/site-search/), [license](https://github.com/withastro/starlight/blob/main/LICENSE) |
| Docusaurus | MIT-licensed React documentation framework emitting static files. | Documentation, custom React pages and a built-in documentation-versioning workflow. | Prefer when maintaining multiple materially different supported product versions makes versioned docs necessary. Versioning adds copies and contributor overhead, which its own documentation warns about. [License](https://github.com/facebook/docusaurus/blob/main/LICENSE), [deployment](https://docusaurus.io/docs/deployment), [versioning](https://docusaurus.io/docs/versioning) |
| Mintlify | Managed documentation platform with Git-backed MDX content; open-source components/templates do not establish that the entire hosted service is an OSS stack. | Starter includes five editor seats, custom domain, web editor, authentication, MCP and API playground. Pro adds assistant, agent, automations, previews and admin APIs. | Starter is $0. The pricing page displayed Pro at **$450/month with annual billing selected**; this is an annual-billing rate, not a verified month-to-month quote. Enterprise is quoted. [Pricing](https://www.mintlify.com/pricing), [Git-based setup](https://www.mintlify.com/docs/quickstart) |

**Mintlify portability needs precise wording.** Its custom Astro frontend can be deployed on another host, but search/assistant continue to use Mintlify services. The current headless feature table excludes the hosted web editor, authentication, API playground and several other hosted capabilities. Separately, a self-contained static-export API is available in private beta under an Enterprise agreement. This is not evidence that every Free/Pro customer can export the complete service or operate it offline. [Custom frontend](https://www.mintlify.com/docs/guides/custom-frontend), [static export availability](https://www.mintlify.com/docs/api/static-export/overview)

Starlight's getting-started guide still identifies it as beta software and recommends regular updates. Pin the tested dependency set, review upgrades through pull requests, and verify rendering and search after changes. This is a maintenance tradeoff of the recommended framework. [Starlight maintenance guidance](https://starlight.astro.build/getting-started/)

Mintlify changed AI billing on September 8, 2026: assistant answers and automation updates use fixed credit amounts, while work yielding no result is not charged; Pro/Enterprise editor and Slack agent usage is unlimited under the announced terms. Included credits and overage charges still need a budget. Avoid carrying old “Hobby” or older paid-plan figures into a purchase decision. [Dated billing announcement](https://www.mintlify.com/blog/outcome-based-ai-pricing)

For this portfolio, native docs versioning is a future product need. Keep the studio handbook current, label unreleased product instructions explicitly, and cut separate version documentation only when users actually operate multiple supported versions. If that requires substantial Starlight custom work, reconsider Docusaurus before inventing a versioning system. This is our design judgment, informed by Docusaurus's documented versioning tradeoffs.

## Sponsorship is optional, not a budget assumption

Mintlify's OSS program offers free Pro for qualifying **non-commercial** open-source projects. Its criteria include a recognized OSS license, no venture/revenue funding, and no for-profit company ownership or primary maintenance. Zinnober Haus's enterprise-product ambition does not establish eligibility; do not budget on a grant or describe the studio as eligible without a truthful application and acceptance. [Mintlify OSS program](https://www.mintlify.com/oss-program)

Vercel's OSS program page currently says applications are closed. It describes $3,600 in platform credits over three years for selected projects, with eligibility and evaluation criteria; Marketplace provider charges are not covered by those credits. Treat this as a program to monitor, not available funding. [Vercel OSS program](https://vercel.com/open-source-program)

## Concrete deployment architecture

Proposed file ownership and publishing boundaries:

```text
zinnober-haus/
  registry/           repository, service and agent metadata; no credentials
  docs/               authoritative shared research and operating guidance
  agents/             responsibilities, invocation and handoff documentation
  site/               Astro/Starlight presentation, navigation and public assets
  .github/workflows/  pull-request checks; main-only site publication

zettel/               owns Zettel product documentation alongside product code
carthouse/            owns Carthouse product documentation alongside product code
```

Publish one studio site initially at `https://zinnoberhaus.github.io/zinnober-haus/`. This is the expected GitHub project-site address, not a claim that it is deployed. In Astro, configure `site` as `https://zinnoberhaus.github.io` and `base` as `/zinnober-haus`; verify generated links and asset paths with that base. A custom domain can later use a root base after DNS ownership is verified. [Astro's GitHub deployment guide](https://docs.astro.build/en/guides/deploy/github/)

Recommended routes, with the GitHub repository base prepended:

| Route | Audience and source of truth |
| --- | --- |
| `/` | Studio introduction, accurate product status, repository links |
| `/projects/zettel/`, `/projects/carthouse/` | Product summaries generated from the registry; links to canonical product README, roadmap, issues and future product docs |
| `/handbook/` | Contribution, ticket lifecycle, security reporting, releases and governance |
| `/agents/` | Available roles, bounded assignments, handoffs and permitted actions |
| `/research/` | Dated research and decision links with primary-source citations |
| `/registry/` | Public repositories/services and their actual activation status |

Do not make contributors maintain two independent copies of the same operating page. Link to repository Markdown initially, or render an explicit allowlist of shared files at build time and fail if a required source is missing. Keep product-specific installation/reference material in its product repository; the studio site links to it. A future cross-repository docs build should pin source commits and display their provenance, rather than silently fetch changing default branches.

For each site change, the workflow should perform a locked dependency install, validation, production build and internal-link checks. The publication job runs only after successful checks on the protected production branch. Give the build job read-only repository access. The separate Pages deploy job needs `pages: write`, `id-token: write`, a dependency on the completed build, and the `github-pages` environment. This avoids requiring a personal access token for site publication. [GitHub custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

Use the same `site/` build for managed alternatives. A Cloudflare Pages project can connect the selected GitHub repository, with `site` as build root, the checked-in build command, and `dist` as output. Decide Git integration versus Direct Upload when creating it: Cloudflare documents that a Git-integrated project cannot later switch to Direct Upload. Custom subdomains can use a CNAME, while an apex Pages domain requires the zone on Cloudflare. [Git integration setup](https://developers.cloudflare.com/pages/get-started/git-integration/), [custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)

Vercel supports Astro static deployment. Use an explicitly selected Zinnober Haus team and project, the `site/` root, and a static build; there is no reason to add a server adapter merely to publish this handbook. Add product application projects separately when needed. [Astro on Vercel](https://vercel.com/docs/frameworks/frontend/astro)

## Documentation operations and verification

Use four document purposes: learning tutorials, task-focused how-to guides, factual reference and conceptual explanation. Keep the installation tutorial executable and short, reference generated from actual public interfaces where practical, and operational explanations clear about supported versions. This structure follows the primary Diátaxis framework. [Diátaxis](https://diataxis.fr/)

The documentation agent should own navigation, prose and source consistency. The hosting agent should own build/deploy configuration and deployment evidence. The security agent checks public-content boundaries, Actions permissions and dependency changes. An independent verifier checks the built website in a browser and through HTTP requests. These are role assignments, not separate service accounts with shared administrator credentials.

Before recording a service as `active`, verify its real account/project identity, live HTTPS URL, successful deployment tied to the expected commit, public accessibility in a signed-out browser, navigation, mobile layout, search, canonical/base URLs, 404 behavior and links to the correct product repositories. A green build alone is insufficient. Keep provider IDs and URLs in the registry, but keep tokens, billing details and private deployment logs out of public files.

Recovery should be ordinary source control: retain the source commit, dependency lockfile and build artifact for each publication, then redeploy the previous known-good commit if a publication is broken. Test the documented recovery path at least once before promising that it works. For a future custom domain, record where DNS is controlled and the previous target so migration has an explicit rollback. Domain availability and ownership have not been verified by this research.

## Budget and revisit triggers

The proposed GitHub Pages plus Starlight setup has **no required hosting or documentation subscription** for public repositories within the documented limits. Domain registration, paid runners, optional analytics, agent model usage and future product infrastructure are separate expenses. Do not market the entire studio as cost-free because the static site is free.

Revisit this decision when a commercial service page needs a different host, a release needs multiple supported docs versions, nontechnical editors need a managed editor, contributors need per-PR hosted previews, or demonstrated traffic exceeds host limits. Recheck current prices and account identity at that point. These triggers make an eventual Vercel/Mintlify purchase assessable against actual needs instead of anticipated enterprise scale.
