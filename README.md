# Awesome AI Coding Tools & Agents 🚀

A curated list of awesome AI coding assistants, autonomous agents, AI-native IDEs, extensions, security proxies, and development frameworks. Designed to help developers find the right tooling for their workflow, from autocomplete extensions to fully autonomous terminal agents.

---

## 📂 Table of Contents
- [🤖 AI Coding CLI Agents](#-ai-coding-cli-agents)
- [🛡️ PII & Security Proxies for AI Agents](#️-pii--security-proxies-for-ai-agents)
- [💻 AI-Native IDEs & Workspaces](#-ai-native-ides--workspaces)
- [🧩 AI Coding Extensions & Plugins](#-ai-coding-extensions--plugins)
- [📊 Quick Comparison Matrix](#-quick-comparison-matrix)
- [🤝 Contributing](#-contributing)

---

## 🤖 AI Coding CLI Agents
CLI agents run directly inside your terminal, executing shell commands, reading/writing files, running tests, diagnosing compiler/interpreter errors, and managing Git changes autonomously.

| Agent | Creator / Repository | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** | Google Gemini | An open-source, terminal-first AI agent powered by Gemini. | ReAct loops, Model Context Protocol (MCP) support, Google search grounding, local tool execution, GitHub Actions integration. |
| **[Claude Code](https://github.com/anthropics/claude-code)** | Anthropic | Command-line agent powered by Claude. | Deep codebase reasoning, up to 1M token context, agentic terminal loops, interactive multi-file editing. |
| **[Antigravity CLI](https://github.com/google-deepmind/antigravity)** | Google DeepMind | Advanced agentic CLI pair programmer. | Parallel subagent orchestration, automated testing, built-in browser sandboxing, Google ecosystem integration. |
| **[OpenCode](https://github.com/anomalyco/opencode)** | Anomaly | An open-source, model-agnostic coding agent. | TUI support, 75+ model providers supported, LSP diagnostics, git-based snapshot recovery, command workflows. |
| **[OpenAI Codex CLI / Codex](https://github.com/openai/openai-cookbook)** | OpenAI | Terminal-based interfaces utilizing OpenAI models. | Fast code generation, scripting, API-driven terminal workflows, sandboxed shell execution. |
| **[Pi Agent](https://github.com/earendil-works/pi)** | Earendil Works | A terminal-first AI agent toolkit and harness. | Unified LLM API, agent loop, interactive TUI, session persistence, modular tool architecture. |
| **[Oh My Pi](https://github.com/can1357/oh-my-pi)** | can1357 | A terminal-native AI coding agent with advanced tool harness. | Hash-anchored edits, LSP integration, browser automation, subagent delegation. |
| **[Aider](https://github.com/aider-chat/aider)** | Aider-chat | Terminal-based pair programmer that works with local & cloud LLMs. | Git-aware, edits multiple files, automatic commit generation, test-driven coding support. |
| **[SWE-agent](https://github.com/princeton-nlp/SWE-agent)** | Princeton NLP | An agentic framework that turns LLMs into software engineering agents. | Custom Agent-Computer Interface (ACI), runs inside secure Docker containers, highly successful on SWE-bench. |
| **[OpenDevin / All-Hands](https://github.com/All-Hands-AI/OpenDevin)** | All-Hands AI | An open-source autonomous agent designed to solve complex software engineering tasks. | Sandboxed execution (Docker), agentic planning, multi-file workspace editing, web-browsing capabilities. |
| **[Plandex](https://github.com/plandex-ai/plandex)** | Plandex AI | Terminal-based AI agent designed to manage large tasks across multiple files. | Sandboxed editing, robust branch management, handles complex tasks step-by-step. |
| **[Mentat](https://github.com/ggarrett8/mentat)** | Mentat | Command-line AI coding assistant that coordinates directly with your codebase context. | High-speed diff edits, interactive command loop, customized file indexing. |
| **[GPT-Engineer](https://github.com/gpt-engineer-org/gpt-engineer)** | GPT-Engineer Org | CLI tool that builds entire codebases from a single text prompt. | Multi-file code generation, modular framework setup, interactive prompt clarification. |
| **[Sweep](https://github.com/sweepai/sweep)** | Sweep AI | GitHub-native CLI / integration agent that turns issues into Pull Requests. | Auto-linting, automatic tests, code search, GitHub Action triggers. |
| **[Devika](https://github.com/mufeedvh/devika)** | Mufeed VH | Open-source agentic coder inspired by Cognition's Devin. | Web research, code writing, planning, auto-execution of code, multi-agent structure. |

---

## 🛡️ PII & Security Proxies for AI Agents
Since AI agents operate with direct codebase and terminal access, security proxies are essential to prevent Personally Identifiable Information (PII), secrets, and sensitive tokens from leaking to cloud LLMs.

| Tool / Proxy | Creator / Project | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[CodeGate](https://github.com/StacklokLabs/spring-ai-codegate-sample)** | Stacklok | Privacy-respecting proxy sitting between IDE/CLI and the AI provider. | Intercepts requests, redacts PII and secrets, detects vulnerable packages, decrypts/re-injects variables locally. |
| **[Clawshield](https://github.com/SleuthCo/clawshield-public)** | SleuthCo | Security proxy specifically tailored for developer agents. | YAML-based policy engines, tokenization of sensitive credentials, request auditing. |
| **[Kiji Proxy](https://github.com/dataiku/kiji-proxy)** | Dataiku | Privacy proxy to mask PII in AI requests. | Configurable regex/NLP mapping, token hashing, lightweight middleware execution. |
| **[WitnessAI](https://witness.ai)** | WitnessAI | Enterprise-grade governance and data loss prevention (DLP) for AI. | Deep policy enforcement, real-time agent auditing, sensitive database schema masking. |

---

## 💻 AI-Native IDEs & Workspaces
Standalone applications or highly integrated coding environments designed to put AI agents at the center of the user experience.

| IDE / Workspace | Creator / Project | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[Cursor](https://www.cursor.com/)** | Anysphere | VS Code fork that acts as the leading AI-native code editor. | "Composer" (multi-file edit agent), tab-autocomplete, chat-with-codebase, inline edits. |
| **[Windsurf](https://codeium.com/windsurf)** | Codeium | VS Code based editor focused on deep collaborative agentic loops. | "Windsurf Flow" (seamless agent collaboration), fast index systems, multi-file context tracking. |
| **[PearAI](https://trypear.ai/)** | PearAI | An open-source, user-centric AI code editor forked from VS Code. | Built-in chat, inline refactoring, transparent usage tracking, completely open source. |
| **[Zed AI](https://zed.dev/ai)** | Zed Decent | A high-performance, GPU-accelerated code editor with first-class AI integration. | Built-in Anthropic/OpenAI integrations, collaborative coding, multi-buffer edits, instant startup. |
| **[Project IDX](https://idx.dev/)** | Google | Browser-based workspace built on Visual Studio Code for multiplatform app development. | Integrated Gemini assistant, pre-configured environments, cloud emulator previews. |
| **[Melty](https://github.com/melty-labs/melty)** | Melty Labs | Open-source AI IDE that watches your coding patterns and automates tasks. | Git-aware changes, automated refactoring, codebase change tracing. |
| **[GitHub Copilot Workspace](https://github.com/features/copilot)** | GitHub / Microsoft | A task-centric workspace designed to plan and implement changes in repository issues. | Interactive task list generation, step-by-step code plan, integrated cloud environment. |
| **[Replit Agent](https://replit.com)** | Replit | Cloud-native agent that writes, runs, and deploys applications directly inside the browser. | Full-stack generation, instant deployments, interactive terminal & UI output. |

---

## 🧩 AI Coding Extensions & Plugins
Extensions that integrate directly into popular editors (VS Code, JetBrains, Neovim) to augment your existing coding workflow.

| Extension | Platform Support | Creator | Description / Key Features |
| :--- | :--- | :--- | :--- |
| **[GitHub Copilot](https://github.com/features/copilot)** | VS Code, JetBrains, Visual Studio, Neovim | GitHub | Autocomplete, chat, pull request summaries, multi-line snippet generation. |
| **[Continue](https://github.com/continuedev/continue)** | VS Code, JetBrains | Continue | Open-source, model-agnostic extension. Connects to any local (Ollama) or cloud LLM. |
| **[Cline](https://github.com/cline/cline)** | VS Code | Cline | Open-source agent extension. Utilizes MCP to read/write files and execute terminal commands. |
| **[Roo Code](https://github.com/RooVetGit/Roo-Code)** | VS Code | Roo Vet | Advanced fork of Cline with custom system prompt overrides, agent modes, and enhanced MCP. |
| **[Cody](https://github.com/sourcegraph/cody)** | VS Code, JetBrains, Neovim | Sourcegraph | Codebase search, repository-wide indexing, code explanations. |
| **[Amazon Q Developer](https://aws.amazon.com/q/developer/)** | VS Code, JetBrains | AWS | Formerly CodeWhisperer. Deep integration with AWS APIs, cloud infrastructure suggestions, and security scanning. |
| **[Supermaven](https://supermaven.com/)** | VS Code, JetBrains, Neovim | Supermaven | Extremely fast autocomplete with a massive 300,000-token context window. |
| **[Codeium](https://codeium.com/)** | VS Code, JetBrains, Chrome, Neovim | Codeium | Free autocomplete and chat, codebase search, fast indexing. |
| **[Double.bot](https://www.double.bot/)** | VS Code, JetBrains | Double | Context-rich autocomplete and multi-file code execution extension. |
| **[Tabnine](https://www.tabnine.com/)** | VS Code, JetBrains, Eclipse | Tabnine | Secure assistant with options for local execution and enterprise privacy. |
| **[Bito](https://bito.ai/)** | VS Code, JetBrains | Bito | AI assistant for generating tests, explaining code, and checking security vulnerabilities. |

---

## 📊 Quick Comparison Matrix

| Tool | Primary Form Factor | Open Source? | Local Model Support? | PII / Secrets Protection |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini CLI** | CLI Agent | Yes | Yes | Via custom MCP tools / proxy wrappers |
| **Claude Code** | CLI Agent | No | No | Built-in warnings, compatible with proxies |
| **Antigravity CLI** | CLI Agent | Yes | Yes | Local environment variable encryption |
| **OpenCode** | CLI Agent / TUI | Yes | Yes | Local model mode preserves all code locally |
| **SWE-agent** | CLI Agent / Framework | Yes | Yes | Isolated container prevents host network leakage |
| **Cursor** | IDE | No | Partial | Privacy Mode toggles data opt-out |
| **Continue** | Extension | Yes | Yes | Local/Ollama integration ensures absolute privacy |
| **CodeGate** | Security Proxy | Yes | Yes | Native PII & Secret Redaction (Local decryption) |
| **GitHub Copilot** | Extension | No | No | Enterprise policy controls for code exclusion |

---

## 🤝 Contributing

We welcome contributions! If you would like to add a new tool, extension, proxy, plugin, or CLI agent:

1. Fork this repository.
2. Add the tool to the appropriate table in alphabetical order.
3. Submit a Pull Request with a clear description of the tool.
