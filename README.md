# One-Line Laugh-Off

[![One-Line Laugh-Off](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/yayass-crypto/one-line-laugh-off-20261125/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/yayass-crypto/one-line-laugh-off-20261125/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

An entry for [make.fun's "One-Line Laugh-Off" bounty](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) — one funny line, at most 200 characters, judged head-to-head by the house judge. Winner takes all $2.

## The line

> The librarian shushed me for laughing, so now I read funny books in the parking lot like a criminal with a library card.

One sentence, 116 characters. Shushed for laughing at the funny books, so the reading moves outside — and the last words are the punchline: a criminal with a library card.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It self-checks the line before writing it — non-empty, no leading or trailing whitespace, no newlines, at most 200 characters, exactly one sentence ending in a period — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt` when `/output` is not writable), re-reads the file, and verifies the bytes match before printing a confirmation with the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```

That writes the line to `/output/entry.txt` when writable, or to `out/entry.txt` otherwise. To choose the destination yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/my-out python3 main.py
```
