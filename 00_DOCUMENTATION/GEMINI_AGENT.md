# Google Gemini Coding Agent

This project now ships with a lightweight Gemini-powered coding helper that can be
invoked from the CLI or directly inside VS Code.

## 1. Prerequisites

1. **API key** – this repository already ships with a persisted key in `.env`:

   ```
   GEMINI_API_KEY=AIzaSyAilOZOsmfZ1Ok4FMFilL6ElU6G-e4gnH4
   ```

   Update that file if you ever need to rotate credentials. Environment variables
   in your shell will still override the file if you prefer not to store secrets
   in git.

2. Install the extra dependency (included in `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

## 2. CLI Usage

```bash
python scripts/gemini_agent.py "Explain how markdown extraction works" \
  --files src/**/*.py 02_CONFIGURATION/CONFIG/*.yml
```

- `task` (positional) – your request to the agent.
- `--files` – optional glob(s) pulled into the prompt for high-signal context.
- `--model` – override the default `gemini-1.5-pro-latest` if needed.
- `--dry-run` – inspect the constructed prompt without spending tokens.

The agent automatically truncates context (8k characters per file, ~60k overall)
to stay within the Gemini Pro window.

> The CLI loads `.env` automatically, so the stored key works for both shell
> sessions and the VS Code task without extra export commands.

## 3. VS Code Task

The repo contains `.vscode/tasks.json` with a **“Gemini: Ask Coding Agent”** task.

1. Open the Command Palette → `Tasks: Run Task` → pick the Gemini task.
2. Enter the prompt.
3. Optionally supply glob patterns for context files (space-separated). Leave it
   blank to run without additional context.
4. Responses stream into VS Code’s terminal panel.

## 4. Tips

- Start with a small set of files so Gemini focuses on the right part of the
  repo; you can rerun with more files as needed.
- Pair the `--dry-run` flag with `--files` while iterating on prompt design,
  then drop `--dry-run` once satisfied.
- Keep sensitive data out of prompts unless your API key is scoped to a secure
  Vertex AI project with the appropriate controls.

That’s it—Gemini is now wired into this workspace for quick, context-aware help.
