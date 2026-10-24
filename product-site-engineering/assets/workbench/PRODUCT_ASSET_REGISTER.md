# {{PROJECT_NAME}} protected product assets

Initialized: {{DATE}}

The default rule is that layout and visual style may change, but an asset cannot be deleted, hidden, redirected, renamed beyond recognition, or have its saved data reinterpreted without explicit approval.

## Public capabilities

| Asset | Route/surface | Minimum discoverable entry | Saved data/contract | Protection requirement |
|---|---|---|---|---|
| Primary flow | `/` | Main navigation or landing action |  | Must remain usable end to end |

## Non-public or restricted capabilities

| Capability | Why restricted | Allowed exposure |
|---|---|---|
| Secrets and privileged configuration | Security boundary | Server only |
| Raw production logs and private user content | Privacy boundary | Authorized operations only |

## Before/after map for the current change

| Asset | Before | After | Discoverability impact | Data impact | Approval |
|---|---|---|---|---|---|
|  |  |  |  |  | not_needed |

## Change rules

1. List affected assets before visual or navigation work.
2. Request approval for deletion, hiding, merging, semantic changes, or less discoverable placement.
3. Migrate old data; never silently clear it.
4. Run a protected-asset regression check before declaring a restructure complete.
