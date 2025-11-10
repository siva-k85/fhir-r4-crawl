# CrewAI Customer Support Analysis Demo

This repository includes a CrewAI example that orchestrates three Gemini 2.5 Pro
agents to analyze customer support data, surface bottlenecks, and draft a COO
report.

## Prerequisites

1. Ensure `.env` contains a valid `GEMINI_API_KEY`. (Already checked into the repo
   for convenience; rotate if needed.)
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Demo

```bash
python scripts/crewai_support_analysis.py --data-query "last quarter support data"
```

- `--data-query` is optional and simply labels the simulated dataset the tool
  fetches.
- The script streams verbose output from each CrewAI agent followed by the final
  COO-ready report.

## Components

- **Tool:** `CustomerSupportDataTool` simulates fetching ticket/feedback stats.
- **Agents:** Data Analyst, Process Optimization Specialist, Executive Report
  Writer – all powered by `gemini/gemini-2.5-pro` via CrewAI’s `LLM` wrapper.
- **Tasks:** Sequential analysis → optimization → COO report.

## Gemini CLI / Code Assist

Use `scripts/gemini_agent.py` for ad-hoc coding help inside this repo:

```bash
python scripts/gemini_agent.py "Summarize src pipeline" --files src/**/*.py
```

This CLI loads `.env`, so the same Gemini key works for both the CrewAI demo and
general coding assistance (also exposed as the VS Code task “Gemini: Ask Coding
Agent”).
