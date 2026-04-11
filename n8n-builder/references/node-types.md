# n8n Node Types — Parameters Reference

## Node Structure

```json
{
  "id": "<uuid>",
  "name": "Human Readable Name",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [0, 0],
  "parameters": { ... },
  "credentials": {
    "credentialType": { "id": "YOUR_CREDENTIAL_ID", "name": "Your Credential Name" }
  }
}
```

---

## Code Node (`n8n-nodes-base.code`, typeVersion: 2)
```json
{
  "jsCode": "const item = $input.first().json;\nreturn [{ json: { ... } }];",
  "mode": "runOnceForAllItems"
}
```
- `$input.first().json` — first item
- `$('NodeName').all()` — all items from named node
- `$input.item.json.index || 0` — current item index
- **CRITICAL:** If JS contains `!` (like `!=`), write it to `/tmp/filename.js` and read it back — Python string escaping turns `!` into `\!` inside n8n

---

## HTTP Request Node (`n8n-nodes-base.httpRequest`, typeVersion: 4.2)
```json
{
  "method": "POST",
  "url": "https://api.example.com/endpoint",
  "sendHeaders": true,
  "headerParameters": {
    "parameters": [{ "name": "x-api-key", "value": "KEY" }]
  },
  "sendBody": true,
  "specifyBody": "json",
  "jsonBody": "={{ ({ url: $json.url, fields: $json.fields }) }}"
}
```
**Expression syntax rules:**
- WORKING: `={{ ({ key: value }) }}` — object in parens, no JSON.stringify
- BROKEN: `={{ JSON.stringify({...}) }}` — causes "invalid syntax"
- BROKEN: `={{ }}` embedded inside static JSON body — doesn't evaluate
- Cross-node ref inside body: `$item(0).$node["NodeName"].json.field` — NOT `$('NodeName').first()`

---

## Switch Node (`n8n-nodes-base.switch`, typeVersion: 1)
```json
{
  "mode": "rules",
  "sendToAll": true,
  "rules": [
    { "type": "string", "value": "={{ $json.field.toBoolean() }}", "operation": "equal", "operation2": "true" }
  ]
}
```
- Each rule = one numbered output
- Always use `.toBoolean()` on checkbox fields

---

## Gmail Node (`n8n-nodes-base.gmail`, typeVersion: 2.2)
```json
{
  "sendTo": "={{ $json.email }}",
  "subject": "Subject line",
  "emailType": "text",
  "message": "=Body text here",
  "options": {
    "appendAttribution": false,
    "attachmentsUi": {
      "attachmentsBinary": [{ "property": "={{ Object.keys($binary).join(',') }}" }]
    }
  }
}
```
Credentials: `"gmailOAuth2": { "id": "YOUR_CREDENTIAL_ID", "name": "Your Gmail" }`

---

## Tally Trigger (`n8n-nodes-tallyforms.tallyTrigger`, typeVersion: 2)
```json
{
  "formId": "<FORM_ID>"
}
```
Credentials: `"tallyApi": { "id": "YOUR_CREDENTIAL_ID", "name": "Tally account" }`

---

## Merge Node (`n8n-nodes-base.merge`, typeVersion: 2)
```json
{ "mode": "append" }
```

---

## Sticky Note (`n8n-nodes-base.stickyNote`, typeVersion: 1)
```json
{ "content": "## Title\nNotes here", "height": 200, "width": 400, "color": 4 }
```

---

## Google Sheets Node (`n8n-nodes-base.googleSheets`, typeVersion: 4.5)
```json
{
  "operation": "append",
  "documentId": { "__rl": true, "value": "<SHEET_ID>", "mode": "list" },
  "sheetName": { "__rl": true, "value": "Sheet1", "mode": "list" },
  "columns": {
    "mappingMode": "autoMapInputData"
  }
}
```
Credentials: `"googleSheetsOAuth2Api": { "id": "YOUR_CREDENTIAL_ID", "name": "Google Sheets" }`

---

## Slack Node (`n8n-nodes-base.slack`, typeVersion: 2.2)
```json
{
  "resource": "message",
  "operation": "post",
  "channel": { "__rl": true, "value": "<CHANNEL_ID>", "mode": "id" },
  "text": "={{ $json.message }}"
}
```
Credentials: `"slackOAuth2Api": { "id": "YOUR_CREDENTIAL_ID", "name": "Slack" }`

---

## OpenAI Chat Model (`@n8n/n8n-nodes-langchain.lmChatOpenAi`, typeVersion: 1.2)
```json
{
  "model": "gpt-4o",
  "options": {
    "temperature": 0.3
  }
}
```
Credentials: `"openAiApi": { "id": "YOUR_CREDENTIAL_ID", "name": "OpenAI" }`

---

## AI Agent Node (`@n8n/n8n-nodes-langchain.agent`, typeVersion: 1.7)
```json
{
  "text": "={{ $json.prompt }}",
  "options": {
    "systemMessage": "You are a helpful assistant."
  }
}
```
Connect a Chat Model sub-node via `ai_languageModel` connection type.
