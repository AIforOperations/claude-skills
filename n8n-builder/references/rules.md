# n8n API Rules

> Applies to ALL n8n workflow modifications. Non-negotiable.

## PUT Workflow — Settings Whitelist
Strip `settings` to ONLY these keys before any PUT:
- `executionOrder`
- `saveDataSuccessExecution`
- `callerPolicy`
- `errorWorkflow` (only if workflow actually has one)

Keys that MUST be removed: `binaryMode`, `availableInMCP`, `timeSavedMode`, and any others not listed.

## HTTP Request Node — JSON Body Expressions
- **Working syntax:** `{{ ({ ...js object... }) }}` — object in parens, NO `JSON.stringify`
- **Cross-node reference inside body:** `$item(0).$node["NodeName"].json.field` — NOT `$('NodeName').first()`
- `={{ }}` embedded inside static JSON body does NOT work — use full expression mode
- `JSON.stringify` wrapper causes "invalid syntax" errors — avoid

## General PUT Rules
- Always fetch CURRENT workflow before modifying — never work from cache (stale cache has caused deleted nodes/rules in production)
- After every PUT, fetch again and verify the change landed
- n8n stores connections using node NAMES (not UUIDs) — never convert to UUIDs
- Only change specific connection entries needed — never iterate and rewrite all

## Get an Execution (Error Workflows)
- Always set `includeData: True` — without it, `data.resultData.runData` is null

## Workflow Placement
- After POST, transfer to your project with: `PUT /api/v1/workflows/{id}/transfer` body `{"destinationProjectId": "YOUR_PROJECT_ID"}`
- POST body must NOT include `active` field (read-only). Use PATCH to activate after creation.
- `callerPolicy` allowed values: `any`, `none`, `workflowsFromAList`, `workflowsFromSameOwner` (NOT `workflowsFromAnyUser`)

## Naming
- Use clean, descriptive workflow names. No `[DEMO]` or similar tags.
- Use built-in platform nodes (Shopify, Google Sheets, etc.) over HTTP Request nodes when available. Shows platform logos in the UI.

## Code Nodes
- Write JS code to /tmp/*.js file — inline Python strings mangle `!` as `\!` in n8n
- Switch expressions: always use `.toBoolean()` on checkbox fields (some form providers send boolean as string "true " with trailing space)
