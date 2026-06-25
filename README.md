# Awesome AI Coding Tools, IDEs & Agents 🚀

A curated, comprehensive list of awesome AI coding tools, autonomous agents, AI-native IDEs, extensions, LLM orchestrators, inference engines, vector databases, MCP servers, custom agent skills, security proxies, and educational resources.

### 🏷️ Maturity Rating Legend
* 🟢 **Stable / Production-Ready**: Established, highly stable tools with low bug rates and robust production suitability.
* 🟡 **Active Development**: Fully functional tools undergoing rapid iterations. Expect frequent feature updates.
* 🔴 **Experimental / Beta**: Early-stage prototypes, proofs-of-concept, or bleeding-edge releases. High potential but unstable.


---

## 📂 Table of Contents
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
| 🟢 **[Aider](https://github.com/aider-chat/aider)** <br> [![Stars](https://img.shields.io/github/stars/aider-chat/aider?style=flat-square&label=%E2%98%85)](https://github.com/aider-chat/aider) | Aider-chat | Git-integrated terminal pair programmer. | Edits files in-place, writes automatic git commits, works with local/remote LLMs. |
| 🟢 **[Antigravity CLI](https://github.com/google-deepmind/antigravity)** <br> [![Stars](https://img.shields.io/github/stars/google-deepmind/antigravity?style=flat-square&label=%E2%98%85)](https://github.com/google-deepmind/antigravity) | Google DeepMind | Advanced agentic CLI pair programmer. | Parallel subagent orchestration, sandboxed browser testing, deep git integration. |
| 🟡 **[Claude Code](https://github.com/anthropics/claude-code)** <br> [![Stars](https://img.shields.io/github/stars/anthropics/claude-code?style=flat-square&label=%E2%98%85)](https://github.com/anthropics/claude-code) | Anthropic | Command-line agent powered by Claude models. | 1M+ token context window, deep reasoning, multi-file code workspace editing. |
| 🔴 **[Claw Code Example](https://github.com/ultraworkers/claw-code)** <br> [![Stars](https://img.shields.io/github/stars/ultraworkers/claw-code?style=flat-square&label=%E2%98%85)](https://github.com/ultraworkers/claw-code) | Ultraworkers | Rust-based repository managed automatically by agentic code. | Demonstrates zero human intervention maintenance, autonomous documentation. |
| 🟡 **[cc-switch](https://github.com/farion1231/cc-switch)** <br> [![Stars](https://img.shields.io/github/stars/farion1231/cc-switch?style=flat-square&label=%E2%98%85)](https://github.com/farion1231/cc-switch) | farion1231 | Cross-platform desktop All-in-One assistant manager for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes. | Desktop wrapper, multi-agent provider switching, WSL support. |
| 🟡 **[Devika](https://github.com/mufeedvh/devika)** <br> [![Stars](https://img.shields.io/github/stars/mufeedvh/devika?style=flat-square&label=%E2%98%85)](https://github.com/mufeedvh/devika) | Mufeed VH | Open-source clone of Cognition's Devin. | Plan-execute-monitor coding loops, agentic browser search. |
| 🟡 **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** <br> [![Stars](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=flat-square&label=%E2%98%85)](https://github.com/google-gemini/gemini-cli) | Google Gemini | An open-source, terminal-first AI agent powered by Gemini. | ReAct loops, MCP server compatibility, Google Search grounding, git workflows. |
| 🟡 **[Goose](https://github.com/block/goose)** <br> [![Stars](https://img.shields.io/github/stars/block/goose?style=flat-square&label=%E2%98%85)](https://github.com/block/goose) | Block | Extensible open-source coding agent. | Local or desktop run modes, built-in MCP client, custom developer plugins. |
| **[GPT-Engineer](https://github.com/gpt-engineer-org/gpt-engineer)** | GPT-Engineer Org | Full codebase generator from prompts. | Generates complete frameworks, interactive query staging. |
| 🟢 **[Mentat](https://github.com/ggarrett8/mentat)** <br> [![Stars](https://img.shields.io/github/stars/ggarrett8/mentat?style=flat-square&label=%E2%98%85)](https://github.com/ggarrett8/mentat) | Mentat | Context-aware codebase editor. | Customized file indexing, fast command loop, interactive diff views. |
| 🔴 **[Oh My Codex (OmX)](https://github.com/Yeachan-Heo/oh-my-codex)** <br> [![Stars](https://img.shields.io/github/stars/Yeachan-Heo/oh-my-codex?style=flat-square&label=%E2%98%85)](https://github.com/Yeachan-Heo/oh-my-codex) | Yeachan Heo | Orchestration hooks and head-up display tools for local coders. | Multi-agent configurations, diagnostic heads, scriptable workflow bindings. |
| 🔴 **[Oh My Pi](https://github.com/can1357/oh-my-pi)** <br> [![Stars](https://img.shields.io/github/stars/can1357/oh-my-pi?style=flat-square&label=%E2%98%85)](https://github.com/can1357/oh-my-pi) | can1357 | A terminal-native AI coding agent with advanced tool harness. | Hash-anchored edits, LSP integration, browser automation, subagent delegation. |
| 🔴 **[OpenAI Codex CLI](https://github.com/openai/openai-cookbook)** <br> [![Stars](https://img.shields.io/github/stars/openai/openai-cookbook?style=flat-square&label=%E2%98%85)](https://github.com/openai/openai-cookbook) | OpenAI | Basic terminal execution wrappers for Codex/GPT-4. | Script writing, direct terminal-based shell translations. |
| 🟡 **[Open Claude Code Decompile](https://github.com/ruvnet/open-claude-code)** <br> [![Stars](https://img.shields.io/github/stars/ruvnet/open-claude-code?style=flat-square&label=%E2%98%85)](https://github.com/ruvnet/open-claude-code) | ruvnet | Reverse-engineered and rebuilt nightly Claude Code CLI helper. | Custom hooks, custom execution routing, diagnostic extensions. |
| 🟡 **[OpenClaw](https://github.com/openclaw/openclaw)** <br> [![Stars](https://img.shields.io/github/stars/openclaw/openclaw?style=flat-square&label=%E2%98%85)](https://github.com/openclaw/openclaw) | OpenClaw | Personal AI assistant running on any platform. | Agentic task orchestration, cross-platform local execution, visual tools. |
| 🔴 **[OpenClaude](https://github.com/Gitlawb/openclaude)** <br> [![Stars](https://img.shields.io/github/stars/Gitlawb/openclaude?style=flat-square&label=%E2%98%85)](https://github.com/Gitlawb/openclaude) | Gitlawb | Adaptable terminal assistant designed to run on any model provider. | Flexible tool bindings, de-coupled backend, command automation. |
| 🟡 **[OpenCode](https://github.com/anomalyco/opencode)** <br> [![Stars](https://img.shields.io/github/stars/anomalyco/opencode?style=flat-square&label=%E2%98%85)](https://github.com/anomalyco/opencode) | Anomaly | Model-agnostic terminal developer agent. | Go-based TUI, 75+ LLM providers supported, LSP diagnostics, version control snapshots. |
| 🟢 **[OpenHands (formerly OpenDevin)](https://github.com/All-Hands-AI/OpenHands)** <br> [![Stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square&label=%E2%98%85)](https://github.com/All-Hands-AI/OpenHands) | All-Hands AI | Docker-sandboxed autonomous coding agent. | Runs shell commands, browses the web, reads/writes code inside isolated containers. |
| 🔴 **[OpenSWE](https://github.com/langchain-ai/open-swe)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/open-swe?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/open-swe) | LangChain AI | Open-source asynchronous coding agent framework. | Stateful planning loops, async task execution, customizable LLM backend routes. |
| 🟡 **[Pi Agent](https://github.com/earendil-works/pi)** <br> [![Stars](https://img.shields.io/github/stars/earendil-works/pi?style=flat-square&label=%E2%98%85)](https://github.com/earendil-works/pi) | Earendil Works | A terminal-first AI agent toolkit and harness. | Unified LLM API, agent loop, interactive TUI, session persistence, modular tool architecture. |
| 🟢 **[Plandex](https://github.com/plandex-ai/plandex)** <br> [![Stars](https://img.shields.io/github/stars/plandex-ai/plandex?style=flat-square&label=%E2%98%85)](https://github.com/plandex-ai/plandex) | Plandex AI | Large-task codebase editor. | Sandboxed file staging, handles massive refactoring pipelines. |
| 🟢 **[PR Agent](https://github.com/The-PR-Agent/pr-agent)** <br> [![Stars](https://img.shields.io/github/stars/The-PR-Agent/pr-agent?style=flat-square&label=%E2%98%85)](https://github.com/The-PR-Agent/pr-agent) | Qodo / CodiumAI | Autonomous PR reviewer and description generator. | Git provider integrations (GitHub, GitLab, Bitbucket), auto-docs, code suggestions. |
| 🟢 **[SWE-agent](https://github.com/princeton-nlp/SWE-agent)** <br> [![Stars](https://img.shields.io/github/stars/princeton-nlp/SWE-agent?style=flat-square&label=%E2%98%85)](https://github.com/princeton-nlp/SWE-agent) | Princeton NLP | Agent-Computer Interface (ACI) coder framework. | Top SWE-bench performer, optimized file editing and search tools for LLMs. |
| 🟢 **[Sweep](https://github.com/sweepai/sweep)** <br> [![Stars](https://img.shields.io/github/stars/sweepai/sweep?style=flat-square&label=%E2%98%85)](https://github.com/sweepai/sweep) | Sweep AI | GitHub issue solver bot. | Automatic PR creation, lint fixing, and CI/CD validation. |

---

## 💻 AI-Native IDEs & Cloud Workspaces
Integrated Development Environments (IDEs) built with AI agents at the center of the coding experience.

| Editor / Workspace | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[Cherry Studio](https://github.com/CherryHQ/cherry-studio)** <br> [![Stars](https://img.shields.io/github/stars/CherryHQ/cherry-studio?style=flat-square&label=%E2%98%85)](https://github.com/CherryHQ/cherry-studio) | CherryHQ | AI productivity studio with smart chat, autonomous agents, and 300+ assistants. | Unified access to frontier LLMs, multiple assistant panels, offline capabilities. |
| 🟡 **[ClawX](https://github.com/ValueCell-ai/ClawX)** <br> [![Stars](https://img.shields.io/github/stars/ValueCell-ai/ClawX?style=flat-square&label=%E2%98%85)](https://github.com/ValueCell-ai/ClawX) | ValueCell-ai | Graphical desktop interface for OpenClaw AI agents. | Visual agent configuration, no-code execution controls, local execution logs. |
| 🟢 **[Cursor](https://www.cursor.com/)** | Anysphere | Leading VS Code fork with deep AI integration. | "Composer" multi-file agent, autocomplete, inline codebase chat, custom index. |
| 🟢 **[GitHub Copilot Workspace](https://github.com/features/copilot)** <br> [![Stars](https://img.shields.io/github/stars/features/copilot?style=flat-square&label=%E2%98%85)](https://github.com/features/copilot) | GitHub / Microsoft | Task-centric cloud workspace. | Interactive issue plans, automated task lists, instant sandbox edits. |
| 🟡 **[Melty](https://github.com/melty-labs/melty)** <br> [![Stars](https://img.shields.io/github/stars/melty-labs/melty?style=flat-square&label=%E2%98%85)](https://github.com/melty-labs/melty) | Melty Labs | Open-source IDE that learns from developers. | Tracks git actions, code pattern indexing, smart autocompletion. |
| 🟢 **[PearAI](https://trypear.ai/)** | PearAI | Fully open-source VS Code fork. | Custom assistant panel, inline refactoring, privacy controls. |
| 🟢 **[Project IDX](https://idx.dev/)** | Google | Cloud-based developer workspace. | Multiplatform templates, integrated Gemini chat, device emulators. |
| 🟢 **[Replit Agent](https://replit.com)** | Replit | Browser-based full-stack developer agent. | App creation, instant DB setup, one-click deployments. |
| 🟢 **[Windsurf](https://codeium.com/windsurf)** | Codeium | Agent-first IDE based on VS Code. | "Windsurf Flow" collaborative loops, fast indexing, persistent codebase context. |
| 🟢 **[Zed AI](https://zed.dev/ai)** | Zed Decent | High-performance, collaborative rust-based IDE. | Multi-buffer editing, instant startup, inline LLM chats (OpenAI/Anthropic). |

---

## 🧩 AI Coding Extensions & Plugins
Augmentative extensions to supercharge traditional IDEs (VS Code, JetBrains, Neovim).

| Extension | Platform Support | Creator | Description / Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[GitHub Copilot](https://github.com/features/copilot)** <br> [![Stars](https://img.shields.io/github/stars/features/copilot?style=flat-square&label=%E2%98%85)](https://github.com/features/copilot) | VS Code, JetBrains, Visual Studio, Neovim | GitHub | Fast autocomplete, chat panels, codebase indexing, PR description generator. |
| 🟢 **[Continue](https://github.com/continuedev/continue)** <br> [![Stars](https://img.shields.io/github/stars/continuedev/continue?style=flat-square&label=%E2%98%85)](https://github.com/continuedev/continue) | VS Code, JetBrains | Continue | Open-source, model-agnostic extension. Connects to Ollama (local) or API keys. |
| 🟢 **[Cline](https://github.com/cline/cline)** <br> [![Stars](https://img.shields.io/github/stars/cline/cline?style=flat-square&label=%E2%98%85)](https://github.com/cline/cline) | VS Code | Cline | Open-source agent interface. Reads/writes files and runs terminal commands via MCP. |
| 🟢 **[Roo Code](https://github.com/RooVetGit/Roo-Code)** <br> [![Stars](https://img.shields.io/github/stars/RooVetGit/Roo-Code?style=flat-square&label=%E2%98%85)](https://github.com/RooVetGit/Roo-Code) | VS Code | Roo Vet | Cline fork with specialized agent modes, prompt overrides, and MCP diagnostics. |
| 🟢 **[Cody](https://github.com/sourcegraph/cody)** <br> [![Stars](https://img.shields.io/github/stars/sourcegraph/cody?style=flat-square&label=%E2%98%85)](https://github.com/sourcegraph/cody) | VS Code, JetBrains, Neovim | Sourcegraph | Advanced semantic codebase search, code explanation, chat-with-docs. |
| 🟢 **[Amazon Q Developer](https://aws.amazon.com/q/developer/)** | VS Code, JetBrains | AWS | Autocomplete, security scans, legacy code translation, AWS cloud integrations. |
| 🟢 **[Supermaven](https://supermaven.com/)** | VS Code, JetBrains, Neovim | Supermaven | Ultra-low latency autocomplete, large 300,000 token context window. |
| 🟢 **[Codeium](https://codeium.com/)** | VS Code, JetBrains, Xcode, Neovim | Codeium | Free autocomplete, chat, semantic search, local index building. |
| 🟢 **[Double.bot](https://www.double.bot/)** | VS Code, JetBrains | Double | High-accuracy inline editing, codebase context parsing. |
| 🟢 **[Tabnine](https://www.tabnine.com/)** | VS Code, JetBrains, Eclipse | Tabnine | Secure autocomplete with local offline models or private cloud deployments. |
| 🟢 **[Bito](https://bito.ai/)** | VS Code, JetBrains | Bito | AI helper for unit test generation, security checking, and explaining code. |

---

## 🔌 Custom Agent Skills & Plugins
Reusable, structured skills and behavior overrides designed to teach coding agents (like Claude Code, Gemini CLI, Cline) how to interact with external tools and follow specific protocols.

| Skill / Plugin Repo | Creator | Description | Target Agent / Platform |
| :--- | :--- | :--- | :--- |
| **[Academic Research Skills](https://github.com/Imbad0202/academic-research-skills)** | Imbad0202 | Workflows for research, compilation, drafting, and reviewing papers. | Claude Code / General Agents |
| **[Agent Skills](https://github.com/addyosmani/agent-skills)** | Addy Osmani | Production-grade software engineering skills. | Generic / Claude Code, Gemini CLI |
| **[Andrej Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills)** | Multica AI | Claude Code behaviors derived from Karpathy's LLM coding pitfall observations. | Claude Code / CLAUDE.md |
| **[Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** | mukul975 | 817 structured cybersecurity skills for AI agents mapped to MITRE, NIST frameworks. | Claude Code / General Agents |
| **[Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)** | ComposioHQ | Curated list of awesome Claude Skills, resources, and tools. | Claude Code / General Agents |
| 🔴 **[Caveman](https://github.com/JuliusBrussee/caveman)** <br> [![Stars](https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat-square&label=%E2%98%85)](https://github.com/JuliusBrussee/caveman) | Julius Brussee | Token-saving skill that rewrites instructions into caveman talk. | Claude Code / General Agents |
| 🔴 **[ClawHub](https://github.com/openclaw/clawhub)** <br> [![Stars](https://img.shields.io/github/stars/openclaw/clawhub?style=flat-square&label=%E2%98%85)](https://github.com/openclaw/clawhub) | OpenClaw | Skill and plugin registry for OpenClaw agents. | OpenClaw |
| 🟡 **[DESIGN.md](https://github.com/google-labs-code/design.md)** <br> [![Stars](https://img.shields.io/github/stars/google-labs-code/design.md?style=flat-square&label=%E2%98%85)](https://github.com/google-labs-code/design.md) | google-labs-code | Format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a design system. | Generic / Coding Agents |
| 🔴 **[Graphify](https://github.com/safishamsi/graphify)** <br> [![Stars](https://img.shields.io/github/stars/safishamsi/graphify?style=flat-square&label=%E2%98%85)](https://github.com/safishamsi/graphify) | safishamsi | Turn code, schemas, scripts, docs, and media into queryable knowledge graphs. | Claude Code / Codex / Gemini CLI / Cursor |
| 🟡 **[gstack](https://github.com/garrytan/gstack)** <br> [![Stars](https://img.shields.io/github/stars/garrytan/gstack?style=flat-square&label=%E2%98%85)](https://github.com/garrytan/gstack) | Garry Tan | Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Doc Engineer, and QA. | Claude Code / CLAUDE.md |
| **[Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill)** | op7418 | AI-agent Skill for generating polished HTML slide decks with Swiss layouts. | Claude Code / Codex / General Agents |
| 🟢 **[jscpd](https://github.com/kucherenko/jscpd)** <br> [![Stars](https://img.shields.io/github/stars/kucherenko/jscpd?style=flat-square&label=%E2%98%85)](https://github.com/kucherenko/jscpd) | Andrey Kucherenko | Copy/paste detector for programming source code, AI-ready with token-efficient reporter and skill. | Generic / Coding Agents |
| **[Last 30 Days Skill](https://github.com/mvanhorn/last30days-skill)** | M. Van Horn | Scrapes and synthesizes web/forum summaries. | Claude Code / Generic Agents |
| **[Obsidian Skills](https://github.com/kepano/obsidian-skills)** | Kepano | Teaches agents to read Markdown, Bases, and JSON Canvas in Obsidian. | Obsidian / Generic Agents |
| 🟡 **[React Doctor](https://github.com/millionco/react-doctor)** <br> [![Stars](https://img.shields.io/github/stars/millionco/react-doctor?style=flat-square&label=%E2%98%85)](https://github.com/millionco/react-doctor) | Million.co | Catch and fix bad React code generated by AI agents. | Generic / Code Review Agents |
| 🟡 **[Superpowers](https://github.com/obra/superpowers)** <br> [![Stars](https://img.shields.io/github/stars/obra/superpowers?style=flat-square&label=%E2%98%85)](https://github.com/obra/superpowers) | Obra | An agentic skills framework & software development methodology that works. | Generic / Claude Code, Gemini CLI |
| **[Taste-Skill](https://github.com/Leonxlnx/taste-skill)** | Leonxlnx | Taste-Skill - gives your AI good taste, stopping boring and generic layout generation. | Claude Code / Codex |

---

## 🛡️ PII Masking & AI Agent Security Proxies
Middlewares and gatekeepers that intercept outgoing LLM requests to redact secrets, tokens, and Personally Identifiable Information (PII).

| Tool / Proxy | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[CodeGate](https://github.com/StacklokLabs/spring-ai-codegate-sample)** <br> [![Stars](https://img.shields.io/github/stars/StacklokLabs/spring-ai-codegate-sample?style=flat-square&label=%E2%98%85)](https://github.com/StacklokLabs/spring-ai-codegate-sample) | Stacklok | Privacy-first local proxy for IDE extensions/CLIs. | Detects/masks PII and API keys, warns of vulnerable packages, local decryption. |
| 🟡 **[9router](https://github.com/decolua/9router)** <br> [![Stars](https://img.shields.io/github/stars/decolua/9router?style=flat-square&label=%E2%98%85)](https://github.com/decolua/9router) | Decolua | Local proxy and router for AI tools. | Connects CLI agents to 40+ providers, automatic fallbacks, token compression. |
| 🔴 **[Clawshield](https://github.com/SleuthCo/clawshield-public)** <br> [![Stars](https://img.shields.io/github/stars/SleuthCo/clawshield-public?style=flat-square&label=%E2%98%85)](https://github.com/SleuthCo/clawshield-public) | SleuthCo | YAML-driven security gateway for dev agents. | Enforces prompt policies, logs outputs, filters outbound credentials. |
| 🔴 **[Kiji Proxy](https://github.com/dataiku/kiji-proxy)** <br> [![Stars](https://img.shields.io/github/stars/dataiku/kiji-proxy?style=flat-square&label=%E2%98%85)](https://github.com/dataiku/kiji-proxy) | Dataiku | Lightweight PII masking proxy. | Regular expression and NLP-based token masking. |
| 🟢 **[WitnessAI](https://witness.ai)** | WitnessAI | Enterprise-grade AI proxy firewall. | Granular policy configurations, real-time agent auditing, schema obscuring. |

---

## ⚙️ AI Agent Frameworks & Multi-Agent Platforms
Orchestration frameworks that allow developers to design, wire, and deploy complex autonomous agent teams.

| Framework | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟡 **[Agency Agents](https://github.com/msitarzewski/agency-agents)** <br> [![Stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=flat-square&label=%E2%98%85)](https://github.com/msitarzewski/agency-agents) | msitarzewski | Specialized expert agent pack for creative agencies. | Social media bots, copy editors, UX reviewers, community monitors. |
| 🟢 **[Agno](https://github.com/agno-agi/agno)** <br> [![Stars](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&label=%E2%98%85)](https://github.com/agno-agi/agno) | Agno AI | Open-source framework for building multi-modal agents. | Fast execution, built-in vector integrations, multi-modal support. |
| 🔴 **[AI Berkshire](https://github.com/xbtlin/ai-berkshire)** <br> [![Stars](https://img.shields.io/github/stars/xbtlin/ai-berkshire?style=flat-square&label=%E2%98%85)](https://github.com/xbtlin/ai-berkshire) | xbtlin | A value investing research framework built on Claude Code using multi-agent adversarial analysis. | Python / Claude Code |
| 🟡 **[AI Hedge Fund](https://github.com/virattt/ai-hedge-fund)** <br> [![Stars](https://img.shields.io/github/stars/virattt/ai-hedge-fund?style=flat-square&label=%E2%98%85)](https://github.com/virattt/ai-hedge-fund) | virattt | Simulated multi-agent hedge fund team. | Agent roles: market analyst, risk manager, portfolio optimizer, trader. |
| 🔴 **[AI Scientist v2](https://github.com/SakanaAI/AI-Scientist-v2)** <br> [![Stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat-square&label=%E2%98%85)](https://github.com/SakanaAI/AI-Scientist-v2) | SakanaAI | Fully automated scientific discovery agent. | Tree-search planning, paper writing, data generation, automated peer review. |
| 🟢 **[AutoGen](https://github.com/microsoft/autogen)** <br> [![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/autogen) | Microsoft | Multi-agent conversation framework. | Customizable agent personalities, human-in-the-loop, conversable structures. |
| 🟢 **[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)** <br> [![Stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=flat-square&label=%E2%98%85)](https://github.com/Significant-Gravitas/AutoGPT) | Significant Gravitas | One of the earliest autonomous agent projects. | Multi-agent pipelines, web search, memory integration. |
| 🔴 **[BabyAGI](https://github.com/yoheinakajima/babyagi)** <br> [![Stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=flat-square&label=%E2%98%85)](https://github.com/yoheinakajima/babyagi) | Yohei Nakajima | Lightweight task-driven agent loop. | Simple agent architecture utilizing vector databases and task management pools. |
| 🟢 **[CrewAI](https://github.com/crewAIInc/crewAI)** <br> [![Stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=flat-square&label=%E2%98%85)](https://github.com/crewAIInc/crewAI) | CrewAI Inc | Role-based agent teams orchestration. | Easy agent role-play definitions, task delegation, sequential or hierarchical execution. |
| 🔴 **[DeepAgents](https://github.com/langchain-ai/deepagents)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/deepagents) | LangChain AI | Batteries-included agent harness library. | Standard task interfaces, tool execution wrappers, built-in debug trackers. |
| 🔴 **[Deer Flow](https://github.com/bytedance/deer-flow)** <br> [![Stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=flat-square&label=%E2%98%85)](https://github.com/bytedance/deer-flow) | ByteDance | Long-horizon SuperAgent harness for automated research. | Deep memory architecture, sandboxed execution, goal decomposition. |
| 🔴 **[Dexter](https://github.com/virattt/dexter)** <br> [![Stars](https://img.shields.io/github/stars/virattt/dexter?style=flat-square&label=%E2%98%85)](https://github.com/virattt/dexter) | virattt | Autonomous agent for deep financial research. | Market scraping, portfolio modeling, automated report drafting. |
| 🔴 **[Generic Agent](https://github.com/lsdefine/GenericAgent)** <br> [![Stars](https://img.shields.io/github/stars/lsdefine/GenericAgent?style=flat-square&label=%E2%98%85)](https://github.com/lsdefine/GenericAgent) | lsdefine | Self-evolving AI agent with dynamic skill trees. | Seeded by a 3.3K line Python script, builds its own skills, low token overhead. |
| 🔴 **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** <br> [![Stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=flat-square&label=%E2%98%85)](https://github.com/NousResearch/hermes-agent) | Nous Research | An agent that learns and evolves its internal loop processes. | Self-correction heuristics, modular agent graph, adaptive tool binding. |
| 🟢 **[LangGraph](https://github.com/langchain-ai/langgraph)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/langgraph) | LangChain AI | Stateful multi-agent graph orchestrator. | Cycles, human-in-the-loop, structured state, production-ready. |
| 🟢 **[LobeHub](https://github.com/lobehub/lobehub)** <br> [![Stars](https://img.shields.io/github/stars/lobehub/lobehub?style=flat-square&label=%E2%98%85)](https://github.com/lobehub/lobehub) | LobeHub | Chief Agent Operator for organizing and scheduling multi-agent teams. | Multi-agent collaboration, 7x24 agent operations, deep client integration. |
| 🟢 **[MetaGPT](https://github.com/FoundationAgents/MetaGPT)** <br> [![Stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=flat-square&label=%E2%98%85)](https://github.com/FoundationAgents/MetaGPT) | FoundationAgents | Multi-agent framework mimicking software teams. | Simulates product managers, designers, and developers via SOPs. |
| 🔴 **[MiroFish](https://github.com/666ghj/MiroFish)** <br> [![Stars](https://img.shields.io/github/stars/666ghj/MiroFish?style=flat-square&label=%E2%98%85)](https://github.com/666ghj/MiroFish) | 666ghj | Swarm intelligence prediction engine. | Multi-node consensus, predictive optimization loops. |
| 🟡 **[Multica](https://github.com/multica-ai/multica)** <br> [![Stars](https://img.shields.io/github/stars/multica-ai/multica?style=flat-square&label=%E2%98%85)](https://github.com/multica-ai/multica) | Multica AI | Managed open-source agent platform. | Skill compounding, real-time progress logging, teammate assign systems. |
| 🔴 **[OpenMontage](https://github.com/calesthio/OpenMontage)** <br> [![Stars](https://img.shields.io/github/stars/calesthio/OpenMontage?style=flat-square&label=%E2%98%85)](https://github.com/calesthio/OpenMontage) | calesthio | Open-source agentic video production system with 12 pipelines, 52 tools, and 500+ agent skills. | Python / Video Generation |
| 🔴 **[Page Agent](https://github.com/alibaba/page-agent)** <br> [![Stars](https://img.shields.io/github/stars/alibaba/page-agent?style=flat-square&label=%E2%98%85)](https://github.com/alibaba/page-agent) | Alibaba | JavaScript in-page GUI agent that controls web interfaces with natural language. | TypeScript / Web GUI Control |
| 🟡 **[ruflo](https://github.com/ruvnet/ruflo)** <br> [![Stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=flat-square&label=%E2%98%85)](https://github.com/ruvnet/ruflo) | ruvnet | Leading agent meta-harness for Claude to deploy multi-agent swarms. | Swarm intelligence, adaptive memory, self-learning workflows, RAG integration. |
| 🟡 **[Sim](https://github.com/simstudioai/sim)** <br> [![Stars](https://img.shields.io/github/stars/simstudioai/sim?style=flat-square&label=%E2%98%85)](https://github.com/simstudioai/sim) | Sim Studio | Workforce agent management layer. | Integrates multi-agent tasks, live team logging, worker synchronization. |
| 🔴 **[TradingAgents](https://github.com/TauricResearch/TradingAgents)** <br> [![Stars](https://img.shields.io/github/stars/TauricResearch/TradingAgents?style=flat-square&label=%E2%98%85)](https://github.com/TauricResearch/TradingAgents) | TauricResearch | Multi-agent LLM financial trading framework. | Simulated trading environments, multi-agent portfolios. |

---

## 🛠️ LLM DevTools & Orchestration Infrastructure
Libraries, SDKs, parsers, and intelligence engines to manage data pipelines, structure outputs, and monitor production AI applications.

| Tool | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🔴 **[CodeGraph](https://github.com/colbymchenry/codegraph)** <br> [![Stars](https://img.shields.io/github/stars/colbymchenry/codegraph?style=flat-square&label=%E2%98%85)](https://github.com/colbymchenry/codegraph) | Colby McHenry | Pre-indexed local code knowledge graph. | Syncs automatically on git changes, exposes code indexes locally to avoid API calls. |
| 🟢 **[Dify](https://github.com/langgenius/dify)** <br> [![Stars](https://img.shields.io/github/stars/langgenius/dify?style=flat-square&label=%E2%98%85)](https://github.com/langgenius/dify) | LangGenius | Visual LLM app building and operations platform. | Workflow orchestrator, prompt engineering UI, vector db integrations, monitoring dashboards. |
| 🟢 **[Flowise](https://github.com/FlowiseAI/Flowise)** <br> [![Stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=flat-square&label=%E2%98%85)](https://github.com/FlowiseAI/Flowise) | FlowiseAI | Drag & drop UI for building LangChain/LlamaIndex apps. | Visual nodes, instant API endpoints, chat widget deployments. |
| 🔴 **[GitNexus](https://github.com/abhigyanpatwari/GitNexus)** <br> [![Stars](https://img.shields.io/github/stars/abhigyanpatwari/GitNexus?style=flat-square&label=%E2%98%85)](https://github.com/abhigyanpatwari/GitNexus) | Abhigyan Patwari | Client-side, zero-server repository intelligence engine. | Runs in-browser, maps code dependencies, outputs AI-friendly knowledge maps. |
| 🔴 **[Heretic](https://github.com/p-e-w/heretic)** <br> [![Stars](https://img.shields.io/github/stars/p-e-w/heretic?style=flat-square&label=%E2%98%85)](https://github.com/p-e-w/heretic) | p-e-w | Automatic model censorship removal tool. | Local model tuning layer, automated system alignment bypass. |
| 🟢 **[LangChain](https://github.com/langchain-ai/langchain)** <br> [![Stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%E2%98%85)](https://github.com/langchain-ai/langchain) | LangChain AI | De facto standard ecosystem for LLM orchestration. | Chains, prompts, data connectors, custom tool integrations, LangSmith observability. |
| 🟡 **[Lightpanda Browser](https://github.com/lightpanda-io/browser)** <br> [![Stars](https://img.shields.io/github/stars/lightpanda-io/browser?style=flat-square&label=%E2%98%85)](https://github.com/lightpanda-io/browser) | Lightpanda | Headless browser built in Zig for AI agents. | High-speed, lightweight DOM execution, optimal for sandboxed agent scraping. |
| 🟢 **[LlamaFactory](https://github.com/hiyouga/LlamaFactory)** <br> [![Stars](https://img.shields.io/github/stars/hiyouga/LlamaFactory?style=flat-square&label=%E2%98%85)](https://github.com/hiyouga/LlamaFactory) | hiyouga | Unified efficient fine-tuning framework for 100+ LLMs and VLMs. | Web UI dashboard, multi-GPU training support, RLHF/QLoRA methods. |
| 🟢 **[LlamaIndex](https://github.com/run-llama/llama_index)** <br> [![Stars](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&label=%E2%98%85)](https://github.com/run-llama/llama_index) | LlamaIndex | Data framework for LLM/RAG applications. | Data ingestors, indexing tools, structured queries, custom query engines. |
| 🟢 **[Mem0](https://github.com/mem0ai/mem0)** <br> [![Stars](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&label=%E2%98%85)](https://github.com/mem0ai/mem0) | Mem0 | Personalized memory layer for AI agents. | Remembers user preferences, updates context over time, optimizes personalization. |
| 🟢 **[MinerU](https://github.com/opendatalab/MinerU)** <br> [![Stars](https://img.shields.io/github/stars/opendatalab/MinerU?style=flat-square&label=%E2%98%85)](https://github.com/opendatalab/MinerU) | OpenDataLab | Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for agentic workflows. | High-precision PDF layout extraction, structural element recognition. |
| 🟢 **[n8n](https://github.com/n8n-io/n8n)** <br> [![Stars](https://img.shields.io/github/stars/n8n-io/n8n?style=flat-square&label=%E2%98%85)](https://github.com/n8n-io/n8n) | n8n-io | Fair-code workflow automation platform with native AI capabilities. | Visual workflow builder, 400+ integrations, native agent/subagent orchestration nodes. |
| 🔴 **[OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf)** <br> [![Stars](https://img.shields.io/github/stars/opendataloader-project/opendataloader-pdf?style=flat-square&label=%E2%98%85)](https://github.com/opendataloader-project/opendataloader-pdf) | OpenDataLoader | Open-source PDF parser optimized for LLM training. | High accuracy structure mapping, table extraction, cleans layout noise. |
| 🔴 **[OpenViking](https://github.com/volcengine/OpenViking)** <br> [![Stars](https://img.shields.io/github/stars/volcengine/OpenViking?style=flat-square&label=%E2%98%85)](https://github.com/volcengine/OpenViking) | Volcengine | Context database tailored for AI agents. | Persistent agent memory storage, runtime resource management, skill indexes. |
| 🟢 **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)** <br> [![Stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=flat-square&label=%E2%98%85)](https://github.com/PaddlePaddle/PaddleOCR) | PaddlePaddle | Document-to-text OCR parser. | Supports 100+ languages, extracts layout and tables from scanned documents. |

---

## 📡 Model Context Protocol (MCP) Servers
MCP is a protocol designed to connect LLMs to data, tools, filesystems, and external APIs. Exposes services to MCP-compliant agents (e.g. Gemini CLI, Claude Code, Cline).

| MCP Server | Creator | Description | Tools / Access Exposed |
| :--- | :--- | :--- | :--- |
| **[Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws)** | AWS | Official AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS. | AWS services access (S3, EC2, Bedrock, etc.) |
| 🟡 **[Claude Context MCP](https://github.com/zilliztech/claude-context)** <br> [![Stars](https://img.shields.io/github/stars/zilliztech/claude-context?style=flat-square&label=%E2%98%85)](https://github.com/zilliztech/claude-context) | Zilliz Tech | Vector search-based code search MCP server. | Code search over huge codebases, fast local similarity query tools. |
| 🔴 **[Context7](https://github.com/upstash/context7)** <br> [![Stars](https://img.shields.io/github/stars/upstash/context7?style=flat-square&label=%E2%98%85)](https://github.com/upstash/context7) | Upstash | Serverless state and tool cache. | Caches tool executions, manages state across agent handoffs. |
| **[GitHub MCP Server](https://github.com/github/github-mcp-server)** | GitHub | Official GitHub API bridge. | Lists issues, manages PRs, commits changes, searches repositories. |
| **[MCP Servers Repo](https://github.com/modelcontextprotocol/servers)** | Anthropic | Standard repository of reference MCP servers. | Postgres, SQLite, Slack, GitHub, Puppeteer, Brave Search. |
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
| 🟢 **[Milvus](https://github.com/milvus-io/milvus)** <br> [![Stars](https://img.shields.io/github/stars/milvus-io/milvus?style=flat-square&label=%E2%98%85)](https://github.com/milvus-io/milvus) | Milvus | High-performance, distributed vector database. | Built for billion-scale datasets, GPU indexing, hybrid search support. |
| 🟢 **[Qdrant](https://github.com/qdrant/qdrant)** <br> [![Stars](https://img.shields.io/github/stars/qdrant/qdrant?style=flat-square&label=%E2%98%85)](https://github.com/qdrant/qdrant) | Qdrant | Rust-based vector similarity search engine. | Fast payload filtering, REST/gRPC interfaces, production scale. |

---

## 🎨 Vibe Coding & Generative UI Tools
Tools designed to let non-technical users or visual developers generate layouts, notes, and whole apps using AI natural language ("vibe coding").

| Tool | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[AFFiNE](https://github.com/toeverything/AFFiNE)** <br> [![Stars](https://img.shields.io/github/stars/toeverything/AFFiNE?style=flat-square&label=%E2%98%85)](https://github.com/toeverything/AFFiNE) | toeverything | Workspace tool unifying notes, tasks, and graphics. | AI-native drawing, structured page layout generation. |
| 🔴 **[AI Website Cloner Template](https://github.com/JCodesMore/ai-website-cloner-template)** <br> [![Stars](https://img.shields.io/github/stars/JCodesMore/ai-website-cloner-template?style=flat-square&label=%E2%98%85)](https://github.com/JCodesMore/ai-website-cloner-template) | JCodesMore | Clone any website with one command using AI coding agents. | TypeScript / Website cloning |
| 🟢 **[Chatbot UI](https://github.com/mckaywrigley/chatbot-ui)** <br> [![Stars](https://img.shields.io/github/stars/mckaywrigley/chatbot-ui?style=flat-square&label=%E2%98%85)](https://github.com/mckaywrigley/chatbot-ui) | McKay Wrigley | A clean, customizable front-end for LLM APIs. | Custom prompt templates, system instructions, attachment parsing. |
| 🔴 **[NanoChat](https://github.com/karpathy/nanochat)** <br> [![Stars](https://img.shields.io/github/stars/karpathy/nanochat?style=flat-square&label=%E2%98%85)](https://github.com/karpathy/nanochat) | Andrej Karpathy | Minimalist ChatGPT clone. | Simple code, easily extensible, fast API connections. |
| 🟢 **[Onyx](https://github.com/onyx-dot-app/onyx)** <br> [![Stars](https://img.shields.io/github/stars/onyx-dot-app/onyx?style=flat-square&label=%E2%98%85)](https://github.com/onyx-dot-app/onyx) | Onyx App | Open source chat platform designed for multiple LLMs. | Advanced chat options, workspace customization. |
| 🟡 **[OpenUI](https://github.com/wandb/openui)** <br> [![Stars](https://img.shields.io/github/stars/wandb/openui?style=flat-square&label=%E2%98%85)](https://github.com/wandb/openui) | Weights & Biases | Generates responsive HTML/CSS layouts visually from description. | Direct Tailwind/React component export, interactive design editor. |
| 🔴 **[Thunderbolt](https://github.com/thunderbird/thunderbolt)** <br> [![Stars](https://img.shields.io/github/stars/thunderbird/thunderbolt?style=flat-square&label=%E2%98%85)](https://github.com/thunderbird/thunderbolt) | Thunderbird | Personal client for running customizable AI models. | Local data control, no vendor lock-in UI. |

---

## 📖 AI Learning & Educational Resources
Structured courses, notebooks, and reference materials designed to teach developers how to design neural networks and build AI agents from scratch.

| Resource | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| 🟢 **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** <br> [![Stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/ai-agents-for-beginners) | Microsoft | 12-lesson roadmap for learning to build AI agents. | Structured lectures, notebook labs, tool-calling and planning basics. |
| 🟡 **[Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice)** <br> [![Stars](https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat-square&label=%E2%98%85)](https://github.com/shanraisshan/claude-code-best-practice) | shanraisshan | Guidelines and tips for transition from vibe coding to agentic engineering with Claude Code. | Structured best practices, prompt optimization, workflow patterns. |
| 🟡 **[Learn Claude Code](https://github.com/shareAI-lab/learn-claude-code)** <br> [![Stars](https://img.shields.io/github/stars/shareAI-lab/learn-claude-code?style=flat-square&label=%E2%98%85)](https://github.com/shareAI-lab/learn-claude-code) | shareAI-lab | Educational nano-agent tutorial showing how to build a Claude Code-like harness from scratch. | Code walkthroughs, lightweight bash-to-LLM bindings, agentic tutorials. |
| 🟡 **[Modded NanoGPT](https://github.com/KellerJordan/modded-nanogpt)** <br> [![Stars](https://img.shields.io/github/stars/KellerJordan/modded-nanogpt?style=flat-square&label=%E2%98%85)](https://github.com/KellerJordan/modded-nanogpt) | Keller Jordan | Extremely fast, modified NanoGPT training repo. | Achieves 124M parameter training in 90 seconds, showcases optimization. |
| 🟢 **[Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)** <br> [![Stars](https://img.shields.io/github/stars/karpathy/nn-zero-to-hero?style=flat-square&label=%E2%98%85)](https://github.com/karpathy/nn-zero-to-hero) | Andrej Karpathy | Detailed guide to building neural networks from scratch. | From basic backpropagation to GPT, PyTorch labs, video lecture companion. |
| **[Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** | DAIR.AI | Curated guides, papers, notebooks, and learning paths for prompt/context engineering and AI agents. | Structured papers index, learning materials, system prompt models. |
| 🟢 **[Unsloth](https://github.com/unslothai/unsloth)** <br> [![Stars](https://img.shields.io/github/stars/unslothai/unsloth?style=flat-square&label=%E2%98%85)](https://github.com/unslothai/unsloth) | Unsloth AI | Web UI and training environment for fine-tuning open weights models. | 2x-5x faster model training, lightweight local setup (Gemma, Qwen, DeepSeek). |

---

## 📊 Quick Comparison Matrix

| Tool | Category | Licensing | Primary Language / Stack | Best Suited For... |
| :--- | :--- | :--- | :--- | :--- |
| **[Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws)** | MCP Server | Apache-2.0 | Python | Exposing AWS services securely to coding agents via MCP |
| **Antigravity CLI** | CLI Agent | Proprietary | Python / CLI | Sandboxed multi-agent and browser-based test loops |
| **Claude Code** | CLI Agent | Proprietary | TypeScript / Node.js | Multi-file codebase adjustments using Claude |
| **CodeGate** | Security Proxy | Apache-2.0 | Go / Rust | Masking secrets and PII from outgoing LLM traffic |
| **CrewAI** | Agent Framework | MIT | Python | Role-based agent teams mimicking human software processes |
| **Cursor** | Native IDE | Proprietary | VS Code Fork | The most polished, complete AI-native coding environment |
| **Gemini CLI** | CLI Agent | MIT | TypeScript / Node.js | Fast, tool-equipped CLI coding using Google Gemini models |
| **Goose** | CLI Agent | Apache-2.0 | Rust / Python | Executing task checklists with MCP plugins |
| **gstack** | Custom Skill Pack | MIT | TypeScript | Opinionated agent roles (CEO, Designer, Doc Engineer) for Claude Code |
| **LangGraph** | Agent Framework | MIT | Python / JS | Custom stateful multi-agent workflows and graph logic |
| **Ollama** | Serving Engine | MIT | Go / C++ | Running and exposing open-weights models locally |
| **OpenHands** | CLI Agent / Web | Apache-2.0 | Python / Docker | Isolated container-level SWE benchmarks and repairs |

---

## 🤝 Contributing

We welcome contributions! If you would like to add a new tool, extension, proxy, plugin, or CLI agent:

1. Fork this repository.
2. Add the tool to the appropriate table in alphabetical order.
3. Submit a Pull Request with a clear description of the tool.
