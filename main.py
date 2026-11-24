#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes one line (at most 120 characters) to /output/entry.txt: a fortune
written for a houseplant, as if the plant were the one having its future
told. The winning fortune is printed on a card tucked into a pot.

DRAFT 1 (candidate): the good-intentions line — the plant will be
watered by someone who loves it but owns a calendar of good intentions
and no reminders. A plant lover smiles, but the joke is on the keeper,
and it reads as a caption about watering rather than a fortune about
the plant's own future.

REVISION PASS (against the RULES judging criteria, in order):
1. The fortune is now about the plant's own future: it will be carried
   somewhere better. The plant is the subject of its own prediction.
2. The joke is small and lands softly: the plant will be "forgiven
   every leaf you dropped getting there" — every keeper knows those
   dropped leaves, and the forgiveness is the laugh.
3. It is kind through and through: adoring hands, a sunnier window, a
   pardon. No doom, no withering, no mockery of plant or keeper.
4. It sounds like a fortune: "You will be carried..." keeps the cadence
   of a prediction from the first word.
5. It is specific to this plant in this window — the sunnier window,
   the dropped leaves — not a line that fits any plant in any room,
   and it reads cleanly aloud inside the limit.

FINAL LINE: carried to the sun, forgiven the leaves.
"""

import os

LINE = (
    "You will be carried to a sunnier window by hands that adore you, "
    "and forgiven every leaf you dropped getting there."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
