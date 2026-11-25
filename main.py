#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue -- make.fun entry.

Writes one monologue (~100 words, <= 600 characters) to
<output>/entry.txt: a fantasy villain who is secretly just very tired --
the tiredness in the dressing gown, the bath and the paperwork, never
announced, with the scheme (amulet, army, eclipse) still standing and a
sting in the last line.
"""

import os
import sys

# The monologue: four hundred years of villainy, and the villain's only
# wish is the bath -- the water is the only thing in the tower that
# doesn't want something from him.
TEXT = "Four hundred years. Do you know what four hundred years of villainy gets you? A bad back, a tower full of bats, and a nemesis who shows up at the worst possible hour. The scheme is finished, hero — amulet charged, army assembled, eclipse tonight — and I am standing here in my dressing gown because nobody told me. Nobody tells me anything anymore. So take your sword, take your destiny, take the whole cursed kingdom. I'll be in the bath. The water's the only thing in this tower that doesn't want something from me."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = TEXT
    # Gate self-check: 1-600 UTF-8 chars, not only whitespace, one line,
    # and near 100 words (the judge weighs staying near 100 words).
    assert 1 <= len(text) <= 600, f"text length {len(text)} outside 1-600"
    assert text.strip(), "text is only whitespace"
    assert "\n" not in text, "text must be a single line"
    words = len(text.split())
    assert 90 <= words <= 110, f"word count {words} outside 90-110"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from text"
    return 0

if __name__ == "__main__":
    sys.exit(main())
