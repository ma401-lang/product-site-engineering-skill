# Frontend quality and protected assets

Use this reference for new flows, visual restructuring, navigation changes, forms, responsive work, or client-side persistence.

Before choosing a visual direction, freeze the relevant product benchmark. Record why references are comparable, which principles apply, and which brand or interaction details must not be copied. A gallery of attractive screenshots is not a benchmark. See [benchmark-first.md](benchmark-first.md).

## Protected-asset map

Before restructuring, inventory:

- public routes and their purpose;
- minimum discoverable entry points;
- actions and whether they are real, unavailable, or hidden;
- local/session storage keys, cookies, IndexedDB, and URL state;
- historical data shapes and migration behavior;
- deep links, redirects, metadata, and share URLs;
- future-facing billing or membership code explicitly protected by the owner.

Create an internal table:

| Asset | Before | After | Data impact | Discoverability impact | Approval needed |
|---|---|---|---|---|---|

If a protected asset becomes less discoverable or changes meaning, stop for approval. A visual cleanup is not implicit permission to remove product scope.

## State matrix

For each interactive surface, decide which states apply:

| State | Required behavior |
|---|---|
| Initial | Explain the next useful action; do not show fake data |
| Empty | Say what is absent, where future data will appear, and what the user can do |
| Loading | Preserve layout, announce progress, disable only conflicting actions |
| Success | Confirm the durable result, not merely the click |
| Validation error | Attach plain-language feedback to the field or action |
| Timeout | Explain uncertainty; do not claim failure if the server outcome is unknown |
| Retry | Safe to repeat; preserve user input where appropriate |
| Duplicate | Prevent or reconcile duplicate writes |
| Offline | Explain which operations remain local and which require a connection |
| Stale data | Refresh, merge, or show conflict; do not silently overwrite newer data |
| Storage denied | Keep the current work when possible and expose recovery |
| Cancelled | Stop work and leave a coherent state |

## Forms and async actions

- Validate at both client and server; the server is authoritative.
- Give pending actions a stable disabled state and accessible label.
- Use idempotency keys or a server uniqueness rule for expensive or durable writes.
- Distinguish timeout from confirmed rejection.
- Keep error messages useful to users and attach the request ID when support may need it.
- Do not render backend stack traces, provider responses, SQL messages, or internal configuration.

## Responsive and accessible behavior

Test the actual primary flow, not only screenshots:

- 360 px and a representative larger mobile width;
- keyboard-only navigation with visible focus;
- correct labels, names, roles, and status announcements;
- screen-reader-friendly error and loading changes;
- reduced motion where animation is non-essential;
- text zoom and long localized strings;
- software keyboard covering sticky inputs;
- color contrast and non-color status cues;
- touch targets and no accidental horizontal scrolling.

Use the current [WCAG 2 resources](https://www.w3.org/WAI/standards-guidelines/wcag/) for conformance claims. Automated scans are useful regression checks, but they do not replace keyboard, focus, announcement, zoom, and real-task review.

## Performance and compatibility

- Put measurable performance targets in the benchmark and record whether evidence is lab, preview, field, or user-device data.
- Inspect request waterfalls, server timing, JavaScript execution, fonts, images, hydration, third-party scripts, and layout shifts before adding custom infrastructure.
- Test the browsers and devices the product actually supports; do not infer compatibility from one Chromium run.
- Preserve useful content and controls when JavaScript, storage, a third-party dependency, or a slow network fails where the product contract requires resilience.
- Prefer semantic HTML and platform behavior before recreating controls in JavaScript.
- Treat performance regressions in the primary flow as product regressions, not optional polish.

Use current [Core Web Vitals](https://web.dev/explore/learn-core-web-vitals) definitions when they are part of the benchmark and [Playwright's testing guidance](https://playwright.dev/docs/best-practices) for user-visible browser scenarios. Record the source and verification date rather than copying mutable thresholds into this Skill.

## Metadata, discoverability, and sharing

For public content surfaces, decide explicitly:

- unique, useful page title and description;
- canonical URL, redirects, trailing-slash and duplicate-content behavior;
- robots and sitemap behavior, including `noindex` on previews or private pages;
- language, direction, locale-sensitive text, dates, numbers, and longer translations;
- social/share metadata and a working fallback image;
- structured data only when it truthfully describes visible content;
- stable, descriptive routes and internal links;
- a useful not-found state and preserved deep links after migration.

Search visibility is an outcome to observe, not a guaranteed consequence of adding tags. Use current [Google Search documentation](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) when search discovery is in scope, while keeping people-first information architecture as the product requirement.

## Client persistence

- State exactly where data is saved and whether it syncs across devices.
- Version saved structures and migrate old shapes without erasing unknown fields.
- Test malformed, partial, older, and future-version data.
- Provide a clear delete/export path when the product promise requires it.
- Treat client flags as presentation hints, never as server authorization.

## Public-content boundary

The browser bundle, source maps, DOM, network responses, storage, and public environment variables are public surfaces. Do not ship secrets, private prompts, internal retrieval records, admin status, raw error details, or server-only decision rules to them.
