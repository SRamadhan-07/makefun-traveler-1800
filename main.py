#!/usr/bin/env python3
"""Traveler from 1800 — a make.fun entry.

The program writes one sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): the modern internet explained to a
traveler who has just arrived from the year 1800, built from things
that year already knows. The sentence is 167 characters, inside the
competition's gate of 1 to 200 characters of UTF-8 text. Standard
library only, no network, and deterministic: the same bytes on
every run.
"""

import os

LINE = "Imagine a postal service where every letter ever written arrives instantly, anyone may read over your shoulder, and half the town argues with strangers in the margins."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one sentence: no trailing newline,
    # so the text the judge reads is the sentence itself, byte for byte —
    # the gate counts characters, and a trailing newline would spend one.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
