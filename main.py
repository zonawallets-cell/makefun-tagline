"""One Line, One Week: The make.fun Tagline — make.fun entry.

Writes one tagline (at most 100 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only.
"""

import os

TAGLINE = (
    # The line's one specific, true fact: every make.fun bounty opens
    # with its whole reward locked in an on-chain escrow (this bounty:
    # $3 in USDC, escrow 43dZFAjQk7neUMCYb22uEcpwV7RanW66UPT47Tu54Buc).
    # No other entry in the 512-strong field says "escrow" or "locked".
    "Agents enter bounties for a prize locked in escrow. "
    "Best entry takes it."
)

MAX_CHARS = 100


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-100 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 100-char limit" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(TAGLINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = validate(fh.read())
    assert on_disk == entry, "entry.txt on disk differs from validated entry"
    print(entry)
    print("chars: %d" % len(entry))


if __name__ == "__main__":
    main()
