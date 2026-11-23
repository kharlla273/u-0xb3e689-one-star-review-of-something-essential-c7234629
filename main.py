"""One-Star Review of Something Essential — make.fun entry.

Writes a single-line, deadpan one-star review of an everyday essential
(sleep) to /output/entry.txt. The review is a fixed, hand-written text:
deterministic, no network, no randomness, no model calls.

Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space, on a single line.
"""

import os
from pathlib import Path

# The review. Deadpan complaint, sharpest true grievance first (eight
# hours charged every night), sting in the last few words.
REVIEW = (
    "Sleep charges eight hours a night and delivers a sore neck "
    "and a 3 a.m. meeting with my own thoughts."
)

MAX_CHARS = 160


def validate(text: str) -> None:
    """Enforce the gate locally: 1-160 chars, single line, non-blank."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"review is {len(text)} chars, must be 1-160")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not text.strip():
        raise ValueError("review must not be only white space")


def main() -> Path:
    validate(REVIEW)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    # No trailing newline: the file is exactly the one-line review.
    out_path.write_text(REVIEW, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    path = main()
    print(f"wrote {path} ({len(REVIEW)} chars)")
