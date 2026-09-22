#!/usr/bin/env python3
"""Drive repeatable Ghidra headless decompilation for one local artifact."""

from __future__ import annotations

import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--ghidra-home")
    parser.add_argument("--dry-run", action="store_true")
    parser.parse_args()
    print(json.dumps({"status": "unsupported"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
