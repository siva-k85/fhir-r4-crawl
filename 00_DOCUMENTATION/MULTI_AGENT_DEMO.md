# Multi-Agent Workflow Demo

## Overview

This repository includes two implementations of multi-agent workflows using Google's Gemini API:

1. **Original CrewAI Implementation** (`scripts/crewai_support_analysis.py`) - Requires Python < 3.14
2. **Simplified Gemini Implementation** (`scripts/gemini_multi_agent_demo.py`) - Works with Python 3.14+

## Setup

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Google Generative AI package
pip install google-generativeai python-dotenv
```

### 2. Configure API Key

Add your Gemini API key to the `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

## Running the Demos

### Gemini CLI Agent

The basic Gemini CLI agent for code assistance:

```bash
# Get help with a specific task
python scripts/gemini_agent.py "What is this project about?" --files README.md

# Fix a bug in a specific file
python scripts/gemini_agent.py "Fix the login issue" --files src/auth.py

# Refactor code
python scripts/gemini_agent.py "Refactor this to use async/await" --files src/main.py
```

### Multi-Agent Customer Support Analysis

The simplified multi-agent workflow that simulates CrewAI functionality:

```bash
# Run the default analysis
python scripts/gemini_multi_agent_demo.py

# Analyze specific data
python scripts/gemini_multi_agent_demo.py --data-query "Q4 2024 support tickets"
```

## How It Works

### Simplified Multi-Agent Architecture

The `gemini_multi_agent_demo.py` implements a three-agent workflow:

1. **Data Analyst Agent**
   - Analyzes raw support data
   - Identifies patterns and quantifies issues
   - Outputs structured analysis with metrics

2. **Process Optimizer Agent**
   - Takes analyst output as input
   - Identifies root cause bottlenecks
   - Proposes actionable improvements

3. **Report Writer Agent**
   - Combines all findings
   - Creates executive-ready report
   - Formats for C-level consumption

Each agent uses the same Gemini 2.5 Pro model but with different system instructions to specialize their behavior.

### Sequential Processing

Unlike CrewAI's complex orchestration, this implementation uses simple sequential processing:

1. Each agent completes its task before passing output to the next
2. Small delays prevent rate limiting
3. Each agent's output becomes input for the next agent
4. Final output is a comprehensive executive report

## Python 3.14 Compatibility

The simplified implementation works with Python 3.14+ because it:
- Uses only `google-generativeai` package (compatible with Python 3.14)
- Avoids complex dependencies like CrewAI, LangChain, etc.
- Implements agent behavior through system prompts rather than frameworks

## Available Models

To see available Gemini models for your API key:

```bash
python scripts/list_models.py
```

Current recommended model: `gemini-2.5-pro`

## Extending the System

To add new agents or modify behavior:

1. Edit the system instructions in `_create_agents()` method
2. Add new agent definitions with specialized prompts
3. Modify the workflow in the `run()` method
4. Adjust the mock data in `_get_mock_support_data()` for testing

## Troubleshooting

### Model Not Found Error
If you get a "model not found" error, run `list_models.py` to see available models and update the DEFAULT_MODEL in the script.

### Rate Limiting
The scripts include small delays between agent calls. If you encounter rate limits, increase the `time.sleep()` values.

### API Key Issues
Ensure your API key is properly set in `.env` and has permissions for the Gemini API.

## Use Cases

This simplified multi-agent system can be adapted for:
- Customer support analysis (current implementation)
- Code review workflows
- Document generation pipelines
- Data analysis and reporting
- Content creation workflows
- Research and summarization tasks

The key is to define clear system instructions for each agent that specialize their behavior for specific tasks in the workflow.