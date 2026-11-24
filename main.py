#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5 syllables, under 200 characters)
to /output/entry.txt. Deterministic, no network, no dependencies.
"""

import os

HAIKU = """Cursor blinks at three
the stack trace ends in silence
I wrote it at noon
"""


def main() -> None:
    text = HAIKU.strip("\n") + "\n"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    lines = text.strip().split("\n")
    assert len(lines) == 3, "entry must be three lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
