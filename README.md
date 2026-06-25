# Awesome AI Coding Tools, IDEs & Agents 🚀

A curated, comprehensive list of awesome AI coding tools, autonomous agents, AI-native IDEs, extensions, LLM orchestrators, inference engines, vector databases, MCP servers, and security proxies. Organized to help developers find the right tools for building AI-powered systems or accelerating their engineering workflows.

---

## 📂 Table of Contents
- [🤖 AI Coding CLI Agents & SWE Systems](#-ai-coding-cli-agents--swe-systems)
- [💻 AI-Native IDEs & Cloud Workspaces](#-ai-native-ides--cloud-workspaces)
- [🧩 AI Coding Extensions & Plugins](#-ai-coding-extensions--plugins)
- [🛡️ PII Masking & AI Agent Security Proxies](#️-pii-masking--ai-agent-security-proxies)
- [⚙️ AI Agent Frameworks & Multi-Agent Platforms](#️-ai-agent-frameworks--multi-agent-platforms)
- [🛠️ LLM DevTools & Orchestration Infrastructure](#️-llm-devtools--orchestration-infrastructure)
- [🔌 Model Context Protocol (MCP) Servers](#-model-context-protocol-mcp-servers)
- [⚡ LLM Inference & Local Serving Engines](#-llm-inference--local-serving-engines)
- [🗄️ Vector Databases & Vector Stores](#️-vector-databases--vector-stores)
- [🎨 Vibe Coding & Generative UI Tools](#-vibe-coding--generative-ui-tools)
- [📊 Quick Comparison Matrix](#-quick-comparison-matrix)
- [🤝 Contributing](#-contributing)

---

## 🤖 AI Coding CLI Agents & SWE Systems
Autonomous CLI-first software engineering agents that can write code, run commands, execute tests, manage git changes, and solve issues.

| Repository / Agent | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** | Google Gemini | Open-source, terminal-first AI agent powered by Gemini. | ReAct loops, MCP server compatibility, Google Search grounding, git workflows. |
| **[Claude Code](https://github.com/anthropics/claude-code)** | Anthropic | Command-line agent powered by Claude models. | 1M+ token context window, deep reasoning, multi-file code workspace editing. |
| **[Antigravity CLI](https://github.com/google-deepmind/antigravity)** | Google DeepMind | Advanced agentic CLI pair programmer. | Parallel subagent orchestration, sandboxed browser testing, deep git integration. |
| **[Goose](https://github.com/block/goose)** | Block | Extensible open-source coding agent. | Local or desktop run modes, built-in MCP client, custom developer plugins. |
| **[OpenCode](https://github.com/anomalyco/opencode)** | Anomaly | Model-agnostic terminal developer agent. | Go-based TUI, 75+ LLM providers supported, LSP diagnostics, version control snapshots. |
| **[Aider](https://github.com/aider-chat/aider)** | Aider-chat | Git-integrated terminal pair programmer. | Edits files in-place, writes automatic git commits, works with local/remote LLMs. |
| **[OpenHands (formerly OpenDevin)](https://github.com/All-Hands-AI/OpenHands)** | All-Hands AI | Docker-sandboxed autonomous coding agent. | Runs shell commands, browses the web, reads/writes code inside isolated containers. |
| **[SWE-agent](https://github.com/princeton-nlp/SWE-agent)** | Princeton NLP | Agent-Computer Interface (ACI) coder framework. | Top SWE-bench performer, optimized file editing and search tools for LLMs. |
| **[Pi Agent](https://github.com/earendil-works/pi)** | Earendil Works | Modular coding agent harness and TUI. | LLM connection wrapper, task state persistence, modular CLI tools. |
| **[Oh My Pi](https://github.com/can1357/oh-my-pi)** | can1357 | High-performance terminal AI pair programmer. | Hash-anchored line diffing, LSP checking, subagent spawns. |
| **[Plandex](https://github.com/plandex-ai/plandex)** | Plandex AI | Large-task codebase editor. | Sandboxed file staging, handles massive refactoring pipelines. |
| **[Mentat](https://github.com/ggarrett8/mentat)** | Mentat | Context-aware codebase editor. | Customized file indexing, fast command loop, interactive diff views. |
| **[GPT-Engineer](https://github.com/gpt-engineer-org/gpt-engineer)** | GPT-Engineer Org | Full codebase generator from prompts. | Generates complete frameworks, interactive query staging. |
| **[Sweep](https://github.com/sweepai/sweep)** | Sweep AI | GitHub issue solver bot. | Automatic PR creation, lint fixing, and CI/CD validation. |
| **[Devika](https://github.com/mufeedvh/devika)** | Mufeed VH | Open-source clone of Cognition's Devin. | Plan-execute-monitor coding loops, agentic browser search. |
| **[OpenAI Codex CLI](https://github.com/openai/openai-cookbook)** | OpenAI | Basic terminal execution wrappers for Codex/GPT-4. | Script writing, direct terminal-based shell translations. |

---

## 💻 AI-Native IDEs & Cloud Workspaces
Integrated Development Environments (IDEs) built with AI agents at the center of the coding workflow.

| Editor / Workspace | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[Cursor](https://www.cursor.com/)** | Anysphere | Leading VS Code fork with deep AI integration. | "Composer" multi-file agent, autocomplete, inline codebase chat, custom index. |
| **[Windsurf](https://codeium.com/windsurf)** | Codeium | Agent-first IDE based on VS Code. | "Windsurf Flow" collaborative loops, fast indexing, persistent codebase context. |
| **[PearAI](https://trypear.ai/)** | PearAI | Fully open-source VS Code fork. | Custom assistant panel, inline refactoring, privacy controls. |
| **[Zed AI](https://zed.dev/ai)** | Zed Decent | High-performance, collaborative rust-based IDE. | Multi-buffer editing, instant startup, inline LLM chats (OpenAI/Anthropic). |
| **[Project IDX](https://idx.dev/)** | Google | Cloud-based developer workspace. | Multiplatform templates, integrated Gemini chat, device emulators. |
| **[Melty](https://github.com/melty-labs/melty)** | Melty Labs | Open-source IDE that learns from developers. | Tracks git actions, code pattern indexing, smart autocompletion. |
| **[GitHub Copilot Workspace](https://github.com/features/copilot)** | GitHub / Microsoft | Task-centric cloud workspace. | Interactive issue plans, automated task lists, instant sandbox edits. |
| **[Replit Agent](https://replit.com)** | Replit | Browser-based full-stack developer agent. | App creation, instant DB setup, one-click deployments. |

---

## 🧩 AI Coding Extensions & Plugins
Augmentative extensions to supercharge traditional IDEs (VS Code, JetBrains, Neovim).

| Extension | Platform Support | Creator | Description / Key Features |
| :--- | :--- | :--- | :--- |
| **[GitHub Copilot](https://github.com/features/copilot)** | VS Code, JetBrains, Visual Studio, Neovim | GitHub | Fast autocomplete, chat panels, codebase indexing, PR description generator. |
| **[Continue](https://github.com/continuedev/continue)** | VS Code, JetBrains | Continue | Open-source, model-agnostic extension. Connects to Ollama (local) or API keys. |
| **[Cline](https://github.com/cline/cline)** | VS Code | Cline | Open-source agent interface. Reads/writes files and runs terminal commands via MCP. |
| **[Roo Code](https://github.com/RooVetGit/Roo-Code)** | VS Code | Roo Vet | Cline fork with specialized agent modes, prompt overrides, and MCP diagnostics. |
| **[Cody](https://github.com/sourcegraph/cody)** | VS Code, JetBrains, Neovim | Sourcegraph | Advanced semantic codebase search, code explanation, chat-with-docs. |
| **[Amazon Q Developer](https://aws.amazon.com/q/developer/)** | VS Code, JetBrains | AWS | Autocomplete, security scans, legacy code translation, AWS cloud integrations. |
| **[Supermaven](https://supermaven.com/)** | VS Code, JetBrains, Neovim | Supermaven | Ultra-low latency autocomplete, large 300,000 token context window. |
| **[Codeium](https://codeium.com/)** | VS Code, JetBrains, Xcode, Neovim | Codeium | Free autocomplete, chat, semantic search, local index building. |
| **[Double.bot](https://www.double.bot/)** | VS Code, JetBrains | Double | High-accuracy inline editing, codebase context parsing. |
| **[Tabnine](https://www.tabnine.com/)** | VS Code, JetBrains, Eclipse | Tabnine | Secure autocomplete with local offline models or private cloud deployments. |
| **[Bito](https://bito.ai/)** | VS Code, JetBrains | Bito | AI helper for unit test generation, security checking, and explaining code. |

---

## 🛡️ PII Masking & AI Agent Security Proxies
Middlewares and gatekeepers that intercept outgoing LLM requests to redact secrets, tokens, and Personally Identifiable Information (PII).

| Tool / Proxy | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[CodeGate](https://github.com/StacklokLabs/spring-ai-codegate-sample)** | Stacklok | Privacy-first local proxy for IDE extensions/CLIs. | Detects/masks PII and API keys, warns of vulnerable packages, local decryption. |
| **[Clawshield](https://github.com/SleuthCo/clawshield-public)** | SleuthCo | YAML-driven security gateway for dev agents. | Enforces prompt policies, logs outputs, filters outbound credentials. |
| **[Kiji Proxy](https://github.com/dataiku/kiji-proxy)** | Dataiku | Lightweight PII masking proxy. | Regular expression and NLP-based token masking. |
| **[WitnessAI](https://witness.ai)** | WitnessAI | Enterprise-grade AI proxy firewall. | Granular policy configurations, real-time agent auditing, schema obscuring. |

---

## ⚙️ AI Agent Frameworks & Multi-Agent Platforms
Orchestration frameworks that allow developers to design, wire, and deploy complex autonomous agent teams.

| Framework | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)** | Significant Gravitas | One of the earliest autonomous agent projects. | Multi-agent pipelines, web search, memory integration. |
| **[LangGraph](https://github.com/langchain-ai/langgraph)** | LangChain AI | Stateful multi-agent graph orchestrator. | Cycles, human-in-the-loop, structured state, production-ready. |
| **[AutoGen](https://github.com/microsoft/autogen)** | Microsoft | Multi-agent conversation framework. | Customizable agent personalities, human-in-the-loop, conversable structures. |
| **[CrewAI](https://github.com/crewAIInc/crewAI)** | CrewAI Inc | Role-based agent teams orchestration. | Easy agent role-play definitions, task delegation, sequential or hierarchical execution. |
| **[MetaGPT](https://github.com/FoundationAgents/MetaGPT)** | FoundationAgents | Multi-agent framework mimicking software teams. | Simulates product managers, designers, and developers via standardized SOPs. |
| **[BabyAGI](https://github.com/yoheinakajima/babyagi)** | Yohei Nakajima | Lightweight task-driven agent loop. | Simple agent architecture utilizing vector databases and task management pools. |
| **[Agno](https://github.com/agno-agi/agno)** | Agno AI | Open-source framework for building multi-modal agents. | Fast execution, built-in vector integrations, multi-modal support. |

---

## 🛠️ LLM DevTools & Orchestration Infrastructure
Libraries and SDKs to manage data pipelines, chain prompts, structure outputs, and monitor production AI applications.

| Tool | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[LangChain](https://github.com/langchain-ai/langchain)** | LangChain AI | De facto standard ecosystem for LLM orchestration. | Chains, prompts, data connectors, custom tool integrations, LangSmith observability. |
| **[Dify](https://github.com/langgenius/dify)** | LangGenius | Visual LLM app building and operations platform. | Workflow orchestrator, prompt engineering UI, vector db integrations, monitoring dashboards. |
| **[LlamaIndex](https://github.com/run-llama/llama_index)** | LlamaIndex | Data framework for LLM/RAG applications. | Data ingestors, indexing tools, structured queries, custom query engines. |
| **[Flowise](https://github.com/FlowiseAI/Flowise)** | FlowiseAI | Drag & drop UI for building LangChain/LlamaIndex apps. | Visual nodes, instant API endpoints, chat widget deployments. |
| **[Mem0](https://github.com/mem0ai/mem0)** | Mem0 | Personalized memory layer for AI agents. | Remembers user preferences, updates context over time, optimizes personalization. |

---

## 🔌 Model Context Protocol (MCP) Servers
MCP is a protocol designed to connect LLMs to data, tools, filesystems, and external APIs. These servers expose local or remote systems to MCP-compliant agents (e.g. Gemini CLI, Claude Code, Cline).

| MCP Server | Creator | Description | Tools / Access Exposed |
| :--- | :--- | :--- | :--- |
| **[MCP Servers Repo](https://github.com/modelcontextprotocol/servers)** | Anthropic | Standard repository of reference MCP servers. | Postgres, SQLite, Slack, GitHub, Puppeteer, Brave Search. |
| **[Context7](https://github.com/upstash/context7)** | Upstash | Serverless state and tool cache. | Caches tool executions, manages state across agent handoffs. |
| **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** | Microsoft | Browser automation server. | Exposes headless browser actions (navigate, click, type, screenshot). |
| **[GitHub MCP Server](https://github.com/github/github-mcp-server)** | GitHub | Official GitHub API bridge. | Lists issues, manages PRs, commits changes, searches repositories. |

---

## ⚡ LLM Inference & Local Serving Engines
Engines designed to run, serve, and perform inference with large language models locally or in private clouds.

| Engine | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[Ollama](https://github.com/ollama/ollama)** | Ollama | Package and run LLMs locally on macOS, Linux, and Windows. | Simple CLI, one-line installs (Llama 3, Phi, Qwen), OpenAI compatible API. |
| **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | GGML Org | High-performance inference engine in C/C++. | CPU/GPU execution, low memory overhead, broad hardware support. |
| **[vLLM](https://github.com/vllm-project/vllm)** | vLLM Project | High-throughput, memory-efficient LLM serving engine. | PagedAttention, continuous batching, distributed inference, serving API. |
| **[GPT4All](https://github.com/nomic-ai/gpt4all)** | Nomic AI | Desktop app and SDK for local LLM execution. | Runs locally on consumer GPUs/CPUs, built-in search/document RAG capabilities. |
| **[LocalAI](https://github.com/mudler/LocalAI)** | mudler | Drop-in OpenAI replacement for local models. | Supports audio generation, images, embedding, and text models. |
| **[Text-generation-webui](https://github.com/oobabooga/text-generation-webui)** | oobabooga | Gradio web UI for running local models. | Supports transformers, llama.cpp, ExLlamaV2, custom parameter sliders. |
| **[Llamafile](https://github.com/Mozilla-Ocho/llamafile)** | Mozilla Ocho | Single-file executable for local LLMs. | Runs across 6 OS platforms without installations, fast CPU execution. |
| **[SGLang](https://github.com/sgl-project/sglang)** | SGLang Project | Structured generation language & engine. | High throughput serving, prompt caching, JSON schema constraints. |

---

## 🗄️ Vector Databases & Vector Stores
Specialized databases built to index, store, and query high-dimensional embeddings for RAG and agent memory.

| Database | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[Milvus](https://github.com/milvus-io/milvus)** | Milvus | High-performance, distributed vector database. | Built for billion-scale datasets, GPU indexing, hybrid search support. |
| **[Qdrant](https://github.com/qdrant/qdrant)** | Qdrant | Rust-based vector similarity search engine. | Fast payload filtering, REST/gRPC interfaces, production scale. |
| **[FAISS](https://github.com/facebookresearch/faiss)** | Meta Research | Library for efficient similarity search of dense vectors. | GPU acceleration, fast index algorithms, local run implementation. |
| **[Chroma](https://github.com/chroma-core/chroma)** | Chroma Core | Lightweight, developer-friendly open-source vector store. | Fast python setup, ideal for notebooks and rapid prototyping. |

---

## 🎨 Vibe Coding & Generative UI Tools
Tools designed to let non-technical users or visual developers generate layouts, notes, and whole apps using AI natural language ("vibe coding").

| Tool | Creator | Description | Key Features |
| :--- | :--- | :--- | :--- |
| **[AFFiNE](https://github.com/toeverything/AFFiNE)** | toeverything | Workspace tool unifying notes, tasks, and graphics. | AI-native drawing, structured page layout generation. |
| **[Chatbot UI](https://github.com/mckaywrigley/chatbot-ui)** | McKay Wrigley | A clean, customizable front-end for LLM APIs. | Custom prompt templates, system instructions, attachment parsing. |
| **[OpenUI](https://github.com/wandb/openui)** | Weights & Biases | Generates responsive HTML/CSS layouts visually from description. | Direct Tailwind/React component export, interactive design editor. |

---

## 📊 Quick Comparison Matrix

| Tool | Category | Licensing | Primary Language / Stack | Best Suited For... |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini CLI** | CLI Agent | MIT | TypeScript / Node.js | Fast, tool-equipped CLI coding using Google Gemini models |
| **Claude Code** | CLI Agent | Proprietary | TypeScript / Node.js | Multi-file codebase adjustments using Claude |
| **Antigravity CLI** | CLI Agent | Proprietary | Python / CLI | Sandboxed multi-agent and browser-based test loops |
| **Goose** | CLI Agent | Apache-2.0 | Rust / Python | Executing task checklists with MCP plugins |
| **OpenHands** | CLI Agent / Web | Apache-2.0 | Python / Docker | Isolated container-level SWE benchmarks and repairs |
| **LangGraph** | Agent Framework | MIT | Python / JS | Custom stateful multi-agent workflows and graph logic |
| **CrewAI** | Agent Framework | MIT | Python | Role-based agent teams mimicking human software processes |
| **Ollama** | Serving Engine | MIT | Go / C++ | Running and exposing open-weights models locally |
| **CodeGate** | Security Proxy | Apache-2.0 | Go / Rust | Masking secrets and PII from outgoing LLM traffic |
| **Cursor** | Native IDE | Proprietary | VS Code Fork | The most polished, complete AI-native coding environment |

---

## 🤝 Contributing

We welcome contributions! If you would like to add a new tool, extension, proxy, plugin, or CLI agent:

1. Fork this repository.
2. Add the tool to the appropriate table in alphabetical order.
3. Submit a Pull Request with a clear description of the tool.
