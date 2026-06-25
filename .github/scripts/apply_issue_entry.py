#!/usr/bin/env python3
"""Apply an agent-client issue suggestion to both localized README files."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


README_EN = Path("README.en.md")
README_ZH = Path("README.md")

CATEGORY_HEADINGS_ZH = {
    "General Desktop Agents": "通用桌面 Agent",
    "Agentic IDEs and Workspaces": "Agentic IDE 与工作区",
    "Editor Extensions": "编辑器扩展",
    "Terminal and TUI Agents": "终端与 TUI Agent",
    "Local-First and Open-Source Clients": "本地优先与开源客户端",
    "Related Standards and Ecosystem": "相关标准与生态",
}


def normalize_heading(value: str) -> str:
    value = value.strip().lower()
    value = value.replace("?", "")
    value = re.sub(r"\s+", " ", value)
    return value


def parse_sections(body: str) -> dict[str, str]:
    matches = list(re.finditer(r"^#{2,3}\s+(.+?)\s*$", body, re.MULTILINE))
    sections: dict[str, str] = {}

    for index, match in enumerate(matches):
        name = normalize_heading(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections[name] = body[start:end].strip()

    return sections


def section_value(sections: dict[str, str], *names: str) -> str:
    for name in names:
        value = sections.get(normalize_heading(name))
        if value:
            return value
    return ""


def extract_markdown_entry(value: str) -> str:
    fence = re.search(r"```(?:markdown)?\s*(.*?)```", value, re.DOTALL | re.IGNORECASE)
    if fence:
        value = fence.group(1)

    lines = [line.strip() for line in value.splitlines() if line.strip()]
    entry_lines = [line for line in lines if line.startswith("- [")]
    if not entry_lines:
        return ""
    return entry_lines[0]


def validate_entry(entry: str, field_name: str) -> None:
    if not entry.startswith("- ["):
        raise ValueError(f"{field_name} must be a single Markdown list item starting with '- ['.")
    if not re.search(r"\]\(https?://[^)]+\)", entry):
        raise ValueError(f"{field_name} must include an HTTP(S) link.")
    required_parts = ["Platforms:", "Type:", "License:", "Last checked:"]
    missing = [part for part in required_parts if part not in entry]
    if missing:
        raise ValueError(f"{field_name} is missing metadata: {', '.join(missing)}")


def entry_url(entry: str) -> str:
    match = re.search(r"\]\(([^)]+)\)", entry)
    if not match:
        raise ValueError("Entry does not contain a Markdown link.")
    return match.group(1)


def insert_entry(content: str, heading: str, entry: str) -> tuple[str, bool]:
    url = entry_url(entry)
    if url in content:
        return content, False

    pattern = re.compile(
        rf"(^## {re.escape(heading)}\n\n)(.*?)(?=\n## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        raise ValueError(f"Could not find README section: {heading}")

    section_body = match.group(2).rstrip()
    replacement = f"{match.group(1)}{section_body}\n{entry}\n"
    return content[: match.start()] + replacement + content[match.end() :], True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Parse and validate without writing files.")
    args = parser.parse_args()

    body = os.environ.get("ISSUE_BODY", "")
    if not body:
        raise ValueError("ISSUE_BODY environment variable is required.")

    sections = parse_sections(body)
    category = section_value(sections, "Category", "Suggested category")
    english_entry = extract_markdown_entry(
        section_value(sections, "English entry", "Suggested English entry", "Suggested entry")
    )
    chinese_entry = extract_markdown_entry(
        section_value(sections, "Chinese entry", "Suggested Chinese entry")
    )

    if not category:
        raise ValueError("Issue is missing a Category section.")
    if category not in CATEGORY_HEADINGS_ZH:
        allowed = ", ".join(CATEGORY_HEADINGS_ZH)
        raise ValueError(f"Unsupported category '{category}'. Allowed categories: {allowed}")
    if not english_entry:
        raise ValueError("Issue is missing an English entry.")
    if not chinese_entry:
        raise ValueError("Issue is missing a Chinese entry.")

    validate_entry(english_entry, "English entry")
    validate_entry(chinese_entry, "Chinese entry")

    readme_en = README_EN.read_text(encoding="utf-8")
    readme_zh = README_ZH.read_text(encoding="utf-8")

    new_en, changed_en = insert_entry(readme_en, category, english_entry)
    new_zh, changed_zh = insert_entry(readme_zh, CATEGORY_HEADINGS_ZH[category], chinese_entry)

    if args.dry_run:
        print(f"Validated issue entry for category: {category}")
        print(f"README.en.md changed: {changed_en}")
        print(f"README.md changed: {changed_zh}")
        return 0

    README_EN.write_text(new_en, encoding="utf-8")
    README_ZH.write_text(new_zh, encoding="utf-8")
    print(f"Applied issue entry to category: {category}")
    print(f"README.en.md changed: {changed_en}")
    print(f"README.md changed: {changed_zh}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
