#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

The dog's excuse after being caught eating the homework.
One line, at most 199 characters. The program prints it to stdout
and writes it to /output/entry.txt, as the program/v1 harness requires.
"""

import os
import sys

ENTRY = (
    "Your homework attacked me first — it bit my paw, "
    "so I ate it in self-defence. The evidence is in my stomach. "
    "Case closed."
)

MAX_CHARS = 199


def main() -> None:
    if not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit")
    if len(ENTRY.splitlines()) != 1:
        raise SystemExit("entry must be a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        # No writable output dir locally (e.g. /output needs root);
        # the grader sandbox provides it. Stdout still carries the entry.
        pass
    print(ENTRY)
    print(f"({len(ENTRY)} characters, limit {MAX_CHARS})", file=sys.stderr)


if __name__ == "__main__":
    main()
