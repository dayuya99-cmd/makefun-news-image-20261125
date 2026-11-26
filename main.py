"""news-image-20261125 entry: copy the built image to the output directory.

The image (768x1024, 25 November 2026 world news) lives in this repo as
entry.png; this program copies it to $MAKEFUN_OUTPUT_DIR/entry.png.
Standard library only, no network.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png missing next to main.py")
    with open(SRC, "rb") as f:
        head = f.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_hash = hashlib.sha256(open(SRC, "rb").read()).hexdigest()
    dst_hash = hashlib.sha256(open(DST, "rb").read()).hexdigest()
    if src_hash != dst_hash:
        raise SystemExit("copy mismatch: output differs from entry.png")
    print("wrote", DST, os.path.getsize(DST), "bytes, sha256", dst_hash[:16])


if __name__ == "__main__":
    main()
