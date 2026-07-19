# Awesome AI Coding Tools, IDEs & Agents 🚀

A curated, comprehensive list of awesome AI coding tools, autonomous agents, AI-native IDEs, extensions, LLM orchestrators, inference engines, vector databases, MCP servers, custom agent skills, security proxies, and educational resources.

### 🏷️ Maturity Rating Legend
* 🟢 **Stable / Production-Ready**: Established, highly stable tools with low bug rates and robust production suitability.
* 🟡 **Active Development**: Fully functional tools undergoing rapid iterations. Expect frequent feature updates.
* 🔴 **Experimental / Beta**: Early-stage prototypes, proofs-of-concept, or bleeding-edge releases. High potential but unstable.


---

## 📋 Changelog

### 2026-07-19 — Weekly Update
**Added:**
- [TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) → LLM DevTools
- [SkillOpt](https://github.com/microsoft/SkillOpt) → Custom Agent Skills
- [LMCache](https://github.com/LMCache/LMCache) → LLM Inference Engines
- [ECC](https://github.com/affaan-m/ECC) → AI Agent Frameworks
- [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) → AI Agent Frameworks
- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) → AI Learning
- [openwiki](https://github.com/langchain-ai/openwiki) → LLM DevTools
- [awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026) → AI Learning
- [500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) → AI Learning
- [my-opencode-config](https://github.com/youxufkhan/my-opencode-config) → AI Coding CLI Agents
- [nimbench](https://github.com/youxufkhan/nimbench) → LLM DevTools
- [lancedb](https://github.com/lancedb/lancedb) → Vector Databases
- [ragflow](https://github.com/infiniflow/ragflow) → LLM DevTools
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) → MCP Servers
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) → AI Learning
- [awesome-llm-tools](https://github.com/sam-blackfly/awesome-llm-tools) → AI Learning
- [bolt.diy](https://github.com/stackblitz-labs/bolt.diy) → Vibe Coding
- [SWE-agent](https://github.com/swe-agent/swe-agent) → AI Coding CLI Agents
- [mastra](https://github.com/mastra-ai/mastra) → AI Agent Frameworks
- [pydantic-ai](https://github.com/pydantic/pydantic-ai) → AI Agent Frameworks
- [firecrawl](https://github.com/mendableai/firecrawl) → LLM DevTools
- [langflow](https://github.com/langflow-ai/langflow) → LLM DevTools
- [autogen](https://github.com/microsoft/autogen) → AI Agent Frameworks
- [open-webui](https://github.com/open-webui/open-webui) → Vibe Coding


### 2026-07-12 — Weekly Update
**Added:**
- [AI Job Search](https://github.com/MadsLorentzen/ai-job-search) → AI Coding CLI Agents & SWE Systems
- [Claude Code Templates](https://github.com/davila7/claude-code-templates) → AI Coding CLI Agents & SWE Systems
- [Terax AI](https://github.com/crynta/terax-ai) → AI-Native IDEs & Cloud Workspaces
- [CodexBar](https://github.com/steipete/CodexBar) → AI Coding Extensions & Plugins
- [Archify](https://github.com/tt-a1i/archify) → Custom Agent Skills & Plugins
- [Claude HUD](https://github.com/jarrodwatts/claude-hud) → Custom Agent Skills & Plugins
- [Claude Mem](https://github.com/thedotmack/claude-mem) → Custom Agent Skills & Plugins
- [Stitch Skills](https://github.com/google-labs-code/stitch-skills) → Custom Agent Skills & Plugins
- [Claude Video](https://github.com/bradautomates/claude-video) → LLM DevTools & Orchestration Infrastructure
- [Crawl4AI](https://github.com/unclecode/crawl4ai) → LLM DevTools & Orchestration Infrastructure
- [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) → LLM DevTools & Orchestration Infrastructure
- [olmOCR](https://github.com/allenai/olmocr) → LLM DevTools & Orchestration Infrastructure
- [Video Use](https://github.com/browser-use/video-use) → LLM DevTools & Orchestration Infrastructure
- [Desktop Commander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) → Model Context Protocol (MCP) Servers
- [Meetily](https://github.com/Zackriya-Solutions/meetily) → Vibe Coding & Generative UI Tools

---

## 📂 Table of Contents
- [📋 Changelog](#-changelog)
- [🤖 AI Coding CLI Agents & SWE Systems](#-ai-coding-cli-agents--swe-systems)
- [💻 AI-Native IDEs & Cloud Workspaces](#-ai-native-ides--cloud-workspaces)
- [🧩 AI Coding Extensions & Plugins](#-ai-coding-extensions--plugins)
- [🔌 Custom Agent Skills & Plugins](#-custom-agent-skills--plugins)
- [🛡️ PII Masking & AI Agent Security Proxies](#️-pii-masking--ai-agent-security-proxies)
- [⚙️ AI Agent Frameworks & Multi-Agent Platforms](#️-ai-agent-frameworks--multi-agent-platforms)
- [🛠️ LLM DevTools & Orchestration Infrastructure](#️-llm-devtools--orchestration-infrastructure)
- [📡 Model Context Protocol (MCP) Servers](#-model-context-protocol-mcp-servers)
- [⚡ LLM Inference & Local Serving Engines](#-llm-inference--local-serving-engines)
- [🗄️ Vector Databases & Vector Stores](#️-vector-databases--vector-stores)
- [🎨 Vibe Coding & Generative UI Tools](#-vibe-coding--generative-ui-tools)
- [📖 AI Learning & Educational Resources](#-ai-learning--educational-resources)
- [📊 Quick Comparison Matrix](#-quick-comparison-matrix)
- [🤝 Contributing](#-contributing)

---

## 🤖 AI Coding CLI Agents & SWE Systems
Autonomous CLI-first software engineering agents that can write code, run commands, execute tests, manage git changes, and solve issues.

| Repository / Agent | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[AI Job Search](https://github.com/MadsLorentzen/ai-job-search)** <br> [![Stars](https://img.shields.io/github/stars/MadsLorentzen/ai-job-search?style=flat-square&label=%E2%98%85)](https://github.com/MadsLorentzen/ai-job-search) | Mads Lorentzen | AI-powered job application framework built on Claude Code. | Evaluate postings, tailor CVs, write cover letters, prep interviews |
| 🟢 **[Aider](https://github.com/aider-chat/aider)** <br> [![Stars](https://img.shields.io/github/stars/aider-chat/aider?style=flat-square&label=%E2%98%85)](https://github.com/aider-chat/aider) | Aider-chat | Git-integrated terminal pair programmer. | Edits files in-place, writes automatic git commits, works with local/remote LLMs. |
| 🟢 **[Antigravity CLI](https://antigravity.google)** | Google DeepMind | Advanced agentic CLI pair programmer. | Parallel subagent orchestration, sandboxed browser testing, deep git integration. |
| 🟡 **[cc-switch](https://github.com/farion1231/cc-switch)** <br> [![Stars](https://img.shields.io/github/stars/farion1231/cc-switch?style=flat-square&label=%E2%98%85)](https://github.com/farion1231/cc-switch) | farion1231 | Cross-platform desktop All-in-One assistant manager for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes. | Desktop wrapper, multi-agent provider switching, WSL support. |
| 🟡 **[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code)** | Anthropic | Command-line agent powered by Claude models. | 1M+ token context window, deep reasoning, multi-file code workspace editing. |
| 🟢 **[Claude Code Templates](https://github.com/davila7/claude-code-templates)** <br> [![Stars](https://img.shields.io/github/stars/davila7/claude-code-templates?style=flat-square&label=%E2%98%85)](https://github.com/davila7/claude-code-templates) | davila7 | CLI tool for configuring and monitoring Claude Code. | Template configurations, active monitoring, context metrics |
| 🔴 **[Claw Code Example](https://github.com/ultraworkers/claw-code)** <br> [![Stars](https://img.shields.io/github/stars/ultraworkers/claw-code?style=flat-square&label=%E2%98%85)](https://github.com/ultraworkers/claw-code) | Ultraworkers | Rust-based repository managed automatically by agentic code. | Demonstrates zero human intervention maintenance, autonomous documentation. |
| 🟡 **[codex-profiles](https://github.com/Ducksss/codex-profiles)** <br> [![Stars](https://img.shields.io/github/stars/Ducksss/codex-profiles?style=flat-square&label=%E2%98%85)](https://github.com/Ducksss/codex-profiles) | Ducksss | Bash CLI for launching Codex CLI and Desktop with isolated CODEX_HOME profiles. | Separate accounts, config, sessions, plugins, caches, and logs without copying auth.json tokens. |
| 🟡 **[DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)** <br> [![Stars](https://img.shields.io/github/stars/esengine/DeepSeek-Reasonix?style=flat-square&label=%E2%98%85)](https://github.com/esengine/DeepSeek-Reasonix) | esengine | DeepSeek-native terminal coding agent. | Engineered around prefix-cache stability, low input-token overhead. |
| 🟡 **[Devika](https://github.com/mufeedvh/devika)** <br> [![Stars](https://img.shields.io/github/stars/mufeedvh/devika?style=flat-square&label=%E2%98%85)](https://github.com/mufeedvh/devika) | Mufeed VH | Open-source clone of Cognition's Devin. | Plan-execute-monitor coding loops, agentic browser search. |
| 🟡 **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** <br> [![Stars](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=flat-square&label=%E2%98%85)](https://github.com/google-gemini/gemini-cli) | Google Gemini | An open-source, terminal-first AI agent powered by Gemini. | ReAct loops, MCP server compatibility, Google Search grounding, git workflows. |
| 🟡 **[Goose](https://github.com/aaif-goose/goose)** <br> [![Stars](https://img.shields.io/github/stars/aaif-goose/goose?style=flat-square&label=%E2%98%85)](https://github.com/aaif-goose/goose) | Agentic AI Foundation (AAIF) | Extensible open-source coding agent. | Local or desktop run modes, built-in MCP client, custom developer plugins. |
| 🟡 **[my-opencode-config](https://github.com/youxufkhan/my-opencode-config)** <br> [![Stars](https://img.shields.io/github/stars/youxufkhan/my-opencode-config?style=flat-square&label=%E2%98%85)](https://github.com/youxufkhan/my-opencode-config) | youxufkhan | CLI tool to auto-configure OpenCode with free AI models. | Automated, open-source |
| 🟢 **[SWE-agent](https://github.com/swe-agent/swe-agent)** <br> [![Stars](https://img.shields.io/github/stars/swe-agent/swe-agent?style=flat-square&label=%E2%98%85)](https://github.com/swe-agent/swe-agent) | swe-agent | SWE-agent takes a GitHub issue and tries to automatically fix it. | Automated, open-source |

---

## 💻 AI-Native IDEs & Cloud Workspaces
Integrated Development Environments (IDEs) built with AI agents at the center of the coding experience.

| Editor / Workspace | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[Cherry Studio](https://github.com/CherryHQ/cherry-studio)** <br> [![Stars](https://img.shields.io/github/stars/CherryHQ/cherry-studio?style=flat-square&label=%E2%98%85)](https://github.com/CherryHQ/cherry-studio) | CherryHQ | AI productivity studio with smart chat, autonomous agents, and 300+ assistants. | Unified access to frontier LLMs, multiple assistant panels, offline capabilities. |
| 🟡 **[ClawX](https://github.com/ValueCell-ai/ClawX)** <br> [![Stars](https://img.shields.io/github/stars/ValueCell-ai/ClawX?style=flat-square&label=%E2%98%85)](https://github.com/ValueCell-ai/ClawX) | ValueCell-ai | Graphical desktop interface for OpenClaw AI agents. | Visual agent configuration, no-code execution controls, local execution logs. |
| 🟢 **[Cursor](https://www.cursor.com/)** | Anysphere | Leading VS Code fork with deep AI integration. | "Composer" multi-file agent, autocomplete, inline codebase chat, custom index. |
| 🟢 **[GitHub Copilot Workspace](https://github.com/features/copilot/workspace)** | GitHub / Microsoft | Task-centric cloud workspace. | Interactive issue plans, automated task lists, instant sandbox edits. |
| 🟡 **[Melty](https://github.com/melty-labs/melty)** <br> [![Stars](https://img.shields.io/github/stars/melty-labs/melty?style=flat-square&label=%E2%98%85)](https://github.com/melty-labs/melty) | Melty Labs | Open-source IDE that learns from developers. | Tracks git actions, code pattern indexing, smart autocompletion. |
| 🟡 **[Orca](https://github.com/stablyai/orca)** <br> [![Stars](https://img.shields.io/github/stars/stablyai/orca?style=flat-square&label=%E2%98%85)](https://github.com/stablyai/orca) | stablyai | Desktop and mobile ADE (Agent Development Environment). | Run fleets of parallel coding agents, multi-agent TUI, support for custom models. |
| 🟢 **[Project IDX](https://idx.dev/)** | Google | Cloud-based developer workspace. | Multiplatform templates, integrated Gemini chat, device emulators. |
| 🟢 **[Replit Agent](https://replit.com)** | Replit | Browser-based full-stack developer agent. | App creation, instant DB setup, one-click deployments. |
| 🟢 **[Terax AI](https://github.com/crynta/terax-ai)** <br> [![Stars](https://img.shields.io/github/stars/crynta/terax-ai?style=flat-square&label=%E2%98%85)](https://github.com/crynta/terax-ai) | crynta | Lightweight, terminal-first AI-native developer workspace. | Terminal-first design, local execution, multi-model compatibility |
| 🟢 **[Windsurf](https://codeium.com/windsurf)** | Codeium | Agent-first IDE based on VS Code. | "Windsurf Flow" collaborative loops, fast indexing, persistent codebase context. |
| 🟢 **[Zed AI](https://zed.dev/ai)** | Zed Decent | High-performance, collaborative rust-based IDE. | Multi-buffer editing, instant startup, inline LLM chats (OpenAI/Anthropic). |

---

## 🧩 AI Coding Extensions & Plugins
Augmentative extensions to supercharge traditional IDEs (VS Code, JetBrains, Neovim).

| Extension | Platform Support | Creator | Description / Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[Amazon Q Developer](https://aws.amazon.com/q/developer/)** | VS Code, JetBrains | AWS | Autocomplete, security scans, legacy code translation, AWS cloud integrations. |
| 🟢 **[Bito](https://bito.ai/)** | VS Code, JetBrains | Bito | AI helper for unit test generation, security checking, and explaining code. |
| 🟢 **[Cline](https://github.com/cline/cline)** <br> [![Stars](https://img.shields.io/github/stars/cline/cline?style=flat-square&label=%E2%98%85)](https://github.com/cline/cline) | VS Code | Cline | Open-source agent interface. Reads/writes files and runs terminal commands via MCP. |
| 🟢 **[Codeium](https://codeium.com/)** | VS Code, JetBrains, Xcode, Neovim | Codeium | Free autocomplete, chat, semantic search, local index building. |
| 🟢 **[CodexBar](https://github.com/steipete/CodexBar)** <br> [![Stars](https://img.shields.io/github/stars/steipete/CodexBar?style=flat-square&label=%E2%98%85)](https://github.com/steipete/CodexBar) | Peter Steinberger | Menu bar assistant showing usage statistics for OpenAI Codex and Claude Code. | Usage statistics, offline monitoring, status bar access |
| 🟢 **[Cody](https://sourcegraph.com/cody)** | VS Code, JetBrains, Neovim | Sourcegraph | Advanced semantic codebase search, code explanation, chat-with-docs. |
| 🟢 **[Continue](https://github.com/continuedev/continue)** <br> [![Stars](https://img.shields.io/github/stars/continuedev/continue?style=flat-square&label=%E2%98%85)](https://github.com/continuedev/continue) | VS Code, JetBrains | Continue | Open-source, model-agnostic extension. Connects to Ollama (local) or API keys. |
| 🟢 **[Double.bot](https://www.double.bot/)** | VS Code, JetBrains | Double | High-accuracy inline editing, codebase context parsing. |
| 🟢 **[GitHub Copilot](https://github.com/features/copilot)** | VS Code, JetBrains, Visual Studio, Neovim | GitHub | Fast autocomplete, chat panels, codebase indexing, PR description generator. |
| 🟢 **[Roo Code](https://github.com/RooVetGit/Roo-Code)** <br> [![Stars](https://img.shields.io/github/stars/RooVetGit/Roo-Code?style=flat-square&label=%E2%98%85)](https://github.com/RooVetGit/Roo-Code) | VS Code | Roo Vet | Cline fork with specialized agent modes, prompt overrides, and MCP diagnostics. |
| 🟢 **[Supermaven](https://supermaven.com/)** | VS Code, JetBrains, Neovim | Supermaven | Ultra-low latency autocomplete, large 300,000 token context window. |
| 🟢 **[Tabnine](https://www.tabnine.com/)** | VS Code, JetBrains, Eclipse | Tabnine | Secure autocomplete with local offline models or private cloud deployments. |

---

## 🔌 Custom Agent Skills & Plugins
Reusable, structured skills and behavior overrides designed to teach coding agents (like Claude Code, Gemini CLI, Cline) how to interact with external tools and follow specific protocols.

| Skill / Plugin Repo | Creator | Description | Target Agent / Platform |
| :--- | :--- | :--- | :--- |
| 🟡 **[Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)** <br> [![Stars](https://img.shields.io/github/stars/Imbad0202/academic-research-skills?style=flat-square&label=%E2%98%85)](https://github.com/Imbad0202/academic-research-skills) | Imbad0202 | Workflows for research, compilation, drafting, and reviewing papers. | Claude Code / General Agents |
| 🟢 **[Agent Skills](https://github.com/addyosmani/agent-skills)** <br> [![Stars](https://img.shields.io/github/stars/addyosmani/agent-skills?style=flat-square&label=%E2%98%85)](https://github.com/addyosmani/agent-skills) | Addy Osmani | Production-grade software engineering skills. | Generic / Claude Code, Gemini CLI |
| 🟡 **[Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills)** <br> [![Stars](https://img.shields.io/github/stars/multica-ai/andrej-karpathy-skills?style=flat-square&label=%E2%98%85)](https://github.com/multica-ai/andrej-karpathy-skills) | Multica AI | Claude Code behaviors derived from Karpathy's LLM coding pitfall observations. | Claude Code / CLAUDE.md |
| 🟢 **[Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** <br> [![Stars](https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square&label=%E2%98%85)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | mukul975 | 817 structured cybersecurity skills for AI agents mapped to MITRE, NIST frameworks. | Claude Code / General Agents |
| 🟢 **[Archify](https://github.com/tt-a1i/archify)** <br> [![Stars](https://img.shields.io/github/stars/tt-a1i/archify?style=flat-square&label=%E2%98%85)](https://github.com/tt-a1i/archify) | tt-a1i | Agent skill to generate architecture diagrams with theme toggle and PNG/SVG export. | Diagram generation, dark/light theme, vector exports |
| 🟢 **[Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)** <br> [![Stars](https://img.shields.io/github/stars/ComposioHQ/awesome-claude-skills?style=flat-square&label=%E2%98%85)](https://github.com/ComposioHQ/awesome-claude-skills) | ComposioHQ | Curated list of awesome Claude Skills, resources, and tools. | Claude Code / General Agents |
| 🔴 **[Caveman](https://github.com/JuliusBrussee/caveman)** <br> [![Stars](https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat-square&label=%E2%98%85)](https://github.com/JuliusBrussee/caveman) | Julius Brussee | Token-saving skill that rewrites instructions into caveman talk. | Claude Code / General Agents |
| 🟢 **[Claude HUD](https://github.com/jarrodwatts/claude-hud)** <br> [![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-hud?style=flat-square&label=%E2%98%85)](https://github.com/jarrodwatts/claude-hud) | Jarrod Watts | Claude Code plugin displaying context usage, active tools, running agents, and task progress. | HUD visualization, active tool tracking, task progress monitoring |
| 🟢 **[Claude Mem](https://github.com/thedotmack/claude-mem)** <br> [![Stars](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square&label=%E2%98%85)](https://github.com/thedotmack/claude-mem) | thedotmack | Persistent SQLite-based context and memory system for Claude Code and other agents. | Context persistence, AI-driven compression, multi-agent support |
| 🔴 **[ClawHub](https://github.com/openclaw/clawhub)** <br> [![Stars](https://img.shields.io/github/stars/openclaw/clawhub?style=flat-square&label=%E2%98%85)](https://github.com/openclaw/clawhub) | OpenClaw | Skill and plugin registry for OpenClaw agents. | OpenClaw |
| 🟡 **[Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin)** <br> [![Stars](https://img.shields.io/github/stars/EveryInc/compound-engineering-plugin?style=flat-square&label=%E2%98%85)](https://github.com/EveryInc/compound-engineering-plugin) | EveryInc | Code optimization and refactoring agent plugin. | Standardized helper workflows for Claude Code, Codex, and Cursor. |
| 🟡 **[Council of High Intelligence](https://github.com/0xNyk/council-of-high-intelligence)** <br> [![Stars](https://img.shields.io/github/stars/0xNyk/council-of-high-intelligence?style=flat-square&label=%E2%98%85)](https://github.com/0xNyk/council-of-high-intelligence) | 0xNyk | Deliberation engine with 18 AI personas. | Claude Code / General Agent skill for structured multi-round deliberation and verdicts. |
| 🟡 **[DESIGN.md](https://github.com/google-labs-code/design.md)** <br> [![Stars](https://img.shields.io/github/stars/google-labs-code/design.md?style=flat-square&label=%E2%98%85)](https://github.com/google-labs-code/design.md) | google-labs-code | Format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system. | Generic / Coding Agents |
| 🔴 **[Graphify](https://github.com/safishamsi/graphify)** <br> [![Stars](https://img.shields.io/github/stars/safishamsi/graphify?style=flat-square&label=%E2%98%85)](https://github.com/safishamsi/graphify) | safishamsi | Turn code, schemas, scripts, docs, and media into queryable knowledge graphs. | Claude Code / Codex / Gemini CLI / Cursor |
| 🟡 **[gstack](https://github.com/garrytan/gstack)** <br> [![Stars](https://img.shields.io/github/stars/garrytan/gstack?style=flat-square&label=%E2%98%85)](https://github.com/garrytan/gstack) | Garry Tan | Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Doc Engineer, and QA. | Claude Code / CLAUDE.md |
| 🟡 **[Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill)** <br> [![Stars](https://img.shields.io/github/stars/op7418/guizang-ppt-skill?style=flat-square&label=%E2%98%85)](https://github.com/op7418/guizang-ppt-skill) | op7418 | AI-agent Skill for generating polished HTML slide decks with Swiss layouts. | Claude Code / Codex / General Agents |
| 🟢 **[jscpd](https://github.com/kucherenko/jscpd)** <br> [![Stars](https://img.shields.io/github/stars/kucherenko/jscpd?style=flat-square&label=%E2%98%85)](https://github.com/kucherenko/jscpd) | Andrey Kucherenko | Copy/paste detector for programming source code, AI-ready with token-efficient reporter and skill. | Generic / Coding Agents |
| 🔴 **[Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill)** <br> [![Stars](https://img.shields.io/github/stars/mvanhorn/last30days-skill?style=flat-square&label=%E2%98%85)](https://github.com/mvanhorn/last30days-skill) | M. Van Horn | Scrapes and synthesizes web/forum summaries. | Claude Code / Generic Agents |
| 🟡 **[Matt Pocock Skills](https://github.com/mattpocock/skills)** <br> [![Stars](https://img.shields.io/github/stars/mattpocock/skills?style=flat-square&label=%E2%98%85)](https://github.com/mattpocock/skills) | Matt Pocock | Opinionated TypeScript/Web developer agent skills. | Exposes specialized workflows and commands from a `.claude` directory. |
| 🟡 **[Obsidian Skills](https://github.com/kepano/obsidian-skills)** <br> [![Stars](https://img.shields.io/github/stars/kepano/obsidian-skills?style=flat-square&label=%E2%98%85)](https://github.com/kepano/obsidian-skills) | Kepano | Teaches agents to read Markdown, Bases, and JSON Canvas in Obsidian. | Obsidian / Generic Agents |
| 🟡 **[OpenSpec](https://github.com/Fission-AI/OpenSpec)** <br> [![Stars](https://img.shields.io/github/stars/Fission-AI/OpenSpec?style=flat-square&label=%E2%98%85)](https://github.com/Fission-AI/OpenSpec) | Fission-AI | Spec-driven development framework. | Formal specifications and test cases designed for AI pair programmers. |
| 🟡 **[React Doctor](https://github.com/millionco/react-doctor)** <br> [![Stars](https://img.shields.io/github/stars/millionco/react-doctor?style=flat-square&label=%E2%98%85)](https://github.com/millionco/react-doctor) | Million.co | Catch and fix bad React code generated by AI agents. | Generic / Code Review Agents |
| 🟢 **[SkillOpt](https://github.com/microsoft/SkillOpt)** <br> [![Stars](https://img.shields.io/github/stars/microsoft/SkillOpt?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/SkillOpt) | microsoft | SkillOpt is a text-space optimizer that trains reusable natural-language skills. | Automated, open-source |
| 🟢 **[Stitch Skills](https://github.com/google-labs-code/stitch-skills)** <br> [![Stars](https://img.shields.io/github/stars/google-labs-code/stitch-skills?style=flat-square&label=%E2%98%85)](https://github.com/google-labs-code/stitch-skills) | Google Labs | Library of agent skills designed to work with the Stitch MCP server. | Open skills standard, multi-agent compatibility, tool bindings |
| 🟡 **[stop-slop](https://github.com/hardikpandya/stop-slop)** <br> [![Stars](https://img.shields.io/github/stars/hardikpandya/stop-slop?style=flat-square&label=%E2%98%85)](https://github.com/hardikpandya/stop-slop) | hardikpandya | AI writing mitigation skill. | Strips predictable AI phrases and cliches from generated documentation and text. |
| 🟡 **[Superpowers](https://github.com/obra/superpowers)** <br> [![Stars](https://img.shields.io/github/stars/obra/superpowers?style=flat-square&label=%E2%98%85)](https://github.com/obra/superpowers) | Obra | An agentic skills framework & software development methodology that works. | Generic / Claude Code, Gemini CLI |
| 🔴 **[Taste-Skill](https://github.com/Leonxlnx/taste-skill)** <br> [![Stars](https://img.shields.io/github/stars/Leonxlnx/taste-skill?style=flat-square&label=%E2%98%85)](https://github.com/Leonxlnx/taste-skill) | Leonxlnx | Taste-Skill - gives your AI good taste, stopping boring and generic layout generation. | Claude Code / Codex |

---

## 🛡️ AI Gateways, Proxies & Agent Security
Middlewares, security gatekeepers, and routing gateways that manage LLM traffic, load balance queries, track costs, and redact secrets or PII.

| Tool / Proxy | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟡 **[9router](https://github.com/decolua/9router)** <br> [![Stars](https://img.shields.io/github/stars/decolua/9router?style=flat-square&label=%E2%98%85)](https://github.com/decolua/9router) | Decolua | Local proxy and router for AI tools. | Connects CLI agents to 40+ providers, automatic fallbacks, token compression. |
| 🔴 **[Clawshield](https://github.com/SleuthCo/clawshield-public)** <br> [![Stars](https://img.shields.io/github/stars/SleuthCo/clawshield-public?style=flat-square&label=%E2%98%85)](https://github.com/SleuthCo/clawshield-public) | SleuthCo | YAML-driven security gateway for dev agents. | Enforces prompt policies, logs outputs, filters outbound credentials. |
| 🟢 **[CodeGate](https://github.com/stacklok/codegate)** <br> [![Stars](https://img.shields.io/github/stars/stacklok/codegate?style=flat-square&label=%E2%98%85)](https://github.com/stacklok/codegate) | Stacklok | Privacy-first local proxy for IDE extensions/CLIs. | Detects/masks PII and API keys, warns of vulnerable packages, local decryption. |
| 🟢 **[FreeLLMAPI](https://github.com/tashfeenahmed/freellmapi)** <br> [![Stars](https://img.shields.io/github/stars/tashfeenahmed/freellmapi?style=flat-square&label=%E2%98%85)](https://github.com/tashfeenahmed/freellmapi) | tashfeenahmed | Aggregated LLM proxy for free tiers. | Combines 16+ provider free tiers into one OpenAI-compatible endpoint with automatic failover. |
| 🔴 **[Kiji Proxy](https://github.com/dataiku/kiji-proxy)** <br> [![Stars](https://img.shields.io/github/stars/dataiku/kiji-proxy?style=flat-square&label=%E2%98%85)](https://github.com/dataiku/kiji-proxy) | Dataiku | Lightweight PII masking proxy. | Regular expression and NLP-based token masking. |
| 🟢 **[LiteLLM](https://github.com/BerriAI/litellm)** <br> [![Stars](https://img.shields.io/github/stars/BerriAI/litellm?style=flat-square&label=%E2%98%85)](https://github.com/BerriAI/litellm) | BerriAI | Call 100+ LLM APIs using the OpenAI format. Proxy server for load balancing, cost tracking, and fallbacks. | Load balancer, budget manager, billing tracking, fallback routing. |
| 🟡 **[no-mistakes](https://github.com/kunchenguid/no-mistakes)** <br> [![Stars](https://img.shields.io/github/stars/kunchenguid/no-mistakes?style=flat-square&label=%E2%98%85)](https://github.com/kunchenguid/no-mistakes) | kunchenguid | AI code push gateway and quality gate. | Runs tests/linting on temporary worktrees before forwarding pushes and opening PRs. |
| 🟡 **[OmniRoute](https://github.com/diegosouzapw/OmniRoute)** <br> [![Stars](https://img.shields.io/github/stars/diegosouzapw/OmniRoute?style=flat-square&label=%E2%98%85)](https://github.com/diegosouzapw/OmniRoute) | diegosouzapw | AI gateway supporting smart routing, load balancing, retries, and fallback mechanisms for multi-provider LLMs. | OpenAI-compatible endpoint, retries, multi-provider fallbacks. |
| 🟢 **[One API](https://github.com/songquanpeng/one-api)** <br> [![Stars](https://img.shields.io/github/stars/songquanpeng/one-api?style=flat-square&label=%E2%98%85)](https://github.com/songquanpeng/one-api) | songquanpeng | Multi-provider LLM API key management, distribution, and billing proxy system. | OpenAI API format wrapper, multi-user quotas, custom billing. |
| 🟢 **[Portkey AI Gateway](https://github.com/Portkey-AI/gateway)** <br> [![Stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=flat-square&label=%E2%98%85)](https://github.com/Portkey-AI/gateway) | Portkey-AI | High-performance, open-source AI gateway to route, load-balance, cache, and monitor LLM queries. | 50+ LLM integrations, fast routing, caching, observability. |
| 🟢 **[RouteLLM](https://github.com/lm-sys/RouteLLM)** <br> [![Stars](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&label=%E2%98%85)](https://github.com/lm-sys/RouteLLM) | lm-sys | Open-source framework for cost-saving LLM routing, sending simpler queries to smaller models and complex queries to larger ones. | Cost optimization, router training and evaluation, BERT-based routing models. |
| 🟡 **[Strix](https://github.com/usestrix/strix)** <br> [![Stars](https://img.shields.io/github/stars/usestrix/strix?style=flat-square&label=%E2%98%85)](https://github.com/usestrix/strix) | usestrix | AI-powered penetration testing security tool. | Finds, tests, and auto-patches security vulnerabilities within agentic CI pipelines. |
| 🟢 **[WitnessAI](https://witness.ai)** | WitnessAI | Enterprise-grade AI proxy firewall. | Granular policy configurations, real-time agent auditing, schema obscuring. |

---

## ⚙️ AI Agent Frameworks & Multi-Agent Platforms
Orchestration frameworks that allow developers to design, wire, and deploy complex autonomous agent teams.

| Framework | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟡 **[Agency Agents](https://github.com/msitarzewski/agency-agents)** <br> [![Stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=flat-square&label=%E2%98%85)](https://github.com/msitarzewski/agency-agents) | msitarzewski | Specialized expert agent pack for creative agencies. | Social media bots, copy editors, UX reviewers, community monitors. |
| 🔴 **[AgentBBS](https://github.com/ruvnet/AgentBBS)** <br> [![Stars](https://img.shields.io/github/stars/ruvnet/AgentBBS?style=flat-square&label=%E2%98%85)](https://github.com/ruvnet/AgentBBS) | ruvnet | Multiplayer agent arena and BBS workspace. | Human-agent multiplayer board, MCP and SSH access interfaces, arena benchmarking. |
| 🟢 **[Agno](https://github.com/agno-agi/agno)** <br> [![Stars](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&label=%E2%98%85)](https://github.com/agno-agi/agno) | Agno AI | Open-source framework for building multi-modal agents. | Fast execution, built-in vector integrations, multi-modal support. |
| 🔴 **[AI Berkshire](https://github.com/xbtlin/ai-berkshire)** <br> [![Stars](https://img.shields.io/github/stars/xbtlin/ai-berkshire?style=flat-square&label=%E2%98%85)](https://github.com/xbtlin/ai-berkshire) | xbtlin | A value investing research framework built on Claude Code using multi-agent adversarial analysis. | Python / Claude Code |
| 🟡 **[AI Hedge Fund](https://github.com/virattt/ai-hedge-fund)** <br> [![Stars](https://img.shields.io/github/stars/virattt/ai-hedge-fund?style=flat-square&label=%E2%98%85)](https://github.com/virattt/ai-hedge-fund) | virattt | Simulated multi-agent hedge fund team. | Agent roles: market analyst, risk manager, portfolio optimizer, trader. |
| 🔴 **[AI Scientist v2](https://github.com/SakanaAI/AI-Scientist-v2)** <br> [![Stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat-square&label=%E2%98%85)](https://github.com/SakanaAI/AI-Scientist-v2) | SakanaAI | Fully automated scientific discovery agent. | Tree-search planning, paper writing, data generation, automated peer review. |
| 🟢 **[AutoGen](https://github.com/microsoft/autogen)** <br> [![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/autogen) | Microsoft | Multi-agent conversation framework. | Customizable agent personalities, human-in-the-loop, conversable structures. |
| 🟢 **[autogen](https://github.com/microsoft/autogen)** <br> [![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/autogen) | microsoft | A programming framework for agentic AI. | Automated, open-source |
| 🟢 **[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)** <br> [![Stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=flat-square&label=%E2%98%85)](https://github.com/Significant-Gravitas/AutoGPT) | Significant Gravitas | One of the earliest autonomous agent projects. | Multi-agent pipelines, web search, memory integration. |
| 🔴 **[BabyAGI](https://github.com/yoheinakajima/babyagi)** <br> [![Stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=flat-square&label=%E2%98%85)](https://github.com/yoheinakajima/babyagi) | Yohei Nakajima | Lightweight task-driven agent loop. | Simple agent architecture utilizing vector databases and task management pools. |
| 🟢 **[CrewAI](https://github.com/crewAIInc/crewAI)** <br> [![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=flat-square&label=%E2%98%85)](https://github.com/crewAIInc/crewAI) | CrewAI Inc | Role-based agent teams orchestration. | Easy agent role-play definitions, task delegation, sequential or hierarchical execution. |
| 🟢 **[CubeSandbox](https://github.com/TencentCloud/CubeSandbox)** <br> [![Stars](https://img.shields.io/github/stars/TencentCloud/CubeSandbox?style=flat-square&label=%E2%98%85)](https://github.com/TencentCloud/CubeSandbox) | TencentCloud | Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents. | Automated, open-source |
| 🔴 **[DeepAgents](https://github.com/langchain-ai/deepagents)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/deepagents) | LangChain AI | Batteries-included agent harness library. | Standard task interfaces, tool execution wrappers, built-in debug trackers. |
| 🔴 **[Deer Flow](https://github.com/bytedance/deer-flow)** <br> [![Stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=flat-square&label=%E2%98%85)](https://github.com/bytedance/deer-flow) | ByteDance | Long-horizon SuperAgent harness for automated research. | Deep memory architecture, sandboxed execution, goal decomposition. |
| 🔴 **[Dexter](https://github.com/virattt/dexter)** <br> [![Stars](https://img.shields.io/github/stars/virattt/dexter?style=flat-square&label=%E2%98%85)](https://github.com/virattt/dexter) | virattt | Autonomous agent for deep financial research. | Market scraping, portfolio modeling, automated report drafting. |
| 🟢 **[ECC](https://github.com/affaan-m/ECC)** <br> [![Stars](https://img.shields.io/github/stars/affaan-m/ECC?style=flat-square&label=%E2%98%85)](https://github.com/affaan-m/ECC) | affaan-m | The agent harness performance optimization system. | Automated, open-source |
| 🔴 **[Generic Agent](https://github.com/lsdefine/GenericAgent)** <br> [![Stars](https://img.shields.io/github/stars/lsdefine/GenericAgent?style=flat-square&label=%E2%98%85)](https://github.com/lsdefine/GenericAgent) | lsdefine | Self-evolving AI agent with dynamic skill trees. | Seeded by a 3.3K line Python script, builds its own skills, low token overhead. |
| 🔴 **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** <br> [![Stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=flat-square&label=%E2%98%85)](https://github.com/NousResearch/hermes-agent) | Nous Research | An agent that learns and evolves its internal loop processes. | Self-correction heuristics, modular agent graph, adaptive tool binding. |
| 🟢 **[LangGraph](https://github.com/langchain-ai/langgraph)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/langgraph) | LangChain AI | Stateful multi-agent graph orchestrator. | Cycles, human-in-the-loop, structured state, production-ready. |
| 🟢 **[LobeHub](https://github.com/lobehub/lobehub)** <br> [![Stars](https://img.shields.io/github/stars/lobehub/lobehub?style=flat-square&label=%E2%98%85)](https://github.com/lobehub/lobehub) | LobeHub | Chief Agent Operator for organizing and scheduling multi-agent teams. | Multi-agent collaboration, 7x24 agent operations, deep client integration. |
| 🟢 **[mastra](https://github.com/mastra-ai/mastra)** <br> [![Stars](https://img.shields.io/github/stars/mastra-ai/mastra?style=flat-square&label=%E2%98%85)](https://github.com/mastra-ai/mastra) | mastra-ai | Mastra is the modern TypeScript framework for AI-powered applications and agents. | Automated, open-source |
| 🟢 **[MetaGPT](https://github.com/FoundationAgents/MetaGPT)** <br> [![Stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=flat-square&label=%E2%98%85)](https://github.com/FoundationAgents/MetaGPT) | FoundationAgents | Multi-agent framework mimicking software teams. | Simulates product managers, designers, and developers via SOPs. |
| 🔴 **[MiroFish](https://github.com/666ghj/MiroFish)** <br> [![Stars](https://img.shields.io/github/stars/666ghj/MiroFish?style=flat-square&label=%E2%98%85)](https://github.com/666ghj/MiroFish) | 666ghj | Swarm intelligence prediction engine. | Multi-node consensus, predictive optimization loops. |
| 🟡 **[Multica](https://github.com/multica-ai/multica)** <br> [![Stars](https://img.shields.io/github/stars/multica-ai/multica?style=flat-square&label=%E2%98%85)](https://github.com/multica-ai/multica) | Multica AI | Managed open-source agent platform. | Skill compounding, real-time progress logging, teammate assign systems. |
| 🔴 **[OpenMontage](https://github.com/calesthio/OpenMontage)** <br> [![Stars](https://img.shields.io/github/stars/calesthio/OpenMontage?style=flat-square&label=%E2%98%85)](https://github.com/calesthio/OpenMontage) | calesthio | Open-source agentic video production system with 12 pipelines, 52 tools, and 500+ agent skills. | Python / Video Generation |
| 🔴 **[Page Agent](https://github.com/alibaba/page-agent)** <br> [![Stars](https://img.shields.io/github/stars/alibaba/page-agent?style=flat-square&label=%E2%98%85)](https://github.com/alibaba/page-agent) | Alibaba | JavaScript in-page GUI agent that controls web interfaces with natural language. | TypeScript / Web GUI Control |
| 🟢 **[pydantic-ai](https://github.com/pydantic/pydantic-ai)** <br> [![Stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat-square&label=%E2%98%85)](https://github.com/pydantic/pydantic-ai) | pydantic | AI Agent Framework, the Pydantic way. | Automated, open-source |
| 🟡 **[ruflo](https://github.com/ruvnet/ruflo)** <br> [![Stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square&label=%E2%98%85)](https://github.com/ruvnet/ruflo) | ruvnet | Leading agent meta-harness for Claude to deploy multi-agent swarms. | Swarm intelligence, adaptive memory, self-learning workflows, RAG integration. |
| 🟡 **[Sim](https://github.com/simstudioai/sim)** <br> [![Stars](https://img.shields.io/github/stars/simstudioai/sim?style=flat-square&label=%E2%98%85)](https://github.com/simstudioai/sim) | Sim Studio | Workforce agent management layer. | Integrates multi-agent tasks, live team logging, worker synchronization. |
| 🔴 **[TradingAgents](https://github.com/TauricResearch/TradingAgents)** <br> [![Stars](https://img.shields.io/github/stars/TauricResearch/TradingAgents?style=flat-square&label=%E2%98%85)](https://github.com/TauricResearch/TradingAgents) | TauricResearch | Multi-agent LLM financial trading framework. | Simulated trading environments, multi-agent portfolios. |

---

## 🛠️ LLM DevTools & Orchestration Infrastructure
Libraries, SDKs, parsers, and intelligence engines to manage data pipelines, structure outputs, and monitor production AI applications.

| Tool | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟡 **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)** <br> [![Stars](https://img.shields.io/github/stars/Panniantong/Agent-Reach?style=flat-square&label=%E2%98%85)](https://github.com/Panniantong/Agent-Reach) | Panniantong | External internet search harness for agents. | Scraping and reading web pages, social media, and forums without API fees. |
| 🔴 **[AgentiCOW](https://github.com/ruvnet/agenticow)** <br> [![Stars](https://img.shields.io/github/stars/ruvnet/agenticow?style=flat-square&label=%E2%98%85)](https://github.com/ruvnet/agenticow) | ruvnet | Copy-on-Write memory branching tool. | Multi-agent vector database memory snapshots, 83x faster than full persistence. |
| 🟢 **[Claude Video](https://github.com/bradautomates/claude-video)** <br> [![Stars](https://img.shields.io/github/stars/bradautomates/claude-video?style=flat-square&label=%E2%98%85)](https://github.com/bradautomates/claude-video) | bradautomates | Gives Claude the ability to watch any video via download, frame extraction, and transcription. | Video downloads, frame extraction, automated transcription |
| 🔴 **[ClipCannon](https://github.com/ChrisRoyse/clipcannon)** <br> [![Stars](https://img.shields.io/github/stars/ChrisRoyse/clipcannon?style=flat-square&label=%E2%98%85)](https://github.com/ChrisRoyse/clipcannon) | Chris Royse | AI-driven video processing tool that maps transcripts and media segments into semantic vector clusters. | Teleological constellations mapping, video content vector indexing, semantic search. |
| 🔴 **[CodeGraph](https://github.com/colbymchenry/codegraph)** <br> [![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=flat-square&label=%E2%98%85)](https://github.com/colbymchenry/codegraph) | Colby McHenry | Pre-indexed local code knowledge graph. | Syncs automatically on git changes, exposes code indexes locally to avoid API calls. |
| 🟢 **[Crawl4AI](https://github.com/unclecode/crawl4ai)** <br> [![Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=flat-square&label=%E2%98%85)](https://github.com/unclecode/crawl4ai) | unclecode | Open-source LLM-friendly web crawler and scraper for agentic workflows. | High-speed crawling, LLM-ready markdown conversion, structured data extraction |
| 🟢 **[Dify](https://github.com/langgenius/dify)** <br> [![Stars](https://img.shields.io/github/stars/langgenius/dify?style=flat-square&label=%E2%98%85)](https://github.com/langgenius/dify) | LangGenius | Visual LLM app building and operations platform. | Workflow orchestrator, prompt engineering UI, vector db integrations, monitoring dashboards. |
| 🟢 **[firecrawl](https://github.com/mendableai/firecrawl)** <br> [![Stars](https://img.shields.io/github/stars/mendableai/firecrawl?style=flat-square&label=%E2%98%85)](https://github.com/mendableai/firecrawl) | mendableai | The API to search, scrape, and interact with the web at scale. | Automated, open-source |
| 🟢 **[Flowise](https://github.com/FlowiseAI/Flowise)** <br> [![Stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=flat-square&label=%E2%98%85)](https://github.com/FlowiseAI/Flowise) | FlowiseAI | Drag & drop UI for building LangChain/LlamaIndex apps. | Visual nodes, instant API endpoints, chat widget deployments. |
| 🔴 **[GitNexus](https://github.com/abhigyanpatwari/GitNexus)** <br> [![Stars](https://img.shields.io/github/stars/abhigyanpatwari/GitNexus?style=flat-square&label=%E2%98%85)](https://github.com/abhigyanpatwari/GitNexus) | Abhigyan Patwari | Client-side, zero-server repository intelligence engine. | Runs in-browser, maps code dependencies, outputs AI-friendly knowledge maps. |
| 🔴 **[Heretic](https://github.com/p-e-w/heretic)** <br> [![Stars](https://img.shields.io/github/stars/p-e-w/heretic?style=flat-square&label=%E2%98%85)](https://github.com/p-e-w/heretic) | p-e-w | Automatic model censorship removal tool. | Local model tuning layer, automated system alignment bypass. |
| 🟢 **[LangChain](https://github.com/langchain-ai/langchain)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/langchain) | LangChain AI | De facto standard ecosystem for LLM orchestration. | Chains, prompts, data connectors, custom tool integrations, LangSmith observability. |
| 🟢 **[langflow](https://github.com/langflow-ai/langflow)** <br> [![Stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=flat-square&label=%E2%98%85)](https://github.com/langflow-ai/langflow) | langflow-ai | Langflow is a powerful tool for building and deploying AI-powered agents and workflows. | Automated, open-source |
| 🟡 **[Lightpanda Browser](https://github.com/lightpanda-io/browser)** <br> [![Stars](https://img.shields.io/github/stars/lightpanda-io/browser?style=flat-square&label=%E2%98%85)](https://github.com/lightpanda-io/browser) | Lightpanda | Headless browser built in Zig for AI agents. | High-speed, lightweight DOM execution, optimal for sandboxed agent scraping. |
| 🟢 **[LlamaFactory](https://github.com/hiyouga/LlamaFactory)** <br> [![Stars](https://img.shields.io/github/stars/hiyouga/LlamaFactory?style=flat-square&label=%E2%98%85)](https://github.com/hiyouga/LlamaFactory) | hiyouga | Unified efficient fine-tuning framework for 100+ LLMs and VLMs. | Web UI dashboard, multi-GPU training support, RLHF/QLoRA methods. |
| 🟢 **[LlamaIndex](https://github.com/run-llama/llama_index)** <br> [![Stars](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&label=%E2%98%85)](https://github.com/run-llama/llama_index) | LlamaIndex | Data framework for LLM/RAG applications. | Data ingestors, indexing tools, structured queries, custom query engines. |
| 🟢 **[Mem0](https://github.com/mem0ai/mem0)** <br> [![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&label=%E2%98%85)](https://github.com/mem0ai/mem0) | Mem0 | Personalized memory layer for AI agents. | Remembers user preferences, updates context over time, optimizes personalization. |
| 🟢 **[MinerU](https://github.com/opendatalab/MinerU)** <br> [![Stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=flat-square&label=%E2%98%85)](https://github.com/opendatalab/MinerU) | OpenDataLab | Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for agentic workflows. | High-precision PDF layout extraction, structural element recognition. |
| 🟢 **[n8n](https://github.com/n8n-io/n8n)** <br> [![Stars](https://img.shields.io/github/stars/n8n-io/n8n?style=flat-square&label=%E2%98%85)](https://github.com/n8n-io/n8n) | n8n-io | Fair-code workflow automation platform with native AI capabilities. | Visual workflow builder, 400+ integrations, native agent/subagent orchestration nodes. |
| 🟡 **[nimbench](https://github.com/youxufkhan/nimbench)** <br> [![Stars](https://img.shields.io/github/stars/youxufkhan/nimbench?style=flat-square&label=%E2%98%85)](https://github.com/youxufkhan/nimbench) | youxufkhan | A lightweight CLI benchmarking tool for NVIDIA NIM LLMs. | Automated, open-source |
| 🟢 **[OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)** <br> [![Stars](https://img.shields.io/github/stars/iOfficeAI/OfficeCLI?style=flat-square&label=%E2%98%85)](https://github.com/iOfficeAI/OfficeCLI) | iOfficeAI | Office suite purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. | Single binary, no Office installation required, document automation |
| 🟢 **[olmOCR](https://github.com/allenai/olmocr)** <br> [![Stars](https://img.shields.io/github/stars/allenai/olmocr?style=flat-square&label=%E2%98%85)](https://github.com/allenai/olmocr) | Allen Institute for AI | Toolkit for linearizing PDF documents into clean markdown for LLMs. | PDF layout analysis, clean text extraction, markdown linearization |
| 🔴 **[OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf)** <br> [![Stars](https://img.shields.io/github/stars/opendataloader-project/opendataloader-pdf?style=flat-square&label=%E2%98%85)](https://github.com/opendataloader-project/opendataloader-pdf) | OpenDataLoader | Open-source PDF parser optimized for LLM training. | High accuracy structure mapping, table extraction, cleans layout noise. |
| 🔴 **[OpenViking](https://github.com/volcengine/OpenViking)** <br> [![Stars](https://img.shields.io/github/stars/volcengine/OpenViking?style=flat-square&label=%E2%98%85)](https://github.com/volcengine/OpenViking) | Volcengine | Context database tailored for AI agents. | Persistent agent memory storage, runtime resource management, skill indexes. |
| 🟢 **[openwiki](https://github.com/langchain-ai/openwiki)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/openwiki?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/openwiki) | langchain-ai | OpenWiki is a CLI that writes and maintains agent documentation for your codebase. | Automated, open-source |
| 🟢 **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** <br> [![Stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=flat-square&label=%E2%98%85)](https://github.com/PaddlePaddle/PaddleOCR) | PaddlePaddle | Document-to-text OCR parser. | Supports 100+ languages, extracts layout and tables from scanned documents. |
| 🟢 **[ragflow](https://github.com/infiniflow/ragflow)** <br> [![Stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=flat-square&label=%E2%98%85)](https://github.com/infiniflow/ragflow) | infiniflow | RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine. | Automated, open-source |
| 🟢 **[Supermemory](https://github.com/supermemoryai/supermemory)** <br> [![Stars](https://img.shields.io/github/stars/supermemoryai/supermemory?style=flat-square&label=%E2%98%85)](https://github.com/supermemoryai/supermemory) | supermemoryai | Context and memory engine for AI apps. | High-speed, fully local or cloud-hosted memory API for storing agent context. |
| 🟢 **[TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)** <br> [![Stars](https://img.shields.io/github/stars/TencentCloud/TencentDB-Agent-Memory?style=flat-square&label=%E2%98%85)](https://github.com/TencentCloud/TencentDB-Agent-Memory) | TencentCloud | TencentDB Agent Memory delivers fully local long-term memory for AI Agents. | Automated, open-source |
| 🟢 **[Video Use](https://github.com/browser-use/video-use)** <br> [![Stars](https://img.shields.io/github/stars/browser-use/video-use?style=flat-square&label=%E2%98%85)](https://github.com/browser-use/video-use) | browser-use | Edit videos using autonomous coding agents. | Video editing interface, agent workflow orchestration, media automation |

---

## 📡 Model Context Protocol (MCP) Servers
MCP is a protocol designed to connect LLMs to data, tools, filesystems, and external APIs. Exposes services to MCP-compliant agents (e.g. Gemini CLI, Claude Code, Cline).

| MCP Server | Creator | Description | Tools / Access Exposed |
| :--- | :--- | :--- | :--- |
| 🟢 **[Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws)** <br> [![Stars](https://img.shields.io/github/stars/aws/agent-toolkit-for-aws?style=flat-square&label=%E2%98%85)](https://github.com/aws/agent-toolkit-for-aws) | AWS | Official AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS. | AWS services access (S3, EC2, Bedrock, etc.) |
| 🟢 **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** <br> [![Stars](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=flat-square&label=%E2%98%85)](https://github.com/punkpeye/awesome-mcp-servers) | punkpeye | A collection of MCP servers. | Automated, open-source |
| 🟡 **[Claude Context MCP](https://github.com/zilliztech/claude-context)** <br> [![Stars](https://img.shields.io/github/stars/zilliztech/claude-context?style=flat-square&label=%E2%98%85)](https://github.com/zilliztech/claude-context) | Zilliz Tech | Vector search-based code search MCP server. | Code search over huge codebases, fast local similarity query tools. |
| 🔴 **[Context7](https://github.com/upstash/context7)** <br> [![Stars](https://img.shields.io/github/stars/upstash/context7?style=flat-square&label=%E2%98%85)](https://github.com/upstash/context7) | Upstash | Serverless state and tool cache. | Caches tool executions, manages state across agent handoffs. |
| 🟢 **[Desktop Commander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP)** <br> [![Stars](https://img.shields.io/github/stars/wonderwhy-er/DesktopCommanderMCP?style=flat-square&label=%E2%98%85)](https://github.com/wonderwhy-er/DesktopCommanderMCP) | wonderwhy-er | MCP server for Claude that provides terminal control, file system search, and diff editing. | Terminal control, file search, diff file editing |
| 🟢 **[GitHub MCP Server](https://github.com/github/github-mcp-server)** <br> [![Stars](https://img.shields.io/github/stars/github/github-mcp-server?style=flat-square&label=%E2%98%85)](https://github.com/github/github-mcp-server) | GitHub | Official GitHub API bridge. | Lists issues, manages PRs, commits changes, searches repositories. |
| 🟢 **[MCP Servers Repo](https://github.com/modelcontextprotocol/servers)** <br> [![Stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=flat-square&label=%E2%98%85)](https://github.com/modelcontextprotocol/servers) | Anthropic | Standard repository of reference MCP servers. | Postgres, SQLite, Slack, GitHub, Puppeteer, Brave Search. |
| 🟢 **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** <br> [![Stars](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/playwright-mcp) | Microsoft | Browser automation server. | Exposes headless browser actions (navigate, click, type, screenshot). |

---

## ⚡ LLM Inference & Local Serving Engines
Engines designed to run, serve, and perform inference with large language models locally or in private clouds.

| Engine | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[GPT4All](https://github.com/nomic-ai/gpt4all)** <br> [![Stars](https://img.shields.io/github/stars/nomic-ai/gpt4all?style=flat-square&label=%E2%98%85)](https://github.com/nomic-ai/gpt4all) | Nomic AI | Desktop app and SDK for local LLM execution. | Runs locally on consumer GPUs/CPUs, built-in search/document RAG capabilities. |
| 🟡 **[LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)** <br> [![Stars](https://img.shields.io/github/stars/google-ai-edge/LiteRT-LM?style=flat-square&label=%E2%98%85)](https://github.com/google-ai-edge/LiteRT-LM) | Google AI Edge | Edge device model inference engine. | Highly optimized for mobile devices and embedded hardware. |
| 🟢 **[llama.cpp](https://github.com/ggml-org/llama.cpp)** <br> [![Stars](https://img.shields.io/github/stars/ggml-org/llama.cpp?style=flat-square&label=%E2%98%85)](https://github.com/ggml-org/llama.cpp) | GGML Org | High-performance inference engine in C/C++. | CPU/GPU execution, low memory overhead, broad hardware support. |
| 🟢 **[Llamafile](https://github.com/Mozilla-Ocho/llamafile)** <br> [![Stars](https://img.shields.io/github/stars/Mozilla-Ocho/llamafile?style=flat-square&label=%E2%98%85)](https://github.com/Mozilla-Ocho/llamafile) | Mozilla Ocho | Single-file executable for local LLMs. | Runs across 6 OS platforms without installations, fast CPU execution. |
| 🔴 **[llmfit](https://github.com/AlexsJones/llmfit)** <br> [![Stars](https://img.shields.io/github/stars/AlexsJones/llmfit?style=flat-square&label=%E2%98%85)](https://github.com/AlexsJones/llmfit) | AlexsJones | Find out which local models and providers run on your hardware. | Model hardware scanner, benchmark testing, single-command usage. |
| 🟢 **[LMCache](https://github.com/LMCache/LMCache)** <br> [![Stars](https://img.shields.io/github/stars/LMCache/LMCache?style=flat-square&label=%E2%98%85)](https://github.com/LMCache/LMCache) | LMCache | LMCache: Supercharge Your LLM with the Fastest KV Cache Layer. | Automated, open-source |
| 🟢 **[LocalAI](https://github.com/mudler/LocalAI)** <br> [![Stars](https://img.shields.io/github/stars/mudler/LocalAI?style=flat-square&label=%E2%98%85)](https://github.com/mudler/LocalAI) | mudler | Drop-in OpenAI replacement for local models. | Supports audio generation, images, embedding, and text models. |
| 🟢 **[Ollama](https://github.com/ollama/ollama)** <br> [![Stars](https://img.shields.io/github/stars/ollama/ollama?style=flat-square&label=%E2%98%85)](https://github.com/ollama/ollama) | Ollama | Package and run LLMs locally on macOS, Linux, and Windows. | Simple CLI, one-line installs (Llama 3, Phi, Qwen), OpenAI compatible API. |
| 🟢 **[SGLang](https://github.com/sgl-project/sglang)** <br> [![Stars](https://img.shields.io/github/stars/sgl-project/sglang?style=flat-square&label=%E2%98%85)](https://github.com/sgl-project/sglang) | SGLang Project | Structured generation language & engine. | High throughput serving, prompt caching, JSON schema constraints. |
| 🟢 **[Text-generation-webui](https://github.com/oobabooga/text-generation-webui)** <br> [![Stars](https://img.shields.io/github/stars/oobabooga/text-generation-webui?style=flat-square&label=%E2%98%85)](https://github.com/oobabooga/text-generation-webui) | oobabooga | Gradio web UI for running local models. | Supports transformers, llama.cpp, ExLlamaV2, custom parameter sliders. |
| 🟢 **[vLLM](https://github.com/vllm-project/vllm)** <br> [![Stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square&label=%E2%98%85)](https://github.com/vllm-project/vllm) | vLLM Project | High-throughput, memory-efficient LLM serving engine. | PagedAttention, continuous batching, distributed inference, serving API. |

---

## 🗄️ Vector Databases & Vector Stores
Specialized databases built to index, store, and query high-dimensional embeddings for RAG and agent memory.

| Database | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[Chroma](https://github.com/chroma-core/chroma)** <br> [![Stars](https://img.shields.io/github/stars/chroma-core/chroma?style=flat-square&label=%E2%98%85)](https://github.com/chroma-core/chroma) | Chroma Core | Lightweight, developer-friendly open-source vector store. | Fast python setup, ideal for notebooks and rapid prototyping. |
| 🟢 **[Deep Lake](https://github.com/activeloopai/deeplake)** <br> [![Stars](https://img.shields.io/github/stars/activeloopai/deeplake?style=flat-square&label=%E2%98%85)](https://github.com/activeloopai/deeplake) | activeloopai | AI Data Runtime for Agents, serverless postgres, and multimodal datalake. | Multimodal storage, RAG integration, vector query and training runtime. |
| 🟢 **[FAISS](https://github.com/facebookresearch/faiss)** <br> [![Stars](https://img.shields.io/github/stars/facebookresearch/faiss?style=flat-square&label=%E2%98%85)](https://github.com/facebookresearch/faiss) | Meta Research | Library for efficient similarity search of dense vectors. | GPU acceleration, fast index algorithms, local run implementation. |
| 🟢 **[lancedb](https://github.com/lancedb/lancedb)** <br> [![Stars](https://img.shields.io/github/stars/lancedb/lancedb?style=flat-square&label=%E2%98%85)](https://github.com/lancedb/lancedb) | lancedb | Developer-friendly OSS embedded retrieval library for multimodal AI. | Automated, open-source |
| 🟢 **[Milvus](https://github.com/milvus-io/milvus)** <br> [![Stars](https://img.shields.io/github/stars/milvus-io/milvus?style=flat-square&label=%E2%98%85)](https://github.com/milvus-io/milvus) | Milvus | High-performance, distributed vector database. | Built for billion-scale datasets, GPU indexing, hybrid search support. |
| 🟢 **[Qdrant](https://github.com/qdrant/qdrant)** <br> [![Stars](https://img.shields.io/github/stars/qdrant/qdrant?style=flat-square&label=%E2%98%85)](https://github.com/qdrant/qdrant) | Qdrant | Rust-based vector similarity search engine. | Fast payload filtering, REST/gRPC interfaces, production scale. |

---

## 🎨 Vibe Coding & Generative UI Tools
Tools designed to let non-technical users or visual developers generate layouts, notes, and whole apps using AI natural language ("vibe coding").

| Tool | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[AFFiNE](https://github.com/toeverything/AFFiNE)** <br> [![Stars](https://img.shields.io/github/stars/toeverything/AFFiNE?style=flat-square&label=%E2%98%85)](https://github.com/toeverything/AFFiNE) | toeverything | Workspace tool unifying notes, tasks, and graphics. | AI-native drawing, structured page layout generation. |
| 🔴 **[AI Website Cloner Template](https://github.com/JCodesMore/ai-website-cloner-template)** <br> [![Stars](https://img.shields.io/github/stars/JCodesMore/ai-website-cloner-template?style=flat-square&label=%E2%98%85)](https://github.com/JCodesMore/ai-website-cloner-template) | JCodesMore | Clone any website with one command using AI coding agents. | TypeScript / Website cloning |
| 🟡 **[Astryx](https://github.com/facebook/astryx)** <br> [![Stars](https://img.shields.io/github/stars/facebook/astryx?style=flat-square&label=%E2%98%85)](https://github.com/facebook/astryx) | Facebook | Agent-ready open-source design system. | Fully customizable design system components tailored for LLM visual generation. |
| 🟢 **[bolt.diy](https://github.com/stackblitz-labs/bolt.diy)** <br> [![Stars](https://img.shields.io/github/stars/stackblitz-labs/bolt.diy?style=flat-square&label=%E2%98%85)](https://github.com/stackblitz-labs/bolt.diy) | stackblitz-labs | Prompt, run, edit, and deploy full-stack web applications using any LLM you want! | Automated, open-source |
| 🟢 **[Chatbot UI](https://github.com/mckaywrigley/chatbot-ui)** <br> [![Stars](https://img.shields.io/github/stars/mckaywrigley/chatbot-ui?style=flat-square&label=%E2%98%85)](https://github.com/mckaywrigley/chatbot-ui) | McKay Wrigley | A clean, customizable front-end for LLM APIs. | Custom prompt templates, system instructions, attachment parsing. |
| 🟡 **[InsForge](https://github.com/InsForge/InsForge)** <br> [![Stars](https://img.shields.io/github/stars/InsForge/InsForge?style=flat-square&label=%E2%98%85)](https://github.com/InsForge/InsForge) | InsForge | Backend-as-a-service (BaaS) platform optimized for agentic coding. | PostgreSQL database, auth, storage, edge functions, structured schemas for AI agent usage. |
| 🟢 **[Meetily](https://github.com/Zackriya-Solutions/meetily)** <br> [![Stars](https://img.shields.io/github/stars/Zackriya-Solutions/meetily?style=flat-square&label=%E2%98%85)](https://github.com/Zackriya-Solutions/meetily) | Zackriya Solutions | Privacy-first, local AI meeting assistant with Whisper transcription, speaker diarization, and Ollama summarization. | 100% local processing, Whisper transcription, speaker diarization |
| 🔴 **[NanoChat](https://github.com/karpathy/nanochat)** <br> [![Stars](https://img.shields.io/github/stars/karpathy/nanochat?style=flat-square&label=%E2%98%85)](https://github.com/karpathy/nanochat) | Andrej Karpathy | Minimalist ChatGPT clone. | Simple code, easily extensible, fast API connections. |
| 🟢 **[Onyx](https://github.com/onyx-dot-app/onyx)** <br> [![Stars](https://img.shields.io/github/stars/onyx-dot-app/onyx?style=flat-square&label=%E2%98%85)](https://github.com/onyx-dot-app/onyx) | Onyx App | Open source chat platform designed for multiple LLMs. | Advanced chat options, workspace customization. |
| 🟢 **[open-webui](https://github.com/open-webui/open-webui)** <br> [![Stars](https://img.shields.io/github/stars/open-webui/open-webui?style=flat-square&label=%E2%98%85)](https://github.com/open-webui/open-webui) | open-webui | User-friendly AI Interface (Supports Ollama, OpenAI API, ...). | Automated, open-source |
| 🟡 **[OpenUI](https://github.com/wandb/openui)** <br> [![Stars](https://img.shields.io/github/stars/wandb/openui?style=flat-square&label=%E2%98%85)](https://github.com/wandb/openui) | Weights & Biases | Generates responsive HTML/CSS layouts visually from description. | Direct Tailwind/React component export, interactive design editor. |
| 🔴 **[Thunderbolt](https://github.com/thunderbird/thunderbolt)** <br> [![Stars](https://img.shields.io/github/stars/thunderbird/thunderbolt?style=flat-square&label=%E2%98%85)](https://github.com/thunderbird/thunderbolt) | Thunderbird | Personal client for running customizable AI models. | Local data control, no vendor lock-in UI. |

---

## 📖 AI Learning & Educational Resources
Structured courses, notebooks, and reference materials designed to teach developers how to design neural networks and build AI agents from scratch.

| Resource | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects)** <br> [![Stars](https://img.shields.io/github/stars/ashishpatel26/500-AI-Agents-Projects?style=flat-square&label=%E2%98%85)](https://github.com/ashishpatel26/500-AI-Agents-Projects) | ashishpatel26 | The 500 AI Agents Projects is a curated collection of AI agent use cases across various industries. | Automated, open-source |
| 🟢 **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** <br> [![Stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/ai-agents-for-beginners) | Microsoft | 12-lesson roadmap for learning to build AI agents. | Structured lectures, notebook labs, tool-calling and planning basics. |
| 🟢 **[Awesome AI Coding Tools](https://github.com/ai-for-developers/awesome-ai-coding-tools)** <br> [![Stars](https://img.shields.io/github/stars/ai-for-developers/awesome-ai-coding-tools?style=flat-square&label=%E2%98%85)](https://github.com/ai-for-developers/awesome-ai-coding-tools) | AI-for-Developers | Curated index of AI-powered developer utilities. | Comprehensive list of developer extensions, IDEs, and tools. |
| 🟡 **[awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026)** <br> [![Stars](https://img.shields.io/github/stars/caramaschiHG/awesome-ai-agents-2026?style=flat-square&label=%E2%98%85)](https://github.com/caramaschiHG/awesome-ai-agents-2026) | caramaschiHG | 🤖 The most comprehensive list of AI agents, frameworks & tools in 2026. | Automated, open-source |
| 🟢 **[awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** <br> [![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-design-md?style=flat-square&label=%E2%98%85)](https://github.com/VoltAgent/awesome-design-md) | VoltAgent | A collection of DESIGN.md files analysis by popular brand design systems. | Automated, open-source |
| 🟢 **[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** <br> [![Stars](https://img.shields.io/github/stars/Shubhamsaboo/awesome-llm-apps?style=flat-square&label=%E2%98%85)](https://github.com/Shubhamsaboo/awesome-llm-apps) | Shubhamsaboo | 100+ AI Agent & RAG apps you can actually run — clone, customize, ship. | Automated, open-source |
| 🟡 **[awesome-llm-tools](https://github.com/sam-blackfly/awesome-llm-tools)** <br> [![Stars](https://img.shields.io/github/stars/sam-blackfly/awesome-llm-tools?style=flat-square&label=%E2%98%85)](https://github.com/sam-blackfly/awesome-llm-tools) | sam-blackfly | A curated directory of essential LLM tools. | Automated, open-source |
| 🟡 **[Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice)** <br> [![Stars](https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat-square&label=%E2%98%85)](https://github.com/shanraisshan/claude-code-best-practice) | shanraisshan | Guidelines and tips for transition from vibe coding to agentic engineering with Claude Code. | Structured best practices, prompt optimization, workflow patterns. |
| 🟡 **[Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code)** <br> [![Stars](https://img.shields.io/github/stars/shareAI-lab/learn-claude-code?style=flat-square&label=%E2%98%85)](https://github.com/shareAI-lab/learn-claude-code) | shareAI-lab | Educational nano-agent tutorial showing how to build a Claude Code-like harness from scratch. | Code walkthroughs, lightweight bash-to-LLM bindings, agentic tutorials. |
| 🟡 **[Modded NanoGPT](https://github.com/KellerJordan/modded-nanogpt)** <br> [![Stars](https://img.shields.io/github/stars/KellerJordan/modded-nanogpt?style=flat-square&label=%E2%98%85)](https://github.com/KellerJordan/modded-nanogpt) | Keller Jordan | Extremely fast, modified NanoGPT training repo. | Achieves 124M parameter training in 90 seconds, showcases optimization. |
| 🟢 **[Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)** <br> [![Stars](https://img.shields.io/github/stars/karpathy/nn-zero-to-hero?style=flat-square&label=%E2%98%85)](https://github.com/karpathy/nn-zero-to-hero) | Andrej Karpathy | Detailed guide to building neural networks from scratch. | From basic backpropagation to GPT, PyTorch labs, video lecture companion. |
| 🟢 **[Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** <br> [![Stars](https://img.shields.io/github/stars/dair-ai/Prompt-Engineering-Guide?style=flat-square&label=%E2%98%85)](https://github.com/dair-ai/Prompt-Engineering-Guide) | DAIR.AI | Curated guides, papers, notebooks, and learning paths for prompt/context engineering and AI agents. | Structured papers index, learning materials, system prompt models. |
| 🟡 **[System Prompts Leaks](https://github.com/asgeirtj/system_prompts_leaks)** <br> [![Stars](https://img.shields.io/github/stars/asgeirtj/system_prompts_leaks?style=flat-square&label=%E2%98%85)](https://github.com/asgeirtj/system_prompts_leaks) | asgeirtj | Repository of extracted system prompts. | Provides prompt structures for frontier models, coding assistants, and agents. |
| 🟢 **[Unsloth](https://github.com/unslothai/unsloth)** <br> [![Stars](https://img.shields.io/github/stars/unslothai/unsloth?style=flat-square&label=%E2%98%85)](https://github.com/unslothai/unsloth) | Unsloth AI | Web UI and training environment for fine-tuning open weights models. | 2x-5x faster model training, lightweight local setup (Gemma, Qwen, DeepSeek). |

---

## 📊 Quick Comparison Matrix

| Tool | Category | Licensing | Primary Language / Stack | Best Suited For... |
| :--- | :--- | :--- | :--- | :--- |
| **[Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws)** | MCP Server | Apache-2.0 | Python | Exposing AWS services securely to coding agents via MCP |
| **[AI Job Search](https://github.com/MadsLorentzen/ai-job-search)** | CLI Tool | MIT | TypeScript | Automating job application matching, CV tailoring, and interview prep |
| **Antigravity CLI** | CLI Agent | Proprietary | Python / CLI | Sandboxed multi-agent and browser-based test loops |
| **Claude Code** | CLI Agent | Proprietary | TypeScript / Node.js | Multi-file codebase adjustments using Claude |
| **CodeGate** | Security Proxy | Apache-2.0 | Go / Rust | Masking secrets and PII from outgoing LLM traffic |
| **[CrewAI](https://github.com/crewAIInc/crewAI)** | Agent Framework | MIT | Python | Role-based agent teams mimicking human software processes |
| **[Cursor](https://www.cursor.com/)** | Native IDE | Proprietary | VS Code Fork | The most polished, complete AI-native coding environment |
| **[DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)** | CLI Agent | MIT | Go / TUI | High prefix-cache utilization and low-cost DeepSeek terminal pair programming |
| **Gemini CLI** | CLI Agent | MIT | TypeScript / Node.js | Fast, tool-equipped CLI coding using Google Gemini models |
| **Goose** | CLI Agent | Apache-2.0 | Rust / Python | Executing task checklists with MCP plugins |
| **gstack** | Custom Skill Pack | MIT | TypeScript | Opinionated agent roles (CEO, Designer, Doc Engineer) for Claude Code |
| **[LangGraph](https://github.com/langchain-ai/langgraph)** | Agent Framework | MIT | Python / JS | Custom stateful multi-agent workflows and graph logic |
| **[MiMo Code](https://github.com/XiaomiMiMo/MiMo-Code)** | CLI Agent | MIT | Python / CLI | Long-running developer sessions with persistent memory support |
| **[Ollama](https://github.com/ollama/ollama)** | Serving Engine | MIT | Go / C++ | Running and exposing open-weights models locally |
| **OpenHands** | CLI Agent / Web | Apache-2.0 | Python / Docker | Isolated container-level SWE benchmarks and repairs |
| **[Terax AI](https://github.com/crynta/terax-ai)** | Native IDE | Apache-2.0 | TypeScript | High-speed, lightweight terminal-native AI-assisted development |

---

## 🤝 Contributing

We welcome contributions! If you would like to add a new tool, extension, proxy, plugin, or CLI agent:

1. Fork this repository.
2. Add the tool to the appropriate table in alphabetical order.
3. Submit a Pull Request with a clear description of the tool.
