# Awesome Agent Client [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md)

A curated list of desktop, IDE, extension, and terminal clients for AI agents.

This list focuses on user-facing clients that let people delegate work to AI
agents from their desktop, editor, terminal, or local machine. It intentionally
does not list pure agent frameworks unless they provide a usable client surface.

## Contents

- [Selection Criteria](#selection-criteria)
- [General Desktop Agents](#general-desktop-agents)
- [Agentic IDEs and Workspaces](#agentic-ides-and-workspaces)
- [Editor Extensions](#editor-extensions)
- [Terminal and TUI Agents](#terminal-and-tui-agents)
- [Local-First and Open-Source Clients](#local-first-and-open-source-clients)
- [Related Standards and Ecosystem](#related-standards-and-ecosystem)

## Selection Criteria

- The project must have an official website, documentation site, or repository.
- The project must provide a client surface: desktop app, IDE, editor extension,
  CLI, TUI, web app, or local control surface.
- The client must support agentic behavior such as multi-step execution, tool
  use, file or code changes, command execution, MCP, or autonomous workflows.
- Unmaintained, archived, impossible-to-install, or undocumented projects are
  excluded from the main list.
- Descriptions should explain why the client is useful, not just repeat a
  marketing tagline.

## General Desktop Agents

- [ChatGPT Desktop](https://chatgpt.com/features/desktop/) - Desktop ChatGPT client for using ChatGPT with files, screenshots, voice, and desktop shortcuts. Platforms: macOS, Windows. Type: Desktop. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Claude Desktop](https://claude.com/download) - Desktop Claude client with chat, desktop extensions, and access to Claude's agentic product surfaces. Platforms: macOS, Windows. Type: Desktop. License: Proprietary / Freemium. Last checked: 2026-06-24.

## Agentic IDEs and Workspaces

- [Cursor](https://cursor.com/) - AI coding workspace with desktop, CLI, web, and mobile agent surfaces for planning and editing code. Platforms: macOS, Windows, Linux, Web, Mobile. Type: IDE / Agent workspace. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Devin Desktop](https://docs.devin.ai/desktop/getting-started) - Agent command center and IDE, formerly Windsurf, for managing local and cloud software agents. Platforms: macOS, Windows, Linux. Type: IDE / Desktop. License: Proprietary / Commercial. Last checked: 2026-06-24.
- [Google Antigravity](https://antigravity.google/) - Agentic development platform for managing multiple local agents across editor, terminal, and browser workflows. Platforms: macOS, Windows, Linux. Type: IDE / Agent workspace. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Kiro](https://aws.amazon.com/documentation-overview/kiro/) - Agentic engineering IDE and CLI for spec-driven development, local agent collaboration, and delegated coding sessions. Platforms: macOS, Windows, Linux, Web. Type: IDE / CLI / Web. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Zed](https://zed.dev/docs/ai/external-agents) - Code editor with an Agent Panel and external agent support through the Agent Client Protocol. Platforms: macOS, Linux, Windows. Type: IDE / Agent client. License: Open source / Freemium. Last checked: 2026-06-24.
- [JetBrains Junie](https://www.jetbrains.com/junie/) - JetBrains coding agent for IDE workflows, terminal usage, and autonomous code changes. Platforms: macOS, Windows, Linux. Type: IDE / CLI. License: Proprietary / Freemium. Last checked: 2026-06-24.

## Editor Extensions

- [GitHub Copilot Agent Mode](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide#agent-mode) - Agent mode for GitHub Copilot that autonomously edits code, proposes terminal commands, and iterates on failures in supported IDEs. Platforms: VS Code, Visual Studio, JetBrains, Xcode, Eclipse. Type: Editor extension. License: Proprietary / Commercial. Last checked: 2026-06-24.
- [Cline](https://cline.bot/) - Open-source coding agent runtime available in editor, terminal, IDE extension, SDK, and embedded surfaces. Platforms: macOS, Windows, Linux. Type: Extension / CLI / SDK. License: Open source. Last checked: 2026-06-24.
- [Roo Code](https://github.com/RooCodeInc/Roo-Code) - Open-source VS Code-compatible coding agent with specialized modes, MCP support, and task automation. Platforms: VS Code-compatible editors. Type: Editor extension. License: Open source. Last checked: 2026-06-24.
- [Kilo Code](https://github.com/Kilo-Org/kilocode) - Open-source coding agent for VS Code, JetBrains, and CLI with model switching and usage-based model access. Platforms: VS Code, JetBrains, CLI. Type: Extension / CLI. License: Open source. Last checked: 2026-06-24.

## Terminal and TUI Agents

- [OpenAI Codex CLI](https://github.com/openai/codex) - Open-source coding agent from OpenAI that runs locally in your terminal and can read, change, and run code. Platforms: macOS, Linux, Windows. Type: CLI. License: Open source. Last checked: 2026-06-24.
- [Claude Code](https://claude.com/product/claude-code) - Anthropic's agentic coding tool for terminal, IDE, desktop app, browser, and GitHub workflows. Platforms: macOS, Linux, Windows. Type: CLI / IDE / Desktop. License: Proprietary / Commercial. Last checked: 2026-06-24.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Open-source AI agent from Google that brings Gemini into the terminal for coding, problem solving, and tool use. Platforms: macOS, Windows, Linux. Type: CLI. License: Open source. Last checked: 2026-06-24.
- [OpenCode](https://opencode.ai/) - Open-source AI coding agent available as a terminal interface, desktop app, and IDE extension. Platforms: macOS, Windows, Linux. Type: TUI / Desktop / Extension. License: Open source. Last checked: 2026-06-24.
- [Aider](https://github.com/aider-ai/aider) - Terminal pair-programming agent that edits files in your local Git repository and automatically commits changes. Platforms: macOS, Windows, Linux. Type: CLI. License: Open source. Last checked: 2026-06-24.
- [Cursor CLI](https://cursor.com/cli) - Cursor's terminal agent for scripts, automations, MCP workflows, and headless coding tasks. Platforms: macOS, Windows, Linux. Type: CLI. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Amp](https://ampcode.com/) - Coding agent with terminal, editor, JetBrains, and remote-control surfaces for multi-step software work. Platforms: macOS, Linux, Windows via WSL. Type: CLI / Extension / Remote agent. License: Proprietary / Pay-as-you-go. Last checked: 2026-06-24.

## Local-First and Open-Source Clients

- [Goose](https://goose-docs.ai/) - Native open-source AI agent with desktop app, CLI, API, MCP extensions, and support for many model providers. Platforms: macOS, Windows, Linux. Type: Desktop / CLI / API. License: Open source. Last checked: 2026-06-24.
- [AnythingLLM Desktop](https://anythingllm.com/) - Local-first desktop AI application with RAG, custom tools, MCP support, and AI agent workflows. Platforms: macOS, Windows, Linux. Type: Desktop. License: Open source / Commercial. Last checked: 2026-06-24.
- [OpenHands](https://www.openhands.dev/) - Open-source software engineering agent platform with web UI, CLI, and developer control surfaces. Platforms: Web, CLI, self-hosted. Type: Web / CLI / Agent canvas. License: Open source / Commercial. Last checked: 2026-06-24.

## Related Standards and Ecosystem

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - Open protocol for connecting AI applications to external data sources, tools, and workflows. Platforms: N/A. Type: Protocol. License: Open standard. Last checked: 2026-06-24.
- [Agent Client Protocol](https://agentclientprotocol.com/get-started/introduction) - Protocol for standardizing communication between editors, IDEs, and coding agents. Platforms: N/A. Type: Protocol. License: Open standard. Last checked: 2026-06-24.
- [AGENTS.md](https://github.com/agentsmd/agents.md) - Open format for giving coding agents predictable project instructions and context. Platforms: N/A. Type: Project convention. License: Open standard. Last checked: 2026-06-24.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md)
before opening an issue or pull request.

## License

MIT © 2026 dctongsheng
