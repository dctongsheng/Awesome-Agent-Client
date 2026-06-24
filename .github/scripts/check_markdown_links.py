#!/usr/bin/env python3
"""Bounded Markdown link checker for CI automation."""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


CONFIG_PATH = Path(".markdown-link-check.json")
DEFAULT_ALIVE_CODES = {200, 206, 403}
TIMEOUT_SECONDS = 12
USER_AGENT = "Awesome-Agent-Client-Link-Check"


def load_config() -> tuple[list[re.Pattern[str]], set[int]]:
    if not CONFIG_PATH.exists():
        return [], DEFAULT_ALIVE_CODES

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    ignore_patterns = [
        re.compile(item["pattern"])
        for item in config.get("ignorePatterns", [])
        if item.get("pattern")
    ]
    alive_codes = set(config.get("aliveStatusCodes", DEFAULT_ALIVE_CODES))
    return ignore_patterns, alive_codes


def markdown_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [
        match.group(1).strip()
        for match in re.finditer(r"!?\[[^\]]*]\(([^)]+)\)", text)
        if match.group(1).strip()
    ]


def is_ignored(url: str, patterns: list[re.Pattern[str]]) -> bool:
    return any(pattern.search(url) for pattern in patterns)


def check_local_link(source: Path, link: str) -> tuple[bool, str]:
    target = link.split("#", 1)[0]
    if not target:
        return True, "anchor"
    local_path = (source.parent / target).resolve()
    if local_path.exists():
        return True, "local"
    return False, "missing local file"


def request_url(url: str, method: str) -> int:
    request = urllib.request.Request(
        url,
        method=method,
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return response.status


def check_http_link(url: str, alive_codes: set[int]) -> tuple[bool, str]:
    for method in ("HEAD", "GET"):
        try:
            status = request_url(url, method)
            return status in alive_codes, f"status {status}"
        except urllib.error.HTTPError as error:
            if error.code == 405 and method == "HEAD":
                continue
            return error.code in alive_codes, f"status {error.code}"
        except Exception as error:
            if method == "HEAD":
                continue
            return False, str(error)
    return False, "request failed"


def main(paths: list[str]) -> int:
    ignore_patterns, alive_codes = load_config()
    failures: list[str] = []

    for raw_path in paths:
        path = Path(raw_path)
        print(f"Checking {path}")
        for link in markdown_links(path):
            if is_ignored(link, ignore_patterns):
                print(f"  SKIP {link}")
                continue

            parsed = urlparse(link)
            if parsed.scheme in {"http", "https"}:
                ok, detail = check_http_link(link, alive_codes)
            else:
                ok, detail = check_local_link(path, link)

            prefix = "OK" if ok else "FAIL"
            print(f"  {prefix} {link} ({detail})")
            if not ok:
                failures.append(f"{path}: {link} ({detail})")

    if failures:
        print("\nDead or unreachable links:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: check_markdown_links.py <markdown-file> [...]", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1:]))
