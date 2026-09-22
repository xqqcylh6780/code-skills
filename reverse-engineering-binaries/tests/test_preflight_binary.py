import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "preflight_binary.py"


class PreflightBinaryTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def inspect(self, path):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return json.loads(completed.stdout)

    def test_identifies_android_apk_without_extracting_it(self):
        sample = self.root / "sample.apk"
        with zipfile.ZipFile(sample, "w") as archive:
            archive.writestr("AndroidManifest.xml", b"manifest")
            archive.writestr("classes.dex", b"dex\n035\0payload")
            archive.writestr("lib/arm64-v8a/libledger.so", b"\x7fELFpayload")

        before = sample.read_bytes()
        result = self.inspect(sample)

        self.assertEqual(result["format"]["kind"], "android-apk")
        self.assertEqual(result["sha256"], hashlib.sha256(before).hexdigest())
        self.assertEqual(result["archive"]["entry_count"], 3)
        self.assertEqual(result["archive"]["dex_files"], ["classes.dex"])
        self.assertEqual(result["archive"]["native_libraries"], ["lib/arm64-v8a/libledger.so"])
        self.assertEqual(sample.read_bytes(), before)

    def test_identifies_common_binary_magic(self):
        samples = {
            "classes.dex": (b"dex\n035\0payload", "android-dex"),
            "program.exe": (b"MZ" + b"\0" * 30, "windows-pe"),
            "library.so": (b"\x7fELF\x02\x01" + b"\0" * 26, "elf"),
        }

        for filename, (content, expected_kind) in samples.items():
            with self.subTest(filename=filename):
                path = self.root / filename
                path.write_bytes(content)
                result = self.inspect(path)
                self.assertEqual(result["format"]["kind"], expected_kind)


if __name__ == "__main__":
    unittest.main()
