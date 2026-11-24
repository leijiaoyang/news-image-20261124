"""24 November 2026 in one picture.

Entry program for make.fun's "Sum up 24 November's world news in
one image" bounty (https://make.fun/bounty/news-image-20261124).

The repository ships a single front-page image, entry.png, 1024 by
1024 pixels and under a megabyte, drawn for Tuesday 24 November
2026. The masthead names the day; four lead stories fill a two-by-
two grid, each with a photograph and a one-line factual caption; a
further eight stories run under "More of the day"; three more sit in
the foot strip. The leads:

- Hacked registry data puts the Russian death toll in Ukraine near
  500,000.
- Allies warn Russia's Sputnik-S satellite could carry a nuclear
  warhead into orbit as soon as December.
- Trump orders federal executions to be sped up.
- China sentences an official to death for spying for a foreign
  country.

Running this program needs no network. It checks that entry.png is
a real PNG, copies it to /output/entry.png, and confirms the copy
is byte-for-byte the same, so a second run writes the same bytes.
"""

import hashlib
import sys
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")
MAGIC = bytes((0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A))
MAX_BYTES = 1_048_576


def is_png(path: Path) -> bool:
    with path.open("rb") as handle:
        return handle.read(len(MAGIC)) == MAGIC


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not is_png(ENTRY):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if ENTRY.stat().st_size > MAX_BYTES:
        print("entry.png is over the 1 MiB limit", file=sys.stderr)
        return 1
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(ENTRY.read_bytes())
    if sha256(TARGET) != sha256(ENTRY):
        print("copied entry.png does not match the source", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)"
          % (TARGET, TARGET.stat().st_size, sha256(TARGET)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
