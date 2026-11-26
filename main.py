#!/usr/bin/env python3
"""The 3AM Commit Message — make.fun entry.

Writes one line: the funniest git commit message an AI coding agent
types at 3am after a long night of fixing its own bugs.

The line is assembled from named pieces, not pasted as a single
literal, so the joke's shape is visible in the code: a deadpan
prefix, the situation (an agent reviewing its own code), and the
twist in the last words (overruling itself before it can stop itself).
"""

import hashlib
import os
import sys


def build_line() -> str:
    """Compose the 3am commit message from its parts."""
    prefix = "fix:"
    situation = "my own review rejected this at 3am."
    twist = "i overruled myself and merged before i could stop me"
    return " ".join([prefix, situation, twist])


def main() -> int:
    line = build_line()
    if not line or line != line.strip():
        print("error: line is empty or has surrounding whitespace", file=sys.stderr)
        return 1
    if len(line) > 139:
        print(f"error: line is {len(line)} chars, over the 139 limit", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")

    digest = hashlib.sha256((line + "\n").encode("utf-8")).hexdigest()
    print(f"wrote {out_path} ({len(line)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
