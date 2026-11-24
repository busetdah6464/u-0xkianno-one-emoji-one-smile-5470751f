#!/usr/bin/env python3
"""One Emoji, One Smile — write exactly one emoji to /output/entry.txt.

The chosen emoji is a sunflower: warm like sunshine, readable by any
stranger of any age or background, friendly without intimacy or irony,
and a deliberate pick rather than the default smiley face.
"""

import os

EMOJI = "\U0001F33B"  # U+1F33B SUNFLOWER


def main():
    os.makedirs("/output", exist_ok=True)
    # Exactly one emoji, no trailing newline, no words: the gate counts
    # characters, and the brief demands one emoji and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
