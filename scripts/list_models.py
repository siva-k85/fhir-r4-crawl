#!/usr/bin/env python3
"""List available Gemini models."""

import os
import pathlib
import google.generativeai as genai


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


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Set GEMINI_API_KEY in your .env file")
        return

    genai.configure(api_key=api_key)

    print("Available models:")
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")


if __name__ == "__main__":
    main()