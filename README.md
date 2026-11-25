# Laugh-Off Entry: the Shushed Reader

[![One-Line Laugh-Off](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/yayass-crypto/one-line-laugh-off-20261125/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/yayass-crypto/one-line-laugh-off-20261125/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

This repo holds my submission to [make.fun's "One-Line Laugh-Off" bounty](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae): a single funny line, no more than 200 characters, scored head-to-head by the house judge. First place takes the whole $2.

## The joke

> The librarian shushed me for laughing, so I read funny books in the parking lot like a criminal with a library card.

116 characters, one sentence. Getting shushed for laughing at the funny books pushes the reading outdoors — and the laugh lands on the closing image: a criminal with a library card.

## What the program does

`main.py` runs on the Python 3.13 standard library alone and never touches the network. Before writing anything it puts the line through a set of checks: it must be non-empty, free of leading or trailing whitespace, newlines and control characters, at most 200 characters long, a single sentence, and it must end with a period. The destination is `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set, otherwise `/output/entry.txt`, with `out/entry.txt` as the fallback if `/output` cannot be written. After writing, the program reads the file back and refuses to report success unless the bytes match exactly. Success exits 0; any failed check exits 1.

## Running it

```sh
python3 main.py
```

That drops the line into `/output/entry.txt` when that folder is writable, or `out/entry.txt` when it is not. To pick a destination yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/my-out python3 main.py
```
