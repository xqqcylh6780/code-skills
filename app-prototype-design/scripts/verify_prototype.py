#!/usr/bin/env python3
"""Audit a portable mobile app prototype against its declared contract.

Static checks use only the Python standard library. Browser checks are optional and
use an already-installed Python Playwright package; this script never installs it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit


@dataclass(frozen=True)
class AuditIssue:
    code: str
    message: str


class PrototypeMarkup(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.screens: set[str] = set()
        self.duplicate_screens: set[str] = set()
        self.routes: list[tuple[str | None, str]] = []
        self.routes_by_screen: dict[str, set[str]] = defaultdict(set)
        self.back_paths: list[tuple[str | None, str]] = []
        self.nav_items: list[dict[str, Any]] = []
        self.modals: set[str] = set()
        self.modal_opens: list[tuple[str | None, str]] = []
        self.modal_closes: set[str] = set()
        self.images: list[str] = []
        self.contract_reference: str | None = None
        self._stack: list[tuple[str, str | None, int | None]] = []

    @property
    def current_screen(self) -> str | None:
        for _, screen_id, _ in reversed(self._stack):
            if screen_id:
                return screen_id
        return None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name: value or "" for name, value in attrs}
        screen_id = values.get("data-screen") or None
        if screen_id:
            if screen_id in self.screens:
                self.duplicate_screens.add(screen_id)
            self.screens.add(screen_id)

        owner = screen_id or self.current_screen
        route = values.get("data-route-to")
        if route:
            self.routes.append((owner, route))
            if owner:
                self.routes_by_screen[owner].add(route)

        back_to = values.get("data-back-to")
        if back_to:
            self.back_paths.append((owner, back_to))
            if owner:
                self.routes_by_screen[owner].add(back_to)

        nav_index = None
        if "data-nav-item" in values:
            nav_index = len(self.nav_items)
            self.nav_items.append(
                {"route": route or "", "text": "", "label": values.get("data-nav-label", "")}
            )

        modal_id = values.get("data-modal")
        if modal_id:
            self.modals.add(modal_id)
        modal_open = values.get("data-modal-open")
        if modal_open:
            self.modal_opens.append((owner, modal_open))
        modal_close = values.get("data-modal-close")
        if modal_close:
            self.modal_closes.add(modal_close)

        if tag.lower() == "img" and values.get("src"):
            self.images.append(values["src"])
        if tag.lower() == "body" and values.get("data-prototype-contract"):
            self.contract_reference = values["data-prototype-contract"]

        self._stack.append((tag.lower(), screen_id, nav_index))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        for _, _, nav_index in self._stack:
            if nav_index is not None:
                self.nav_items[nav_index]["text"] += data

    def handle_endtag(self, tag: str) -> None:
        target = tag.lower()
        for index in range(len(self._stack) - 1, -1, -1):
            if self._stack[index][0] == target:
                del self._stack[index:]
                break


def _issue(code: str, message: str) -> AuditIssue:
    return AuditIssue(code=code, message=message)


def _normalise_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _load_contract(html_path: Path, contract_path: Path | str | None, markup: PrototypeMarkup):
    if contract_path is None:
        reference = markup.contract_reference or "prototype-contract.json"
        contract = html_path.parent / unquote(urlsplit(reference).path)
    else:
        contract = Path(contract_path)
    contract = contract.resolve()
    return contract, json.loads(contract.read_text(encoding="utf-8"))


def audit_prototype(
    html_path: Path | str,
    contract_path: Path | str | None = None,
) -> list[AuditIssue]:
    """Return contract and markup problems found in a prototype."""

    html = Path(html_path).resolve()
    issues: list[AuditIssue] = []
    if not html.is_file():
        return [_issue("missing-html", f"Prototype HTML does not exist: {html}")]

    markup = PrototypeMarkup()
    markup.feed(html.read_text(encoding="utf-8"))

    try:
        _, contract = _load_contract(html, contract_path, markup)
    except FileNotFoundError as error:
        return [_issue("missing-contract", f"Contract does not exist: {error.filename}")]
    except json.JSONDecodeError as error:
        return [_issue("invalid-contract", f"Contract JSON is invalid: {error}")]

    expected_screens = set(contract.get("screens", []))
    for screen_id in sorted(expected_screens - markup.screens):
        issues.append(_issue("missing-screen", f"Declared screen '{screen_id}' is absent from HTML."))
    for screen_id in sorted(markup.screens - expected_screens):
        issues.append(_issue("undeclared-screen", f"HTML screen '{screen_id}' is absent from the contract."))
    for screen_id in sorted(markup.duplicate_screens):
        issues.append(_issue("duplicate-screen", f"Screen id '{screen_id}' is declared more than once."))

    for owner, target in markup.routes + markup.back_paths:
        if target not in markup.screens:
            location = f" from '{owner}'" if owner else ""
            issues.append(_issue("unknown-route", f"Route target '{target}'{location} does not exist."))

    declared_nav = contract.get("primaryNavigation", [])
    actual_nav = {
        item["route"]: _normalise_text(item["label"] or item["text"])
        for item in markup.nav_items
    }
    declared_nav_ids = {item.get("id", "") for item in declared_nav}
    for item in declared_nav:
        route_id = item.get("id", "")
        label = _normalise_text(str(item.get("label", "")))
        if route_id not in actual_nav:
            issues.append(_issue("missing-nav-item", f"Primary navigation item '{route_id}' is absent."))
        elif actual_nav[route_id] != label:
            issues.append(
                _issue(
                    "nav-label-mismatch",
                    f"Navigation '{route_id}' is labeled '{actual_nav[route_id]}', expected '{label}'.",
                )
            )
    for route_id in sorted(set(actual_nav) - declared_nav_ids):
        issues.append(_issue("unexpected-nav-item", f"Navigation item '{route_id}' is not declared."))

    for subpage in contract.get("subpages", []):
        screen_id = subpage.get("id", "")
        expected_back = subpage.get("backTo", "")
        if (screen_id, expected_back) not in markup.back_paths:
            issues.append(
                _issue(
                    "missing-back",
                    f"Subpage '{screen_id}' has no back control targeting '{expected_back}'.",
                )
            )

    declared_modals = set(contract.get("modals", []))
    open_modals = {modal_id for _, modal_id in markup.modal_opens}
    for modal_id in sorted(declared_modals):
        if modal_id not in markup.modals:
            issues.append(_issue("missing-modal", f"Declared modal '{modal_id}' is absent."))
        if modal_id not in open_modals:
            issues.append(_issue("missing-modal-trigger", f"Modal '{modal_id}' has no open control."))
        if modal_id not in markup.modal_closes:
            issues.append(_issue("missing-modal-close", f"Modal '{modal_id}' has no close control."))
    for _, modal_id in markup.modal_opens:
        if modal_id not in markup.modals:
            issues.append(_issue("unknown-modal", f"Modal trigger targets missing modal '{modal_id}'."))

    core_flow = contract.get("coreFlow", [])
    for source, target in zip(core_flow, core_flow[1:]):
        if target not in markup.routes_by_screen.get(source, set()):
            issues.append(
                _issue(
                    "broken-core-flow",
                    f"Core flow has no control routing from '{source}' to '{target}'.",
                )
            )

    for source in markup.images:
        parsed = urlsplit(source)
        if parsed.scheme in {"http", "https", "data", "blob"} or source.startswith("//"):
            continue
        asset_path = html.parent / unquote(parsed.path.lstrip("/"))
        if not asset_path.is_file():
            issues.append(_issue("missing-asset", f"Image asset does not exist: {source}"))

    return issues


def _find_path(markup: PrototypeMarkup, start: str, target: str) -> list[str] | None:
    queue: deque[list[str]] = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        if path[-1] == target:
            return path
        for next_screen in markup.routes_by_screen.get(path[-1], set()):
            if next_screen not in visited:
                visited.add(next_screen)
                queue.append([*path, next_screen])
    return None


def browser_audit(
    html_path: Path | str,
    contract_path: Path | str | None = None,
    screenshot_dir: Path | str | None = None,
) -> list[AuditIssue]:
    """Exercise navigation, back paths, modals, assets, and responsive overflow."""

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return [
            _issue(
                "browser-unavailable",
                "Python Playwright is not installed. Install it only with user authorization, or use the available Playwright skill/tool.",
            )
        ]

    html = Path(html_path).resolve()
    markup = PrototypeMarkup()
    markup.feed(html.read_text(encoding="utf-8"))
    try:
        _, contract = _load_contract(html, contract_path, markup)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        return [_issue("browser-setup", f"Cannot load prototype contract: {error}")]

    issues: list[AuditIssue] = []
    console_errors: list[str] = []
    page_errors: list[str] = []
    captures = Path(screenshot_dir).resolve() if screenshot_dir else None
    if captures:
        captures.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.goto(html.as_uri(), wait_until="load")

        instances = page.locator("[data-prototype-instance]")
        if instances.count() == 0:
            issues.append(_issue("missing-instance", "No [data-prototype-instance] was rendered."))
        else:
            instance = instances.first
            nav = instance.locator("[data-nav-item]")
            expected_labels = [_normalise_text(str(item.get("label", ""))) for item in contract.get("primaryNavigation", [])]
            actual_labels = [
                _normalise_text(nav.nth(index).get_attribute("data-nav-label") or nav.nth(index).inner_text())
                for index in range(nav.count())
            ]
            if actual_labels != expected_labels:
                issues.append(_issue("browser-nav-mismatch", f"Rendered navigation is {actual_labels}, expected {expected_labels}."))

            for item in contract.get("primaryNavigation", []):
                route_id = item.get("id", "")
                control = instance.locator(f'[data-nav-item][data-route-to="{route_id}"]')
                if control.count() == 0:
                    continue
                control.click()
                if not instance.locator(f'[data-screen="{route_id}"]:visible').is_visible():
                    issues.append(_issue("nav-click-failed", f"Clicking navigation '{route_id}' did not show its screen."))

            start = contract.get("primaryNavigation", [{}])[0].get("id", "")
            primary_routes = {
                item.get("id", "") for item in contract.get("primaryNavigation", [])
            }

            def return_to_primary() -> None:
                for _ in range(len(contract.get("screens", []))):
                    visible = instance.locator("[data-screen]:visible").first
                    current = visible.get_attribute("data-screen") or ""
                    if current in primary_routes:
                        return
                    back_control = visible.locator("[data-back-to]").first
                    if back_control.count() == 0:
                        return
                    back_control.click()

            for subpage in contract.get("subpages", []):
                return_to_primary()
                target = subpage.get("id", "")
                back_to = subpage.get("backTo", "")
                path = _find_path(markup, start, target)
                if not path:
                    issues.append(_issue("unreachable-subpage", f"No route path reaches subpage '{target}'."))
                    continue
                instance.locator(f'[data-nav-item][data-route-to="{start}"]').click()
                for source, destination in zip(path, path[1:]):
                    instance.locator(
                        f'[data-screen="{source}"]:visible [data-route-to="{destination}"]'
                    ).first.click()
                back = instance.locator(
                    f'[data-screen="{target}"]:visible [data-back-to="{back_to}"]'
                )
                if back.count() == 0:
                    continue
                back.click()
                if not instance.locator(f'[data-screen="{back_to}"]:visible').is_visible():
                    issues.append(_issue("back-click-failed", f"Back from '{target}' did not show '{back_to}'."))

            for owner, modal_id in markup.modal_opens:
                if not owner:
                    continue
                return_to_primary()
                path = _find_path(markup, start, owner)
                if not path:
                    issues.append(_issue("unreachable-modal", f"No route path reaches modal trigger '{modal_id}'."))
                    continue
                instance.locator(f'[data-nav-item][data-route-to="{start}"]').click()
                for source, destination in zip(path, path[1:]):
                    instance.locator(
                        f'[data-screen="{source}"]:visible [data-route-to="{destination}"]'
                    ).first.click()
                instance.locator(
                    f'[data-screen="{owner}"]:visible [data-modal-open="{modal_id}"]'
                ).first.click()
                modal = instance.locator(f'[data-modal="{modal_id}"]:visible')
                if not modal.is_visible():
                    issues.append(_issue("modal-open-failed", f"Modal '{modal_id}' did not become visible."))
                    continue
                modal.locator(f'[data-modal-close="{modal_id}"]').first.click()
                if instance.locator(f'[data-modal="{modal_id}"]:visible').count():
                    issues.append(_issue("modal-close-failed", f"Modal '{modal_id}' did not close."))

        broken_images = page.locator("img").evaluate_all(
            "images => images.filter(image => !image.complete || image.naturalWidth === 0).map(image => image.getAttribute('src'))"
        )
        for source in broken_images:
            issues.append(_issue("browser-image-failed", f"Image failed to render: {source}"))

        if captures:
            page.screenshot(path=str(captures / "desktop-overview.png"), full_page=True)
        page.set_viewport_size({"width": 390, "height": 844})
        if page.evaluate("document.documentElement.scrollWidth > window.innerWidth"):
            issues.append(_issue("mobile-overflow", "Prototype has horizontal overflow at 390x844."))
        if captures:
            page.screenshot(path=str(captures / "mobile-entry.png"), full_page=True)

        browser.close()

    for message in console_errors:
        issues.append(_issue("console-error", message))
    for message in page_errors:
        issues.append(_issue("page-error", message))
    return issues


def _print_report(issues: list[AuditIssue], as_json: bool) -> None:
    if as_json:
        print(json.dumps([issue.__dict__ for issue in issues], ensure_ascii=False, indent=2))
    elif not issues:
        print("Prototype audit passed.")
    else:
        for issue in issues:
            print(f"[{issue.code}] {issue.message}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="Path to the prototype HTML entry point")
    parser.add_argument("--contract", type=Path, help="Path to prototype-contract.json")
    parser.add_argument("--browser", action="store_true", help="Run optional browser-backed interaction checks")
    parser.add_argument("--screenshot-dir", type=Path, help="Save desktop and phone screenshots during browser checks")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args(argv)

    issues = audit_prototype(args.html, args.contract)
    if not issues and args.browser:
        issues.extend(browser_audit(args.html, args.contract, args.screenshot_dir))
    _print_report(issues, args.json)
    if any(issue.code == "browser-unavailable" for issue in issues):
        return 2
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
