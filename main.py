#!/usr/bin/env python3
"""One-Line Office Joke entry.

Writes one original office-life joke, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The joke: a setup-and-punchline one-liner about the meeting that
should have been an email, with the punchline escalating the joke.
"""

import os

# The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, on a single line.
MAX_CHARS = 200

JOKE = (
    "I told my boss this meeting could have been an email, "
    "so he booked a follow-up meeting to discuss my attitude "
    "toward meetings."
)


def main() -> None:
    text = JOKE.strip()
    if not text:
        raise ValueError("joke must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(text)} characters, must be at most {MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
