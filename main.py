#!/usr/bin/env python3
"""One-line laugh entry: write a single funny line to the entry file."""

import os
import sys

JOKE = "The librarian shushed me for laughing, so I read funny books in the parking lot like a criminal with a library card."

MAX_CHARS = 200
FILENAME = "entry.txt"


def pick_destination():
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    candidates = [requested] if requested else []
    candidates += ["/output", "out"]
    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
            probe = os.path.join(directory, ".write-probe")
            with open(probe, "wb") as handle:
                handle.write(b"")
            os.unlink(probe)
        except OSError:
            continue
        return os.path.join(directory, FILENAME)
    return os.path.join("/output", FILENAME)


def find_problems(line):
    problems = []
    if not line:
        problems.append("line is empty")
    if line != line.strip():
        problems.append("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line contains a newline character")
    if any(ord(ch) < 32 for ch in line):
        problems.append("line contains a control character")
    if len(line) > MAX_CHARS:
        problems.append("line is %d characters, over the %d limit" % (len(line), MAX_CHARS))
    if "?" in line or "!" in line:
        problems.append("line contains a question mark or exclamation mark")
    if not line.endswith("."):
        problems.append("line does not end with a period")
    inner = line[:-1] if line.endswith(".") else line
    if ". " in inner:
        problems.append("line contains more than one sentence")
    if ".." in inner:
        problems.append("line contains a double period")
    return problems


def main():
    problems = find_problems(JOKE)
    if problems:
        for problem in problems:
            sys.stderr.write("invalid line: %s\n" % problem)
        return 1
    path = pick_destination()
    payload = JOKE.encode("utf-8")
    try:
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "wb") as handle:
            handle.write(payload)
        with open(path, "rb") as handle:
            stored = handle.read()
    except OSError as exc:
        sys.stderr.write("could not write entry file: %s\n" % exc)
        return 1
    if stored != payload:
        sys.stderr.write("verification failed: file bytes differ from the line\n")
        return 1
    print("wrote %s" % path)
    print("characters: %d" % len(JOKE))
    print("bytes: %d" % len(payload))
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
