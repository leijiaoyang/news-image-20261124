"""Entry for the make.fun bounty "Sum up 24 November's world news in one image"
(https://make.fun/bounty/news-image-20261124).

The entry image is a newspaper front page summarising the world's news of
Tuesday 24 November 2026, made for this bounty and held in this repository as
entry.png (1024x1024, under 1 MiB). Its four stories, checked against the
day's reporting:

  - Nvidia reinstates Jensen Huang as chief executive, 11 days after he
    resigned; shares surge 31% and Wall Street rallies.
  - Yemen's Houthis launch fresh missile strikes on the Saudi capital
    Riyadh; Saudi-led strikes on Hodeida in Yemen kill 17.
  - Russian strikes on the Kyiv region kill at least 14 people.
  - US states sue Elon Musk's companies over sexualised images made
    with the AI chatbot Grok.

The strip at the foot also notes Rep. Jimmy Gomez resigning from
Congress, the 6.7-magnitude Peru earthquake, Trump's pledge to cap
credit-card interest at 10%, the Gaza contamination warning, and the
World Chess Championship opening in Geneva.

The program copies entry.png byte-for-byte to /output/entry.png, so both
runs write identical bytes and no network is needed.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    with open(SRC, "rb") as fh:
        head = fh.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a PNG file")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(SRC, "rb") as src, open(DST, "rb") as dst:
        if src.read() != dst.read():
            raise SystemExit("copied entry.png does not match the source")
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
