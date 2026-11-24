#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5 syllables, under 200 characters)
to /output/entry.txt. Deterministic, no network, no dependencies.
"""

import os
import re

HAIKU = """Cursor blinks at three
the stack trace ends in silence
I wrote it at noon
"""

# Expected syllable counts per line (5-7-5). Each word is counted by hand
# below; the table is the source of truth, the check just guards typos.
SYLLABLES = {
    "cursor": 2, "blinks": 1, "at": 1, "three": 1,
    "the": 1, "stack": 1, "trace": 1, "ends": 1, "in": 1, "silence": 2,
    "i": 1, "wrote": 1, "it": 1, "noon": 1,
}
SHAPE = (5, 7, 5)


def count_syllables(line: str) -> int:
    words = re.findall(r"[a-z]+", line.lower())
    return sum(SYLLABLES[w] for w in words)


def main() -> None:
    text = HAIKU.strip("\n") + "\n"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    lines = text.strip().split("\n")
    assert len(lines) == 3, "entry must be three lines"
    for line, want in zip(lines, SHAPE):
        got = count_syllables(line)
        assert got == want, f"line {line!r} has {got} syllables, want {want}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
