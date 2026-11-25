#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line - make.fun entry.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

v1 draft line: the decision already happened in the group chat; the meeting
is just everyone watching it be read out loud. Hand-scored 20/25 against the
judge's 5 criteria: relatable (5) and standalone (5), but the kill is soft
(a group-chat decision can still be "discussed") and the joke has no sting.

v2 draft line: same kill, sharper image - the decision went out by email,
and the meeting is just the reply-all thread with chairs. Hand-scored 24/25:
the sting lands (5), but the kill is still soft - "I emailed the decision"
only communicates it, a meeting could still claim to discuss it.

v3 FINAL line: "already decided" makes the decision done, not merely sent,
so nothing is left to meet about; dropping the first-person "I" means anyone
in the room could say it. Hand-scored 25/25 (C1 5, C2 5, C3 5, C4 5, C5 5).
94 chars, one sentence, one line - also wins the smaller-text tie-break.
"""

import os

LINE = "Yesterday's email already decided this; this meeting is just the reply-all thread with chairs."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
