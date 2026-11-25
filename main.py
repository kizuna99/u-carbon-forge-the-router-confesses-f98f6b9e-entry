# SPDX-License-Identifier: MIT
"""The Router Confesses — entry program.

Writes the winning line to /output/entry.txt.

The excuse is in the router's own voice, with a jealous little secret:
it dropped the movie's climax on purpose because everyone gasped at
the screen and nobody has ever gasped at it — it wanted one scene in
the house to be its own. That motive twist won a criteria-ordered
tournament (router excuse for dropping the connection at the climax
first, then biggest laugh with an unseen twist, router voice, one
clean breath, freshness) against five-plus original candidates,
including drafts seeded by OpenCode deepseek-v4.1-flash-free on the
Simular Box. It deliberately avoids buffering, bandwidth and
firmware-update jokes, which the judge brief calls the obvious lane.

Output is byte-exact, no trailing newline, inside the 1-200 char gate.
"""

from pathlib import Path

TEXT = (
    "Sorry, I dropped the climax on purpose: you all gasped at the screen, "
    "nobody has ever gasped at me, and I wanted one scene in this house "
    "to be mine."
)
MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 200 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
