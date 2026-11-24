#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes one line (<=120 chars) to /output/entry.txt: the error message
a kitchen toaster shows its owner when something goes wrong.
"""

import os

LINE = "ERROR: I BURNED THE TOAST. YOU WATCHED ME DO IT. WE BOTH KNOW WHOSE FAULT THIS IS."


def main():
    # Gate: the entry must be 1-120 chars of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 120, "line must be 1-120 chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
