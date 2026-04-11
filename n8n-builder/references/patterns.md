# n8n Patterns & Gotchas

## Conditional Retry Pattern (NOT Loop Over Items)

Do NOT use Loop Over Items for conditional retries. Use:
- **Code node:** `$('Source').all()` + `$input.item.json.index || 0`
- **Set node** (on retry path): increments index
- **If node:** `index >= maxRetries` → exit, else → back to Code node

**Why:** Loop Over Items loopback path overwrites `$json` with the returning node's output, destroying original data on iteration 2.

---

## Persistent State

Never use `$getWorkflowStaticData` on n8n Cloud — causes execution hangs (write lock never releases).
Use a database table instead (e.g., Postgres: `UPDATE run_counter SET count = count + 1 WHERE id = 1 RETURNING count`).

---

## JS Escaping

If JS code contains `!` (like `!=`), write it to `/tmp/filename.js` and read it back. Python string escaping turns `!` into `\!` inside n8n.

---

## Expression Gotchas

- `={{ ({ key: value }) }}` — working syntax for JSON body expressions
- `JSON.stringify` wrapper causes "invalid syntax" — avoid
- `={{ }}` embedded inside static JSON body does NOT evaluate — use full expression mode
- Cross-node ref inside body: `$item(0).$node["NodeName"].json.field` — NOT `$('NodeName').first()`
- `.toBoolean()` on checkbox fields — some form providers send `"true "` (string with trailing space)

---

## GET Execution

Always set `includeData=true` — without it, `data.resultData.runData` is null.

---

## API POST Rules

- **Do NOT include `active` in POST body** — it's read-only. Use PATCH to activate after creation.
- **callerPolicy allowed values:** `any`, `none`, `workflowsFromAList`, `workflowsFromSameOwner` (NOT `workflowsFromAnyUser`).
