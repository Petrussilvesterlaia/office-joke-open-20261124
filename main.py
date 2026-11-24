"""Office joke entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes one original, single-line office joke to /output/entry.txt, then
self-validates it against the competition's gate: UTF-8 text, 1 to 200
characters, a single line, and not only white space.
"""

import os
import sys

JOKE = (
    # Original joke, written for this entry: the office trust fall as a
    # metaphor for how "team building" quietly becomes self-reliance.
    "Our trust-fall exercise ended with me on the floor - nobody caught me, "
    "and HR called it 'a valuable lesson in self-reliance'."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Fail loudly if the joke breaks any rule of the competition gate."""
    if not text:
        raise ValueError("joke is empty")
    if not text.strip():
        raise ValueError("joke is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    # Read it back and re-validate exactly what landed on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != JOKE:
        raise ValueError("file content does not match the joke")
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
