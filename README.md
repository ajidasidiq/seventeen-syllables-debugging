# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/ajidasidiq/seventeen-syllables-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/ajidasidiq/seventeen-syllables-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A make.fun bounty entry for **Seventeen Syllables of Debugging**.

## The haiku

> Cursor blinks at three
> the stack trace ends in silence
> I wrote it at noon

Three lines, 5-7-5 syllables, 74 characters. The picture is concrete — a cursor blinking at 3 a.m., a stack trace that runs out — and the last line turns it: the bug keeping you up was written by your own hand, hours earlier, in daylight.

## What it does

`main.py` validates the haiku (three lines, 1–200 characters) and writes it to `/output/entry.txt`, deterministically, with no network access and no dependencies.

## How to run

Requires Python 3.13 or later. No dependencies.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
