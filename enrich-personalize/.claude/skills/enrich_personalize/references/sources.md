# Sources & tools

## Firecrawl (REST, no install)
Key lives in the workspace `.env` as `FIRECRAWL_API_KEY` (load it with `set -a; . ./.env; set +a`, or have it exported in your environment). Base `https://api.firecrawl.dev/v2`, auth header `Authorization: Bearer $FIRECRAWL_API_KEY`. Parse responses with `python3 -c`.

- Map a site (find about/team/bio pages): `POST /v2/map` body `{"url":"<domain>"}`
- Scrape a page to markdown: `POST /v2/scrape` body `{"url":"<page>","formats":["markdown"]}`
- Web search with content: `POST /v2/search` body `{"query":"<query>"}`

Use Firecrawl when plain WebFetch returns 403, a JS shell, or truncated text.

## Apify (MCP; token in workspace .env as APIFY_API_TOKEN)
Load via ToolSearch `"select:mcp__apify__call-actor,mcp__apify__fetch-actor-details"`. Call `fetch-actor-details` for the input schema before `call-actor`.

| Actor | id | use |
|---|---|---|
| `compass/crawler-google-places` | `nwua9Gu5YrADL7ZDj` | Google Maps place + reviews; check `ownerResponse` for an owner reply signal |
| `harvestapi/linkedin-profile-posts` | `A3cAPGpwBEG8RJwse` | recent posts by a person (needs their LinkedIn URL); freshest signal when they post |
| `harvestapi/linkedin-company` | `UwSdACBp7ymaGUJjS` | founding year / HQ / size when the site lacks it |
| `apify/website-content-crawler` | `aYG0l9s7dbB7j3gbS` | bulk site crawl alternative to Firecrawl |

Run the waterfall in order and stop at the first strong signal to keep spend down.
