# n8n Builder Skill for Claude Code

A Claude Code skill that builds, deploys, and manages n8n workflows through the n8n REST API. Describe what you want, and Claude builds the workflow JSON, deploys it, and verifies it. No clicking through the UI.

## What's included

- **SKILL.md** - Main skill file with API reference, connection format, expression syntax, and rules
- **references/rules.md** - API rules learned the hard way (settings whitelist, PUT safety, naming)
- **references/patterns.md** - Retry patterns, persistent state, expression gotchas
- **references/node-types.md** - Parameter reference for common node types
- **references/deploy.sh** - One-command deploy script (create + transfer + verify)
- **references/nodes/** - 89 pre-built node snippets (Google Sheets, Gmail, Slack, Telegram, AI agents, Shopify, Stripe, and 80+ more)

## Setup

1. Copy the `n8n-builder` folder into your `.claude/skills/` directory
2. Open `SKILL.md` and fill in your instance details:
   - n8n instance URL
   - API key (Settings > API in n8n)
   - Project ID (optional, for multi-project setups)
   - Credential aliases (run `GET /api/v1/credentials` to list yours)
3. Set environment variables for the deploy script:
   ```bash
   export N8N_API_KEY="your-api-key"
   export N8N_BASE_URL="https://your-instance.app.n8n.cloud/api/v1"
   export N8N_PROJECT_ID="your-project-id"  # optional
   ```
4. (Optional) Create a `references/workflow_index.md` file to track deployed workflows. The deploy script appends to it automatically if it exists, skips silently if it doesn't.

## Usage

Once installed, ask Claude Code to:

- "Create an n8n workflow that monitors a Google Sheet and sends Slack notifications for new rows"
- "Build a workflow that processes incoming Gmail attachments and saves them to Google Drive"
- "Set up an AI agent workflow that classifies incoming emails"

Claude checks the node library, builds the workflow JSON from pre-built snippets, deploys it via the API, and verifies it's running.

## How it works

The skill teaches Claude:

1. **Node library first** - before building any node from scratch, check `references/nodes/` for a pre-built snippet
2. **API safety** - always GET before PUT, verify after PUT, strip settings to whitelist
3. **Expression syntax** - the correct (and broken) ways to write n8n expressions
4. **Connection format** - how to wire nodes together, including AI sub-nodes
5. **Deploy pipeline** - create, transfer to project, verify node count

## The node library

89 ready-to-use node snippets with correct `typeVersion`, parameter structure, and credential placeholders. Covers:

- **Triggers:** Schedule, Gmail, Google Sheets, Tally, Telegram, Webhook, Form, Stripe, Calendly, HubSpot
- **Google:** Sheets (read/append/trigger), Gmail (send/trigger), Drive, Docs, Calendar
- **Communication:** Slack, Telegram, Discord, Microsoft Teams, Email (SendGrid, Brevo, Mailchimp)
- **AI/LLM:** AI Agent, OpenAI, Anthropic, Gemini, Chain LLM, Text Classifier, Structured Output Parser
- **CRM/PM:** HubSpot, Salesforce, Pipedrive, Zoho, Notion, Asana, Monday, ClickUp, Jira, Trello, Linear
- **E-commerce:** Shopify, WooCommerce, Stripe
- **Database:** Postgres, MySQL, Supabase, Airtable
- **Utilities:** Code, HTTP Request, Filter, IF, Switch, Merge, Set Fields, Split in Batches

## Adapting to your instance

The node snippets use `"YOUR_CREDENTIAL_ID"` placeholders. When Claude builds a workflow, it matches the node's credential type against your alias table in SKILL.md and swaps in the correct ID. Keep your credential table up to date.

## Requirements

- Claude Code
- n8n instance (Cloud or self-hosted) with API access enabled
- `python3` in PATH (used by deploy.sh to parse API responses)

## License

MIT
