# Claude Code Skills

Production-tested skills for [Claude Code](https://claude.ai/claude-code). Drop into your `.claude/skills/` directory and go.

## Available Skills

| Skill | Description |
|---|---|
| [n8n-builder](n8n-builder/) | Build, deploy, and manage n8n workflows via the REST API. Includes 89 pre-built node snippets, a deploy script, and API rules. |
| [reddit-to-ad-copy](reddit-to-ad-copy/) | Scrape Reddit via Apify, generate ad concepts through a Concept Engine, and write full Native MSL Facebook ad copy. Includes headline and image prompt generation. |

## Installation

1. Copy the skill folder into your project's `.claude/skills/` directory:
   ```bash
   cp -r n8n-builder /path/to/your/project/.claude/skills/
   ```
2. Follow the setup instructions in the skill's README.

## What are Claude Code skills?

Skills are markdown files that teach Claude Code domain-specific knowledge and workflows. When you invoke a skill (e.g., `/n8n-workflow`), Claude loads the skill file and its references, giving it the context to perform specialized tasks without you explaining the details every time.

Each skill in this repo includes:
- **SKILL.md** - the main skill file with frontmatter, loaded by Claude Code
- **references/** - supporting docs, scripts, and templates the skill pulls in as needed

## Contributing

Found a bug or want to add a skill? Open an issue or PR.

## License

MIT
