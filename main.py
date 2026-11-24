"""The Long Roast: Lawmakers and the File They Cannot Convert — entry.

Writes one fixed satirical sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR). No network, no randomness, no input. Deterministic:
every run writes byte-identical output.

The line: "The senator who wrote the AI Safety Act in Word believes Export
as PDF needs a floor vote, so the law now exists as 214 screenshots stapled
together in the record."

Why this line: the senator's authority (wrote the AI Safety Act) is set up
and undercut by the file (Export as PDF treated as a floor vote); the punch
is about the law itself (214 screenshots stapled together in the record);
no intern/aide/fax/printed-email cliché. 163 characters, inside the 1-320
gate, one sentence, punch on the last few words.
"""

import os
from pathlib import Path

TEXT = (
    "The senator who wrote the AI Safety Act in Word believes Export as PDF "
    "needs a floor vote, so the law now exists as 214 screenshots stapled "
    "together in the record."
)


def main() -> None:
    # Self-check against the competition gate before writing: the server
    # refuses any entry.txt outside 1-320 characters or blank, so fail
    # loudly here instead of silently shipping an invalid entry.
    if not 1 <= len(TEXT) <= 320 or not TEXT.strip():
        raise SystemExit("entry.txt must be 1-320 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
