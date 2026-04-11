---
name: n8n-builder
description: Build, deploy, and manage n8n workflows via the REST API. Use when asked to create, update, debug, or activate n8n workflows.
allowed-tools: Bash, Read, Write, Edit
---

# n8n Workflow Skill

Build, deploy, and manage n8n workflows entirely through the API using pre-built node snippets and battle-tested patterns.

## Setup

Before first use, fill in your instance details below. Get your API key from n8n Settings > API.

- **URL:** `https://YOUR_INSTANCE.app.n8n.cloud`
- **API Key:** `YOUR_API_KEY`
- **Project ID:** `YOUR_PROJECT_ID` (optional, for multi-project instances)

### Credentials

Map your credential aliases here. Get IDs from `GET /api/v1/credentials`.

| Alias | Credential Type | ID | Name |
|---|---|---|---|
| gmail | gmailOAuth2 | | |
| sheets | googleSheetsOAuth2Api | | |
| slack | slackOAuth2Api | | |
| openai | openAiApi | | |
| anthropic | anthropicApi | | |
| telegram | telegramApi | | |
| notion | notionApi | | |

Add rows as needed. The `name` field must match exactly what you named the credential in your n8n instance (Settings > Credentials). Node snippets in `./references/nodes/` use placeholder credentials — Claude swaps in your IDs from this table when building workflows.

---

## Quick Start: New Workflow

1. Check `./references/nodes/` for pre-built node snippets. Copy, rename, set positions.
2. Build the JSON (nodes array + connections object).
3. Write to `/tmp/<name>.json`.
4. Run: `bash ./references/deploy.sh /tmp/<name>.json`
5. Done. Script handles POST, project transfer, verify, and index update.

---

## Connection Format

```json
"Source Name": { "main": [[{"node": "Target", "type": "main", "index": 0}]] }
```

- **Fan-out** (one source, multiple targets): `"main": [[{"node": "A", ...}, {"node": "B", ...}]]`
- **Merge inputs**: source A connects with `"index": 0`, source B with `"index": 1`
- **IF branching**: `"main": [ [true targets], [false targets] ]`
- **AI sub-node**: `"ai_languageModel": [[{"node": "Model Name", "type": "ai_languageModel", "index": 0}]]`
- **AI tool sub-node**: `"ai_tool": [[{"node": "Tool Name", "type": "ai_tool", "index": 0}]]`

---

## Workflow JSON Structure

```json
{
  "name": "Workflow Name",
  "nodes": [...],
  "connections": {...},
  "settings": { "executionOrder": "v1", "callerPolicy": "any" }
}
```

- POST body must NOT include `active` field (read-only, use PATCH to activate)
- Strip all settings keys except: `executionOrder`, `callerPolicy`, `saveDataSuccessExecution`, `errorWorkflow` (if exists)
- Keys that MUST be removed before PUT: `binaryMode`, `availableInMCP`, `timeSavedMode`

---

## API Endpoints

```
POST   /api/v1/workflows              — create
GET    /api/v1/workflows/{id}         — fetch (ALWAYS before PUT)
PUT    /api/v1/workflows/{id}         — update
PATCH  /api/v1/workflows/{id}         — activate/deactivate: { "active": true }
PUT    /api/v1/workflows/{id}/transfer — move to project
GET    /api/v1/executions/{id}?includeData=true — fetch execution data
GET    /api/v1/credentials            — list all credentials
```

---

## Rules

- **GET before PUT** — never modify from cache, always fetch current version first
- **Verify after PUT** — fetch again and confirm changes landed
- Connections use node **NAMES**, never UUIDs
- Prefer native platform nodes over HTTP Request (shows platform logos in the UI)
- Code nodes with `!` characters: write JS to `/tmp/*.js` first, then read it back (Python string escaping turns `!` into `\!`)
- `includeData=true` on execution fetches (without it, `data.resultData.runData` is null)
- `callerPolicy` allowed values: `any`, `none`, `workflowsFromAList`, `workflowsFromSameOwner`

---

## Expression Syntax (HTTP Request body)

- WORKING: `={{ ({ key: value }) }}` — object in parens, no JSON.stringify
- BROKEN: `={{ JSON.stringify({...}) }}` — causes "invalid syntax"
- BROKEN: `={{ }}` embedded inside static JSON body — doesn't evaluate
- Cross-node ref: `$item(0).$node["NodeName"].json.field`

---

## Node Library

Pre-built node snippets live in `./references/nodes/`. Each file is a ready-to-use JSON node object.

**Mandatory workflow:**
1. Before building any node, glob `./references/nodes/*.json` to see what's available.
2. If the node type exists in the library, copy its JSON and customize (name, position, parameters). Do NOT write from scratch.
3. If the node type does NOT exist in the library, build it from scratch.
4. After the workflow is deployed, save any new node types you built to the library as `./references/nodes/<node-name>.json`.

---

## Deep References (load only when needed)

- `./references/patterns.md` — retry patterns, persistent state, expression gotchas
- `./references/rules.md` — PUT/POST rules, settings whitelist, naming conventions
- `./references/node-types.md` — parameter reference for common node types
