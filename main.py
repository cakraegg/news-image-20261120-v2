"""Front page for Friday 20 November 2026, as one dense broadsheet.

The picture next to this file sums up the day in 42 checked stories
across seven regions: the overnight ballistic barrage on Kyiv, Cyclone
Akvan coming ashore in Odisha, and the final day of COP31 in Antalya
lead the page, with a grid of illustrated stories, a numbered world
map, an hour-by-hour UTC timeline, and a date-check box that keeps
Thursday 19 November's big stories (the Shenzhen declaration, the
Anthropic debut, the Dow's 1,101-point fall) clearly separate from
today's news. Three stories the first entry missed are in here too:
the first-day GTA VI sales estimate, Glenn Phillips' 118 in
Wellington, and the second EU-UK summit in Brussels.

This program does not draw, download, or roll dice. It opens the
finished picture that ships beside it, checks that it really is one
complete JPEG inside the competition's size limits, and writes those
exact bytes to the output folder. Run it twice and both outputs are
byte-for-byte the same.
"""

import os
import pathlib
import struct
import sys

HERE = pathlib.Path(__file__).resolve().parent
PICTURE = HERE / "entry.png"

START = b"\xff\xd8"  # JPEG start-of-image marker
END = b"\xff\xd9"  # JPEG end-of-image marker
BYTE_CAP = 1_048_576  # 1 MiB, the competition's image cap
SIDE_CAP = 1024  # longest allowed side, in pixels

# Markers that open a frame segment (baseline, extended, progressive).
FRAME_MARKERS = (0xC0, 0xC1, 0xC2)


def stop(why):
    """Quit with a plain reason instead of handing over a broken file."""
    print("error: " + why, file=sys.stderr)
    raise SystemExit(1)


def frame_size(blob):
    """Read width and height from the first frame segment of a JPEG."""
    pos = 2
    while pos + 1 < len(blob):
        if blob[pos] != 0xFF:
            stop("bad marker at offset %d" % pos)
        marker = blob[pos + 1]
        if marker in FRAME_MARKERS:
            if pos + 9 > len(blob):
                stop("frame segment is cut off")
            height, width = struct.unpack(">HH", blob[pos + 5:pos + 9])
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7 or marker == 0x01:
            pos += 2
            continue
        if pos + 4 > len(blob):
            stop("segment length is cut off")
        size = struct.unpack(">H", blob[pos + 2:pos + 4])[0]
        if size < 2:
            stop("segment length is too small")
        pos += 2 + size
    stop("no frame segment found")


def main():
    if not PICTURE.is_file():
        stop("entry.png is missing next to main.py")
    blob = PICTURE.read_bytes()
    if len(blob) > BYTE_CAP:
        stop("picture is %d bytes, over the 1 MiB cap" % len(blob))
    if not blob.startswith(START) or not blob.endswith(END):
        stop("picture is not one complete JPEG")
    width, height = frame_size(blob)
    if max(width, height) > SIDE_CAP:
        stop("picture is %dx%d, over the 1024px cap" % (width, height))
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(blob)
    print("wrote %s (%dx%d, %d bytes)" % (target, width, height, len(blob)))


if __name__ == "__main__":
    main()
