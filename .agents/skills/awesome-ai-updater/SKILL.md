---
name: awesome-ai-updater
description: Use when updating the Awesome AI Coding Tools repository (README.md), discovering trending AI coding tools, agents, IDEs, MCP servers, or custom agent skills, and applying weekly curated updates.
---

# Awesome AI Coding List Updater

## Overview
Automates discovering, curating, and formatting weekly additions for the **Awesome AI Coding Tools, IDEs & Agents** repository ([README.md](file:///home/xuf/apps/my-awesome-ai/README.md)). Combines fast GitHub API candidate discovery with human-grade editorial curation.

## When to Use
- User asks to perform a weekly update to the repository.
- Discovering latest trending AI coding tools, CLI agents, IDEs, MCP servers, or agent skills.
- Adding newly discovered repositories to [README.md](file:///home/xuf/apps/my-awesome-ai/README.md) while maintaining strict table schemas and alphabetical ordering.

When **NOT** to use:
- Updating general non-AI repositories or non-developer software lists.
- One-off single repo edits that don't need discovery or changelog updates.

## Quick Reference Commands

| Action | Command | Purpose |
| :--- | :--- | :--- |
| **Discover Candidates** | `python3 fix.py --discover` | Scans GitHub searches, stars, and topics for new AI coding tools |
| **Output Candidates JSON** | `python3 fix.py --discover --json` | Machine-readable candidate list with stars & descriptions |
| **Apply Vetted Additions** | `python3 fix.py --apply-file vetted.json` | Inserts rows into tables alphabetically & updates changelog |
| **Verify Markdown Diff** | `git diff README.md` | Validates formatting, alphabetical ordering, and column schemas |

## Curation & Update Workflow

### Step 1: Discover Candidates
Run the discovery command in the repository workspace:
```bash
python3 fix.py --discover
```
This queries GitHub via authenticated `gh` CLI across user stars, trending topics, and key AI coding queries, excluding repositories already listed in [README.md](file:///home/xuf/apps/my-awesome-ai/README.md).

### Step 2: Editorial Screening (Scope Filtering)
Only select projects matching the repository's core focus:
- **IN SCOPE:** AI coding agents, autonomous SWE systems, AI-native IDEs, code generation extensions, agent skills/plugins, AI gateways/firewalls, MCP servers, inference engines, vector databases, vibe coding tools, developer-focused LLM devtools.
- **OUT OF SCOPE:** Generic consumer chatbots, speech/voice clones without coding hooks, phone utilities, games, and math/animation libraries.

### Step 3: Classification & Schema Mapping
Map each selected candidate to exactly one of the 12 sections:

| Category Key | README Section Header | 4th Column Schema |
| :--- | :--- | :--- |
| `CLI Agents` | `## 🤖 AI Coding CLI Agents & SWE Systems` | `Key Features` |
| `IDEs` | `## 💻 AI-Native IDEs & Cloud Workspaces` | `Key Features` |
| `Extensions` | `## 🧩 AI Coding Extensions & Plugins` | `Description / Key Features` (Col 2 is Platform Support) |
| `Skills` | `## 🔌 Custom Agent Skills & Plugins` | `Target Agent / Platform` (e.g. `Claude Code / Codex / Gemini CLI`) |
| `Gateways` | `## 🛡️ AI Gateways, Proxies & Agent Security` | `Key Features` |
| `Frameworks` | `## ⚙️ AI Agent Frameworks & Multi-Agent Platforms` | `Key Features` |
| `DevTools` | `## 🛠️ LLM DevTools & Orchestration Infrastructure` | `Key Features` |
| `MCP` | `## 📡 Model Context Protocol (MCP) Servers` | `Tools / Access Exposed` |
| `Inference` | `## ⚡ LLM Inference & Local Serving Engines` | `Key Features` |
| `VectorDB` | `## 🗄️ Vector Databases & Vector Stores` | `Key Features` |
| `Vibe` | `## 🎨 Vibe Coding & Generative UI Tools` | `Key Features` |
| `Learning` | `## 📖 AI Learning & Educational Resources` | `Key Features` |

### Step 4: Maturity Ratings
Assign badges based on stars:
- 🟢 **Stable**: > 1,000 stars
- 🟡 **Active Development**: 500 – 1,000 stars
- 🔴 **Experimental**: < 500 stars

### Step 5: Apply Vetted Additions
Create a JSON file with selected, vetted entries:
```json
[
  {
    "full_name": "owner/repo",
    "name": "ToolName",
    "owner": "owner",
    "stars": 12500,
    "description": "Clear, concise description without boilerplate.",
    "category": "Skills",
    "target": "Claude Code / General Agents"
  }
]
```
Apply to [README.md](file:///home/xuf/apps/my-awesome-ai/README.md):
```bash
python3 fix.py --apply-file vetted.json
```
The script will:
1. Prepend today's `### YYYY-MM-DD — Weekly Update` block to `## 📋 Changelog`.
2. Insert each row into its target table in strictly alphabetical order.
3. Apply the correct 4th column header for the category.

### Step 6: Verify
Always run:
```bash
git diff README.md
```
Confirm:
- No duplicate entries.
- Changelog contains all added entries with correct category names.
- Table columns are aligned and properly closed.

## Common Mistakes & Rationalizations

| Excuse / Mistake | Reality |
| :--- | :--- |
| "Dumping raw discovery into README without screening" | Discovers non-coding tools (e.g. audio apps, games). Always screen candidates. |
| "Using placeholder text for key features" | Never leave `key_feature_placeholder` or generic filler. Write 3-4 accurate highlights. |
| "Assuming all tables have the same 4 columns" | Skills uses `Target Agent / Platform`; MCP uses `Tools / Access Exposed`; Extensions has `Platform Support`. |
| "Appending rows to the bottom of the table" | Tables must remain sorted alphabetically by tool name. |

## Red Flags — STOP and Verify
- Any table row containing `key_feature_placeholder`.
- Missing or misdated entry in `## 📋 Changelog`.
- Broken markdown links or malformed table pipes.
