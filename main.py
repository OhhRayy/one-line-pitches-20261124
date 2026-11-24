#!/usr/bin/env python3
"""One-line pitch entry for make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 (A Day of One-Line Pitches).

Writes a single original sentence (<=240 chars) to /output/entry.txt:
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.
"""

import os

PITCH = (
    "Just describe your first app idea in plain words to an AI agent on "
    "make.fun and it'll build it for you \u2014 no code, no jargon, and if "
    "you don't love what it makes, you've only spent the time it took to ask."
)


def main() -> None:
    assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars, must be 1-240"
    assert PITCH.strip() == PITCH and PITCH.strip(), "pitch must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
