# Frontend quality and protected assets

Use this reference for new flows, visual restructuring, navigation changes, forms, responsive work, or client-side persistence.

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

## Client persistence

- State exactly where data is saved and whether it syncs across devices.
- Version saved structures and migrate old shapes without erasing unknown fields.
- Test malformed, partial, older, and future-version data.
- Provide a clear delete/export path when the product promise requires it.
- Treat client flags as presentation hints, never as server authorization.

## Public-content boundary

The browser bundle, source maps, DOM, network responses, storage, and public environment variables are public surfaces. Do not ship secrets, private prompts, internal retrieval records, admin status, raw error details, or server-only decision rules to them.
