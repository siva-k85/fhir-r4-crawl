#!/usr/bin/env python3
"""Lightweight Google Gemini coding agent for this repository."""

from __future__ import annotations

import argparse
import glob
import os
import pathlib
import sys
import textwrap
from typing import Iterable, List

try:  # Lazy import so --dry-run works without the dependency installed yet
    import google.generativeai as genai
except ModuleNotFoundError:  # pragma: no cover - dependency is optional until runtime
    genai = None


DEFAULT_MODEL = "gemini-2.5-pro"
MAX_CONTEXT_CHARS = 60_000
PER_FILE_CHAR_LIMIT = 8_000


SYSTEM_PROMPT = textwrap.dedent(
    """You are an elite Google Gemini coding agent assisting inside the
    fhir-r4-crawl repository. Provide concise, actionable guidance that is ready to
    paste back into the codebase. Prefer concrete file paths, numbered steps, and
    diff-style snippets. If the provided context is insufficient, ask for more.
    Assume execution happens from the repo root and respect existing tooling.
    """
).strip()

def load_dotenv() -> None:
    """Load .env variables without requiring python-dotenv."""
    dotenv_path = pathlib.Path(__file__).resolve().parent.parent / ".env"
    if not dotenv_path.exists():
        return
    try:
        lines = dotenv_path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not key or key in os.environ:
            continue
        value = value.strip().strip('"').strip("'")
        os.environ[key] = value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a Gemini coding helper with optional repo context.",
    )
    parser.add_argument(
        "task",
        help="Describe what you want Gemini to do (bugfix, refactor, doc request, etc.)",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        default=[],
        help="File paths or glob patterns to include as context (e.g. src/**/*.py)",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Gemini model to call (default: %(default)s)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Creativity vs. determinism (0-1).",
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=2048,
        help="Upper bound on tokens returned by Gemini.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the payload that would be sent instead of calling the API.",
    )
    return parser.parse_args()


def discover_files(patterns: Iterable[str]) -> List[pathlib.Path]:
    files: List[pathlib.Path] = []
    seen = set()
    for pattern in patterns:
        for match in glob.glob(pattern, recursive=True):
            path = pathlib.Path(match)
            if path.is_dir():
                continue
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append(path)
    return sorted(files)


def load_context(files: Iterable[pathlib.Path]) -> str:
    contexts = []
    remaining = MAX_CONTEXT_CHARS
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        snippet = text[:PER_FILE_CHAR_LIMIT]
        block = f"### {path}\n{snippet}\n"
        block_len = len(block)
        if block_len > remaining:
            break
        contexts.append(block)
        remaining -= block_len
    return "\n".join(contexts)


def main() -> None:
    load_dotenv()
    args = parse_args()
    files = discover_files(args.files)
    context_blob = load_context(files) if files else ""

    prompt_sections = [f"Task:\n{args.task.strip()}" ]
    if context_blob:
        prompt_sections.append("Repository context:\n" + context_blob)
    prompt = "\n\n".join(prompt_sections)

    if args.dry_run:
        print("=== SYSTEM PROMPT ===")
        print(SYSTEM_PROMPT)
        print("\n=== USER PROMPT ===")
        print(prompt)
        if genai is None:
            print("\n(google-generativeai is not installed; install requirements before hitting the API.)")
        return

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("Set GEMINI_API_KEY (or GOOGLE_API_KEY) in your environment before running this script.")

    if genai is None:
        sys.exit("Install google-generativeai via 'pip install -r requirements.txt' before running without --dry-run.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name=args.model,
        system_instruction=SYSTEM_PROMPT,
    )
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=args.temperature,
            max_output_tokens=args.max_output_tokens,
        ),
    )
    if not getattr(response, "text", None):
        sys.exit("Gemini returned no text. Check your quota and model name.")
    print(response.text)


if __name__ == "__main__":
    main()
