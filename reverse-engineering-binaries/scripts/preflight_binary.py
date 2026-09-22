#!/usr/bin/env python3
"""Produce read-only metadata for a binary before reverse engineering."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
import zipfile
from pathlib import Path


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_format(prefix: bytes) -> dict:
    if prefix.startswith(b"dex\n") and len(prefix) >= 8 and prefix[7] == 0:
        version = prefix[4:7].decode("ascii", errors="replace")
        return {"kind": "android-dex", "dex_version": version}
    if prefix.startswith(b"\x7fELF"):
        elf_class = {1: "32-bit", 2: "64-bit"}.get(prefix[4] if len(prefix) > 4 else 0, "unknown")
        endian = {1: "little", 2: "big"}.get(prefix[5] if len(prefix) > 5 else 0, "unknown")
        return {"kind": "elf", "class": elf_class, "endianness": endian}
    if prefix.startswith(b"MZ"):
        result = {"kind": "windows-pe"}
        if len(prefix) >= 64:
            pe_offset = struct.unpack_from("<I", prefix, 0x3C)[0]
            result["pe_header_offset"] = pe_offset
        return result
    if prefix.startswith((b"\xfe\xed\xfa\xce", b"\xce\xfa\xed\xfe")):
        return {"kind": "mach-o", "class": "32-bit"}
    if prefix.startswith((b"\xfe\xed\xfa\xcf", b"\xcf\xfa\xed\xfe")):
        return {"kind": "mach-o", "class": "64-bit"}
    if prefix.startswith((b"\xca\xfe\xba\xbe", b"\xbe\xba\xfe\xca")):
        return {"kind": "mach-o-fat"}
    if prefix.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")):
        return {"kind": "zip-archive"}
    return {"kind": "unknown"}


def inspect_zip(path: Path, max_entries: int) -> tuple[dict, str | None]:
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
    names = [entry.filename.replace("\\", "/") for entry in entries]
    visible_names = names[:max_entries]
    dex_files = sorted(name for name in visible_names if name.endswith(".dex"))
    native_libraries = sorted(
        name for name in visible_names if name.startswith("lib/") and name.endswith(".so")
    )
    suspicious_paths = sum(
        1
        for name in visible_names
        if name.startswith(("/", "\\")) or ".." in Path(name).parts
    )
    encrypted_entries = sum(1 for entry in entries[:max_entries] if entry.flag_bits & 0x1)
    archive_info = {
        "entry_count": len(entries),
        "entries_inspected": min(len(entries), max_entries),
        "truncated": len(entries) > max_entries,
        "manifest_present": "AndroidManifest.xml" in visible_names,
        "dex_files": dex_files,
        "native_libraries": native_libraries,
        "encrypted_entries": encrypted_entries,
        "suspicious_paths": suspicious_paths,
        "uncompressed_size_bytes": sum(entry.file_size for entry in entries),
        "compressed_size_bytes": sum(entry.compress_size for entry in entries),
    }
    kind = "android-apk" if archive_info["manifest_present"] and dex_files else None
    return archive_info, kind


def inspect_binary(path: Path, max_archive_entries: int = 10_000) -> dict:
    if max_archive_entries < 1:
        raise ValueError("max_archive_entries must be at least 1")
    if not path.is_file():
        raise ValueError(f"not a regular file: {path}")
    with path.open("rb") as stream:
        prefix = stream.read(4096)
    detected_format = detect_format(prefix)
    result = {
        "schema_version": 1,
        "path": str(path.resolve()),
        "size_bytes": path.stat().st_size,
        "sha256": hash_file(path),
        "magic_hex": prefix[:16].hex(),
        "format": detected_format,
        "safety": {
            "sample_executed": False,
            "archive_extracted": False,
        },
    }
    if detected_format["kind"] == "zip-archive":
        try:
            archive_info, refined_kind = inspect_zip(path, max_archive_entries)
            result["archive"] = archive_info
            if refined_kind:
                result["format"] = {"kind": refined_kind}
        except (OSError, zipfile.BadZipFile) as exc:
            result["archive_error"] = str(exc)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--max-archive-entries", type=int, default=10_000)
    args = parser.parse_args()
    try:
        result = inspect_binary(args.path, args.max_archive_entries)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
