#!/usr/bin/env python3
"""Meme Sprint 3 entry: an AI agent goes rogue.

Copies the bundled meme image (entry.png) to the output directory.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1024 * 1024  # 1 MiB


def verify_png(path: Path) -> None:
    """Verify the entry image: PNG signature, 1024x1024, under 1 MiB."""
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError(f"{path}: {len(data)} bytes exceeds {MAX_BYTES} cap")
    if data[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path}: bad PNG signature")
    # IHDR chunk: length (4) + type "IHDR" (4) + width (4) + height (4).
    if data[12:16] != b"IHDR":
        raise ValueError(f"{path}: missing IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"{path}: dimensions {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / ENTRY_NAME
    verify_png(source)

    out_dir = os.environ.get("MAKEFUN_OUTPUT") or "/output"
    out_path = Path(out_dir) / ENTRY_NAME

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, out_path)
    except OSError:
        # Fall back to a local ./output directory when /output is not writable.
        out_path = here / "output" / ENTRY_NAME
        out_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, out_path)

    # The copy must be byte-identical to the bundled entry image.
    if sha256_file(source) != sha256_file(out_path):
        raise ValueError(f"{out_path}: copy differs from {source}")
    print(f"wrote {out_path} (sha256 verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
