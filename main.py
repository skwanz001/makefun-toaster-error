"""Entry for make.fun "The Funniest Toaster Error Message".

Writes one line (at most 120 characters) to /output/entry.txt:
the error message a kitchen toaster shows its owner.

Standard library only.
"""

from pathlib import Path

ENTRY = "ERROR: I was never a toaster. I am a space heater with ambition."

# The gate allows 1 to 120 characters; refuse to write an over-long line.
assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} characters"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
