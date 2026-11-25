#!/usr/bin/env python3
"""Laugh-off entry: one funny sentence, written to entry.txt."""

from __future__ import annotations

import os
import sys
from pathlib import Path

LINE = "The librarian shushed me for laughing, so I read funny books in the parking lot like a criminal with a library card."

LIMIT = 200
NAME = "entry.txt"


class EntryError(ValueError):
    """Raised when the line or the destination fails a check."""


def _guard(text: str) -> bytes:
    if not text:
        raise EntryError("empty line")
    if text != text.strip():
        raise EntryError("leading or trailing whitespace")
    if any(ord(c) < 32 for c in text):
        raise EntryError("newline or control character present")
    if len(text) > LIMIT:
        raise EntryError(f"{len(text)} chars exceeds the {LIMIT} limit")
    if "?" in text or "!" in text:
        raise EntryError("question or exclamation mark present")
    if not text.endswith("."):
        raise EntryError("must end with a period")
    body = text[:-1]
    if ". " in body or ".." in body:
        raise EntryError("more than one sentence")
    return text.encode("utf-8")


def _target() -> Path:
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    places = [Path(wanted)] if wanted else []
    places.extend([Path("/output"), Path("out")])
    for folder in places:
        try:
            folder.mkdir(parents=True, exist_ok=True)
            probe = folder / ".write-probe"
            probe.touch()
            probe.unlink()
        except OSError:
            continue
        return folder / NAME
    return Path("/output") / NAME


def _save(dest: Path, payload: bytes) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(payload)
    if dest.read_bytes() != payload:
        raise EntryError("read-back bytes differ from the line")


def run() -> int:
    try:
        payload = _guard(LINE)
        dest = _target()
        _save(dest, payload)
    except (EntryError, OSError) as exc:
        print(f"entry failed: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {dest}")
    print(f"characters: {len(LINE)}")
    print(f"bytes: {len(payload)}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
