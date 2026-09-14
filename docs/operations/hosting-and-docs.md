# Public site and documentation

The initial public project hub and handbook use Astro Starlight in `site/`, published through GitHub Pages at https://zinnoberhaus.github.io/zinnober-haus/. This is a static project documentation site. Product applications, customer data and commercial transactions need their own deployment architecture.

## Content ownership

Edit `docs/operations`, `docs/research` and the root community policies. The build generates the handbook from those sources, while project pages derive from `registry/repos.json`. Generated files are ignored by Git. This avoids maintaining a second copy of policies. The landing page lives in `site/src/content/docs/index.mdx`.

Product research remains versioned with each product; product implementation docs should move with the product's release. Link versioned install/API material from the project page once it exists. Do not publish speculative install commands or empty API references.

Organize documentation by reader task: tutorials teach a first successful workflow; how-to guides solve a specific task; reference gives exact contracts; explanations record tradeoffs. Treat broken instructions as bugs. A behavior-changing PR should update relevant docs and exercise its commands.

## Local setup and publishing

Requires Node 24.11.1 or later and Python 3.11 or later.

```sh
npm ci --prefix site
npm run build --prefix site
npm run dev --prefix site
```

The Pages workflow builds on PRs and main. Only a successful build on main can deploy. It uses scoped GitHub Actions Pages permissions and never deploys fork PR code with write credentials. Site updates travel through review and the required validation check. Roll back by reverting the content/configuration change through a PR and redeploying main.

The static build produces search assets locally. It requires no paid search provider or runtime database. Do not place secrets or internal documents in the public content directories. `registry/services.json` records hosting status and ownership separately from product maturity.

## Optional Vercel path

The same site can be hosted on Vercel: use repository root, install command `npm ci --prefix site`, build command `SITE_BASE=/ npm run build --prefix site`, output directory `site/dist`, and set SITE_URL to the final site origin. Build and inspect a preview before production. A root-relative build must be verified separately from the Pages subpath build.

The connected Vercel identity has only a team named Microyee. No resources are created there under this setup. Select or create an explicitly authorized Zinnober Haus scope before linking; use Vercel Git integration to obtain PR previews. Verify the plan's commercial-use rules and spending limits before paid production deployment.

## Optional Mintlify path

Mintlify is a managed documentation alternative, not a requirement for the open-source site. Evaluate its Starter plan against required search, collaboration and API-reference features; verify current billing and export terms before adopting a paid plan. Its OSS program has eligibility criteria and is not a guaranteed grant. Preserve canonical source in Git and prototype a content migration before switching the production docs URL.

## Publication checklist

Check mobile layout, keyboard navigation, search, internal links, source/edit links and the two project routes. Verify the deployed URL from an unauthenticated client and record the actual deployment in the service registry. Custom domains require a domain controlled by the maintainer; do not invent or buy one as part of this setup.

See [hosting research](../research/hosting-docs-2026-09.md) for current primary sources and tradeoffs.
