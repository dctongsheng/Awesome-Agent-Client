# Awesome Agent Client [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [简体中文](README.zh-CN.md)

一个精选清单，收录桌面端、IDE、编辑器扩展和终端里的 AI Agent 客户端。

这个清单关注用户可以直接使用的客户端：桌面应用、编辑器、终端、TUI、本地控制台或 Web 控制面板。纯 Agent 框架默认不收录，除非它同时提供可直接使用的客户端形态。

## 目录

- [收录标准](#收录标准)
- [通用桌面 Agent](#通用桌面-agent)
- [Agentic IDE 与工作区](#agentic-ide-与工作区)
- [编辑器扩展](#编辑器扩展)
- [终端与 TUI Agent](#终端与-tui-agent)
- [本地优先与开源客户端](#本地优先与开源客户端)
- [相关标准与生态](#相关标准与生态)

## 收录标准

- 项目必须有官网、官方文档或官方仓库。
- 项目必须提供客户端形态：桌面应用、IDE、编辑器扩展、CLI、TUI、Web 应用或本地控制界面。
- 客户端必须具备 Agent 能力，例如多步骤执行、工具调用、文件或代码修改、命令执行、MCP 或自主工作流。
- 已停更、归档、无法安装或缺少文档的项目不进入主清单。
- 描述应说明这个客户端为什么值得关注，而不是只复述营销口号。

## 通用桌面 Agent

- [ChatGPT Desktop](https://chatgpt.com/features/desktop/) - ChatGPT 桌面客户端，支持文件、截图、语音和桌面快捷入口。Platforms: macOS, Windows. Type: Desktop. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Claude Desktop](https://claude.com/download) - Claude 桌面客户端，支持聊天、桌面扩展以及 Claude 的 Agent 产品入口。Platforms: macOS, Windows. Type: Desktop. License: Proprietary / Freemium. Last checked: 2026-06-24.

## Agentic IDE 与工作区

- [Cursor](https://cursor.com/) - AI 编程工作区，提供桌面、CLI、Web 和移动端 Agent 入口，可用于规划和修改代码。Platforms: macOS, Windows, Linux, Web, Mobile. Type: IDE / Agent workspace. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Devin Desktop](https://docs.devin.ai/desktop/getting-started) - Agent 指挥中心和 IDE，前身为 Windsurf，用于管理本地和云端软件 Agent。Platforms: macOS, Windows, Linux. Type: IDE / Desktop. License: Proprietary / Commercial. Last checked: 2026-06-24.
- [Google Antigravity](https://antigravity.google/) - Agentic 开发平台，可在编辑器、终端和浏览器工作流中管理多个本地 Agent。Platforms: macOS, Windows, Linux. Type: IDE / Agent workspace. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Kiro](https://aws.amazon.com/documentation-overview/kiro/) - 面向规格驱动开发的 Agentic 工程 IDE 和 CLI，支持本地 Agent 协作与委派式编码会话。Platforms: macOS, Windows, Linux, Web. Type: IDE / CLI / Web. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Zed](https://zed.dev/docs/ai/external-agents) - 带 Agent Panel 的代码编辑器，可通过 Agent Client Protocol 接入外部 Agent。Platforms: macOS, Linux, Windows. Type: IDE / Agent client. License: Open source / Freemium. Last checked: 2026-06-24.
- [JetBrains Junie](https://www.jetbrains.com/junie/) - JetBrains 的编程 Agent，可在 IDE 和终端中执行自主代码修改任务。Platforms: macOS, Windows, Linux. Type: IDE / CLI. License: Proprietary / Freemium. Last checked: 2026-06-24.

## 编辑器扩展

- [GitHub Copilot Agent Mode](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide#agent-mode) - GitHub Copilot 的 Agent 模式，可在支持的 IDE 中自主改代码、提出终端命令并迭代修复失败。Platforms: VS Code, Visual Studio, JetBrains, Xcode, Eclipse. Type: Editor extension. License: Proprietary / Commercial. Last checked: 2026-06-24.
- [Cline](https://cline.bot/) - 开源编程 Agent runtime，提供编辑器、终端、IDE 扩展、SDK 和嵌入式形态。Platforms: macOS, Windows, Linux. Type: Extension / CLI / SDK. License: Open source. Last checked: 2026-06-24.
- [Roo Code](https://github.com/RooCodeInc/Roo-Code) - 开源 VS Code 兼容编程 Agent，支持专用模式、MCP 和任务自动化。Platforms: VS Code-compatible editors. Type: Editor extension. License: Open source. Last checked: 2026-06-24.
- [Kilo Code](https://github.com/Kilo-Org/kilocode) - 面向 VS Code、JetBrains 和 CLI 的开源编程 Agent，支持模型切换和按模型使用量计费。Platforms: VS Code, JetBrains, CLI. Type: Extension / CLI. License: Open source. Last checked: 2026-06-24.

## 终端与 TUI Agent

- [OpenAI Codex CLI](https://github.com/openai/codex) - OpenAI 的开源本地终端编程 Agent，可读取、修改并运行代码。Platforms: macOS, Linux, Windows. Type: CLI. License: Open source. Last checked: 2026-06-24.
- [Claude Code](https://claude.com/product/claude-code) - Anthropic 的 Agentic 编程工具，覆盖终端、IDE、桌面应用、浏览器和 GitHub 工作流。Platforms: macOS, Linux, Windows. Type: CLI / IDE / Desktop. License: Proprietary / Commercial. Last checked: 2026-06-24.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google 的开源终端 AI Agent，用于编码、问题解决和工具调用。Platforms: macOS, Windows, Linux. Type: CLI. License: Open source. Last checked: 2026-06-24.
- [OpenCode](https://opencode.ai/) - 开源 AI 编程 Agent，提供终端界面、桌面应用和 IDE 扩展。Platforms: macOS, Windows, Linux. Type: TUI / Desktop / Extension. License: Open source. Last checked: 2026-06-24.
- [Aider](https://github.com/aider-ai/aider) - 终端结对编程 Agent，可在本地 Git 仓库中修改文件并自动提交变更。Platforms: macOS, Windows, Linux. Type: CLI. License: Open source. Last checked: 2026-06-24.
- [Cursor CLI](https://cursor.com/cli) - Cursor 的终端 Agent，用于脚本、自动化、MCP 工作流和 headless 编程任务。Platforms: macOS, Windows, Linux. Type: CLI. License: Proprietary / Freemium. Last checked: 2026-06-24.
- [Amp](https://ampcode.com/) - 编程 Agent，提供终端、编辑器、JetBrains 和远程控制形态，适合多步骤软件开发任务。Platforms: macOS, Linux, Windows via WSL. Type: CLI / Extension / Remote agent. License: Proprietary / Pay-as-you-go. Last checked: 2026-06-24.

## 本地优先与开源客户端

- [Goose](https://goose-docs.ai/) - 原生开源 AI Agent，提供桌面应用、CLI、API、MCP 扩展和多模型提供商支持。Platforms: macOS, Windows, Linux. Type: Desktop / CLI / API. License: Open source. Last checked: 2026-06-24.
- [AnythingLLM Desktop](https://anythingllm.com/) - 本地优先桌面 AI 应用，支持 RAG、自定义工具、MCP 和 AI Agent 工作流。Platforms: macOS, Windows, Linux. Type: Desktop. License: Open source / Commercial. Last checked: 2026-06-24.
- [OpenHands](https://www.openhands.dev/) - 开源软件工程 Agent 平台，提供 Web UI、CLI 和开发者控制界面。Platforms: Web, CLI, self-hosted. Type: Web / CLI / Agent canvas. License: Open source / Commercial. Last checked: 2026-06-24.
- [Hermes Agent](https://hermes-agent.nousresearch.com/) - Nous Research 构建的开源自进化 AI Agent，提供桌面和 CLI 入口，支持持久记忆、工具调用和从经验中学习技能。Platforms: macOS, Windows, Linux. Type: Desktop / CLI / Agent runtime. License: Open source / MIT. Last checked: 2026-06-24.

## 相关标准与生态

- [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) - 用于连接 AI 应用和外部数据源、工具、工作流的开放协议。Platforms: N/A. Type: Protocol. License: Open standard. Last checked: 2026-06-24.
- [Agent Client Protocol](https://agentclientprotocol.com/get-started/introduction) - 用于标准化编辑器、IDE 与编程 Agent 通信的协议。Platforms: N/A. Type: Protocol. License: Open standard. Last checked: 2026-06-24.
- [AGENTS.md](https://github.com/agentsmd/agents.md) - 为编程 Agent 提供项目指令和上下文的开放格式。Platforms: N/A. Type: Project convention. License: Open standard. Last checked: 2026-06-24.

## 贡献

欢迎贡献。提交 Issue 或 Pull Request 前，请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

MIT © 2026 dctongsheng
