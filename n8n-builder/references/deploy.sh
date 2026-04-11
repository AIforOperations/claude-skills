#!/bin/bash
# deploy.sh — Create, transfer, verify an n8n workflow in one command
# Usage: bash deploy.sh /path/to/workflow.json
#
# Required env vars (or edit the defaults below):
#   N8N_API_KEY    — your n8n API key
#   N8N_BASE_URL   — e.g. https://your-instance.app.n8n.cloud/api/v1
#   N8N_PROJECT_ID — target project ID (optional, skip transfer if empty)

set -e

command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 is required to parse API responses"; exit 1; }

API_KEY="${N8N_API_KEY:?Set N8N_API_KEY env var}"
BASE="${N8N_BASE_URL:?Set N8N_BASE_URL env var}"
PROJECT_ID="${N8N_PROJECT_ID:-}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INDEX_FILE="$SCRIPT_DIR/workflow_index.md"

JSON_FILE="$1"
if [ -z "$JSON_FILE" ]; then
  echo "Usage: bash deploy.sh <workflow.json>"
  exit 1
fi

if [ ! -f "$JSON_FILE" ]; then
  echo "ERROR: File not found: $JSON_FILE"
  exit 1
fi

# 1. Create workflow
echo "Creating workflow..."
RESPONSE=$(curl -s -X POST "$BASE/workflows" \
  -H "X-N8N-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d @"$JSON_FILE")

ID=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])" 2>/dev/null)
NAME=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['name'])" 2>/dev/null)
NODES=$(echo "$RESPONSE" | python3 -c "import sys,json; print(len(json.load(sys.stdin)['nodes']))" 2>/dev/null)

if [ -z "$ID" ]; then
  echo "ERROR: Failed to create workflow"
  echo "$RESPONSE"
  exit 1
fi

echo "Created: $NAME (ID: $ID, $NODES nodes)"

# 2. Transfer to project (if PROJECT_ID is set)
if [ -n "$PROJECT_ID" ]; then
  curl -s -X PUT "$BASE/workflows/$ID/transfer" \
    -H "X-N8N-API-KEY: $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"destinationProjectId\": \"$PROJECT_ID\"}" > /dev/null
  echo "Transferred to project $PROJECT_ID"
fi

# 3. Verify
V_NODES=$(curl -s -X GET "$BASE/workflows/$ID" \
  -H "X-N8N-API-KEY: $API_KEY" | python3 -c "import sys,json; print(len(json.load(sys.stdin)['nodes']))" 2>/dev/null)

echo "Verified: $V_NODES nodes"

# 4. Update workflow index (if index file exists)
if [ -f "$INDEX_FILE" ]; then
  echo "| $NAME | $ID |" >> "$INDEX_FILE"
  echo "Index updated"
fi

echo ""
echo "DONE | $NAME | $ID"
