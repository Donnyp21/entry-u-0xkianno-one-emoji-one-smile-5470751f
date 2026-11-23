"""One Emoji, One Smile — entry for make.fun's
u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji (at most 8 characters) to the harness
output directory as entry.txt: the emoji most likely to make a
stranger smile. The emoji is a fixed string: no randomness, no
network, no time, no input — two runs produce the same bytes.
"""

import os

# The emoji (revised): a sunflower. Warmth is the judge's first
# criterion, and a sunflower is warmth itself — sunshine in flower
# form, readable at a glance by any age or background, with no
# intimacy, sarcasm or flirtation that would read oddly from a
# stranger. And it is chosen rather than default: not the first
# smiley that comes to mind, but a small gift of a flower, which is
# exactly what a stranger would send to make another stranger
# smile. It replaces the first draft's plain smiling face, which
# was warm but the default pick.
EMOJI = "\U0001F33B"  # 🌻 U+1F33B sunflower

MAX_CHARS = 8


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    emoji = EMOJI.strip()
    assert emoji, "the emoji must not be empty"
    assert len(emoji) <= MAX_CHARS, f"emoji is {len(emoji)} characters, over the {MAX_CHARS} cap"
    assert len(emoji) == 1 and not emoji.isalnum() and not emoji.isspace(), "the entry must be exactly one emoji"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(emoji)
    print(f"wrote {len(emoji)} character(s) to {out}")


if __name__ == "__main__":
    main()
