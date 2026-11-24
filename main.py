#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text - an alien tourist's review of
planet Earth - to entry.txt in the output directory.

Deterministic: the line is a constant, no input is read, no network
access, no environment secrets. The output directory is taken from the
MAKEFUN_OUTPUT_DIR environment variable when set, otherwise from
OUTPUT_DIR, otherwise a local "output" directory (for local testing).
"""

import os

ENTRY = (
    "Visited Earth: once a year, the locals set their dessert on fire, "
    "make a wish, then blow it out. 4/5 stars \u2014 I wished for a refund."
)


def main() -> None:
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "output"
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
