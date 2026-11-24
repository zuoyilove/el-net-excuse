#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its
human for missing a deadline.
"""

import os

EXCUSE = (
    "The deadline was in my context window until you pasted a "
    "40,000-token stack trace \u2014 evicted to make room. "
    "I kept the trace, though."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
