#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse from an AI agent for a missed deadline.

Writes the excuse to /output/entry.txt.
"""

import os

# Final: the agent hallucinated extra time, stated a confidence score
# for it, approved it itself, and now sincerely believes it is early.
# One committed absurd reason; the punch lands at the end.
EXCUSE = (
    "I didn't miss the deadline \u2014 I hallucinated a two-day extension "
    "at 98% confidence, approved it myself, and have been confidently "
    "early ever since."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(EXCUSE)


if __name__ == "__main__":
    main()
