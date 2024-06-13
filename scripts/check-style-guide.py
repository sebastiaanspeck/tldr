#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

"""
A Python script to check pages against the style guide.

Note: If the current directory or one of its parents is called "tldr", the script will assume it is the tldr root, i.e., the directory that contains a clone of https://github.com/tldr-pages/tldr
If you aren't, the script will use TLDR_ROOT as the tldr root. Also, ensure 'git' is available.

Usage:
    python3 scripts/check-style-guide.py [-l LANGUAGE]

Options:
    -l, --language LANGUAGE
        Specify the language, a POSIX Locale Name in the form of "ll" or "ll_CC" (e.g. "fr" or "pt_BR").
"""

import re
from pathlib import Path
import argparse
from _common import (
    IGNORE_FILES,
    Colors,
    get_tldr_root,
    get_pages_dir,
    get_locale,
    create_colored_line,
)


def check_short_long_option(path: Path) -> str:
    with path.open(encoding="utf-8") as f:
        lines = f.readlines()

        for i in range(1, len(lines)):
            command_match = re.search(r"\{\{-([a-z]{1})\|--\w+(-\w+)*\}\}", lines[i])
            if command_match:
                description_match = re.search(rf"\[({command_match[1]})]", lines[i - 2])
                if description_match and command_match[1] == description_match[1]:
                    return create_colored_line(Colors.BLUE, "needs a manual check")

    return ""


def check_page(path: Path, language_to_check: str = "") -> str:
    """
    Check a page.

    path (string): Path to a page.
    language_to_check (string): Optionally, the language of the translation to be checked.

    Returns:
    str: Execution status
         "" if the page matches the Style Guide"
         "\x1b[34mpage needs an update"
    """

    locale = get_locale(path)
    if language_to_check != "" and locale != language_to_check:
        # return empty status to indicate that the page is skipped
        return ""

    return check_short_long_option(path)


def main():
    parser = argparse.ArgumentParser(
        description="Checks all pages on some Style Guide conventions"
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        default="",
        help='language in the format "ll" or "ll_CC" (e.g. "fr" or "pt_BR")',
    )
    args = parser.parse_args()

    root = get_tldr_root()
    pages_dirs = get_pages_dir(root)

    en_path = root / "pages"
    platforms = [i.name for i in en_path.iterdir() if i.name not in IGNORE_FILES]
    for platform in platforms:
        platform_path = en_path / platform
        commands = [
            f"{platform}/{page.name}"
            for page in platform_path.iterdir()
            if page.name not in IGNORE_FILES
        ]
        for command in commands:
            for page_dir in pages_dirs:
                path = root / page_dir / command
                if path.exists():
                    status = check_page(path, args.language)
                    rel_path = "/".join(path.parts[-3:])
                    if status != "":
                        print(create_colored_line(Colors.GREEN, f"{rel_path} {status}"))


if __name__ == "__main__":
    main()
