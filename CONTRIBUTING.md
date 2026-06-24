# Contributing

Thanks for helping improve Awesome Agent Client.

This project is a curated list, not a complete directory. A smaller list of
high-quality, maintained, and clearly useful agent clients is better than a
large list of weak or duplicated entries.

## What Belongs Here

Add a project only when it meets all of these requirements:

- It has an official website, documentation site, or official repository.
- It provides a usable client surface such as a desktop app, IDE, editor
  extension, CLI, TUI, web app, or local control surface.
- It supports agentic behavior such as multi-step execution, tool use, file or
  code edits, command execution, MCP, or autonomous workflows.
- It is actively maintained and can be installed or used by readers.
- You can explain why it is worth including.

## What Does Not Belong Here

Please do not add:

- Pure frameworks, SDKs, papers, or benchmark projects without a usable client.
- Archived, deprecated, unmaintained, or impossible-to-install projects.
- Projects with only a landing page and no docs, repository, or install path.
- Duplicate entries already covered by another item.
- Affiliate links, referral links, or sponsored copy.

## Entry Format

Use this exact format:

```markdown
- [Name](https://example.com) - One sentence description. Platforms: macOS, Windows, Linux. Type: Desktop / IDE / Extension / CLI. License: Open source / Proprietary / Freemium. Last checked: 2026-06-24.
```

Descriptions should be factual, start with an uppercase character, and end with
a period before the metadata fields.

## How To Contribute

1. Fork the repository.
1. Create a branch with a clear name:

```bash
git checkout -b add-client-name
```

1. Add or update the entry in both `README.md` and `README.zh-CN.md`.
1. Keep entries alphabetically sensible within a category when practical, but
   prioritize category fit over strict sorting.
1. Run the checks:

```bash
npx markdownlint-cli2 README.md README.zh-CN.md CONTRIBUTING.md
npx markdown-link-check -c .markdown-link-check.json README.md
npx markdown-link-check -c .markdown-link-check.json README.zh-CN.md
```

1. Commit with a clear message:

```bash
git add .
git commit -m "Add client-name"
```

1. Open a pull request and explain why the client is awesome.

## Automated Issue-To-PR Flow

Maintainers can also turn a completed "Add an agent client" issue into a pull
request automatically:

1. Make sure the issue includes `Category`, `English entry`, and `Chinese entry`.
1. Review the official link and the "Why awesome" explanation.
1. Add the `ready-for-pr` label to the issue.
1. GitHub Actions will create a branch, update both READMEs, run the checks, and
   open a pull request that closes the issue when merged.

The automation intentionally waits for the `ready-for-pr` label so every
suggestion still gets a maintainer review before a pull request is opened.

## Pull Request Checklist

- The project has an official source link.
- The entry appears in both English and Chinese READMEs.
- The entry has platform, type, license/model, and last-checked metadata.
- The link works.
- The project is not archived or deprecated.
- The pull request explains why the client belongs here.
