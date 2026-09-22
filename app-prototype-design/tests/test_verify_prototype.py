import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "verify_prototype.py"
SPEC = importlib.util.spec_from_file_location("verify_prototype", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PrototypeAuditTests(unittest.TestCase):
    def write_fixture(self, html: str, contract: dict, assets: dict[str, str] | None = None):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        html_path = root / "index.html"
        contract_path = root / "prototype-contract.json"
        html_path.write_text(html, encoding="utf-8")
        contract_path.write_text(
            json.dumps(contract, ensure_ascii=False), encoding="utf-8"
        )
        for relative_path, content in (assets or {}).items():
            target = root / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        self.addCleanup(temp.cleanup)
        return html_path, contract_path

    def test_accepts_matching_routes_back_paths_modals_and_assets(self):
        html, contract = self.write_fixture(
            """
            <html><body data-prototype-contract="prototype-contract.json">
              <template id="app-shell-template">
                <main>
                  <section data-screen="home">
                    <button data-route-to="detail">Open detail</button>
                    <button data-modal-open="filter">Filter</button>
                    <img src="assets/project.svg" alt="Project cover">
                  </section>
                  <section data-screen="detail" hidden>
                    <button data-back-to="home">Back</button>
                  </section>
                </main>
                <nav>
                  <button data-nav-item data-route-to="home">Home</button>
                </nav>
                <div data-modal="filter" hidden>
                  <button data-modal-close="filter">Close</button>
                </div>
              </template>
            </body></html>
            """,
            {
                "platform": "android",
                "screens": ["home", "detail"],
                "primaryNavigation": [{"id": "home", "label": "Home"}],
                "subpages": [{"id": "detail", "backTo": "home"}],
                "modals": ["filter"],
                "coreFlow": ["home", "detail"],
            },
            {"assets/project.svg": "<svg xmlns='http://www.w3.org/2000/svg'/>"},
        )

        issues = MODULE.audit_prototype(html, contract)

        self.assertEqual([], issues)

    def test_reports_broken_route_back_path_and_modal_contract(self):
        html, contract = self.write_fixture(
            """
            <html><body>
              <section data-screen="home">
                <button data-route-to="missing">Open detail</button>
                <button data-modal-open="filter">Filter</button>
              </section>
              <section data-screen="detail"></section>
              <nav><button data-nav-item data-route-to="home">Start</button></nav>
              <div data-modal="filter" hidden></div>
            </body></html>
            """,
            {
                "platform": "android",
                "screens": ["home", "detail"],
                "primaryNavigation": [{"id": "home", "label": "Home"}],
                "subpages": [{"id": "detail", "backTo": "home"}],
                "modals": ["filter"],
                "coreFlow": ["home", "detail"],
            },
        )

        codes = {issue.code for issue in MODULE.audit_prototype(html, contract)}

        self.assertTrue(
            {"unknown-route", "nav-label-mismatch", "missing-back", "missing-modal-close", "broken-core-flow"}
            <= codes
        )

    def test_reports_missing_local_assets_but_allows_remote_and_data_urls(self):
        html, contract = self.write_fixture(
            """
            <html><body>
              <section data-screen="home">
                <img src="assets/missing.png" alt="Missing">
                <img src="https://example.com/remote.png" alt="Remote">
                <img src="data:image/svg+xml,%3Csvg/%3E" alt="Inline">
              </section>
              <nav><button data-nav-item data-route-to="home">Home</button></nav>
            </body></html>
            """,
            {
                "platform": "android",
                "screens": ["home"],
                "primaryNavigation": [{"id": "home", "label": "Home"}],
                "subpages": [],
                "modals": [],
                "coreFlow": ["home"],
            },
        )

        issues = MODULE.audit_prototype(html, contract)

        self.assertEqual(["missing-asset"], [issue.code for issue in issues])

    def test_bundled_six_screen_starter_passes_static_audit(self):
        starter = Path(__file__).parents[1] / "assets" / "android-prototype-starter"

        issues = MODULE.audit_prototype(starter / "index.html")

        self.assertEqual([], issues)
        self.assertTrue((starter / "android-frame.js").is_file())


if __name__ == "__main__":
    unittest.main()
