"""Validate and optionally submit a typed Jev request from a UTF-8 JSON file."""

import argparse
import json
import math
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MAX_REQUEST_BYTES = 1024 * 1024


def validate(payload):
    if not isinstance(payload, dict):
        raise ValueError("request must be a JSON object")
    if not isinstance(payload.get("state"), (str, dict, list)):
        raise ValueError("state must be a string, object, or array")
    if not isinstance(payload.get("model", "jev-latest"), str):
        raise ValueError("model must be a string")
    questions = payload.get("questions")
    if not isinstance(questions, dict) or not questions:
        raise ValueError("questions must be a nonempty object")
    for key, question in questions.items():
        if not isinstance(key, str) or not isinstance(question, dict):
            raise ValueError("each question must have a string key and object value")
        kind = question.get("type")
        if kind not in ("noul", "choice", "score"):
            raise ValueError(f"{key}: type must be noul, choice, or score")
        if not isinstance(question.get("instructions"), (str, dict, list)):
            raise ValueError(f"{key}: instructions must be a string, object, or array")
        criteria = question.get("criteria")
        if kind == "choice" and (not isinstance(criteria, dict) or not 2 <= len(criteria) <= 255):
            raise ValueError(f"{key}: choice criteria must have 2 to 255 options")
        if kind == "score" and (not isinstance(criteria, list) or not 2 <= len(criteria) <= 10):
            raise ValueError(f"{key}: score criteria must have 2 to 10 levels")
    payload.setdefault("model", "jev-latest")
    return payload


def unit_interval(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and 0 <= value <= 1


def validate_answers(result, questions):
    if not isinstance(result, dict) or not isinstance(result.get("answers"), dict):
        raise ValueError("API returned no answers object")
    answers = result["answers"]
    if set(answers) != set(questions):
        raise ValueError("API answer keys do not match the requested questions")
    for key, question in questions.items():
        answer = answers[key]
        kind = question["type"]
        if not isinstance(answer, dict) or answer.get("type") != kind:
            raise ValueError(f"{key}: API answer type does not match the question")
        if kind == "noul":
            if not unit_interval(answer.get("noul")):
                raise ValueError(f"{key}: API returned an invalid noul value")
        else:
            if not unit_interval(answer.get("confidence")):
                raise ValueError(f"{key}: API returned an invalid confidence value")
            probabilities = answer.get("probabilities")
            if not isinstance(probabilities, dict) or not all(unit_interval(value) for value in probabilities.values()):
                raise ValueError(f"{key}: API returned invalid probabilities")
            if kind == "choice":
                if answer.get("choice") not in question["criteria"] or set(probabilities) != set(question["criteria"]):
                    raise ValueError(f"{key}: API choice or probabilities differ from the supplied options")
            else:
                score = answer.get("score")
                if not isinstance(score, (int, float)) or isinstance(score, bool) or not math.isfinite(score) or not 0 <= score <= len(question["criteria"]) - 1:
                    raise ValueError(f"{key}: API returned an invalid score")


def get_api_key():
    key = os.environ.get("TYPESAFE_API_KEY")
    if key or os.name != "nt":
        return key
    # A running Windows app does not inherit user environment changes made after launch.
    try:
        import winreg

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as environment:
            key, _ = winreg.QueryValueEx(environment, "TYPESAFE_API_KEY")
        return key
    except (OSError, ImportError):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", help="UTF-8 JSON request file, or - for standard input")
    parser.add_argument("--check", action="store_true", help="validate locally; do not call the API")
    args = parser.parse_args()

    try:
        raw = sys.stdin.buffer.read(MAX_REQUEST_BYTES + 1) if args.request == "-" else Path(args.request).read_bytes()
        if len(raw) > MAX_REQUEST_BYTES:
            raise ValueError("request exceeds 1 MiB; narrow the state before sending it")
        payload = validate(json.loads(raw.decode("utf-8")))
        if args.check:
            print("request valid")
            return 0

        api_key = get_api_key()
        if not api_key:
            raise ValueError("TYPESAFE_API_KEY is not set")
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request = urllib.request.Request(
            ENDPOINT,
            data=body,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.load(response)
        validate_answers(result, payload["questions"])
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, urllib.error.URLError) as exc:
        if isinstance(exc, urllib.error.HTTPError):
            message = f"API returned HTTP {exc.code}"
        elif isinstance(exc, urllib.error.URLError):
            message = f"API request failed: {exc.reason}"
        else:
            message = str(exc)
        print(message, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
