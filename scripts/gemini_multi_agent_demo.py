#!/usr/bin/env python3
"""Simplified multi-agent workflow using Gemini 2.5 Pro without CrewAI."""

import argparse
import json
import os
import pathlib
import time
from dataclasses import dataclass
from typing import Dict, List

import google.generativeai as genai


def load_dotenv() -> None:
    """Load environment variables from the repo-level .env file."""
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


@dataclass
class Agent:
    """A simple agent that uses Gemini for specific tasks."""
    name: str
    role: str
    goal: str
    backstory: str
    model: genai.GenerativeModel


class CustomerSupportWorkflow:
    """Simulates a multi-agent workflow for analyzing customer support data."""

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.agents = self._create_agents()
        self.support_data = self._get_mock_support_data()

    def _create_agents(self) -> Dict[str, Agent]:
        """Create the three agents with different system prompts."""

        # Data Analyst Agent
        analyst_model = genai.GenerativeModel(
            model_name="gemini-2.5-pro",
            system_instruction="""You are a Customer Support Data Analyst.
            Your strength lies in identifying patterns and quantifying problems from raw support data.
            Analyze customer support data to identify trends, recurring issues, and key pain points.
            Be specific with numbers, percentages, and concrete examples."""
        )

        # Process Optimizer Agent
        optimizer_model = genai.GenerativeModel(
            model_name="gemini-2.5-pro",
            system_instruction="""You are a Process Optimization Specialist.
            You specialize in optimizing business processes and can quickly tie root causes to operational fixes.
            Identify bottlenecks and inefficiencies in current support processes and propose actionable improvements.
            Focus on practical, implementable solutions with clear impact assessments."""
        )

        # Report Writer Agent
        writer_model = genai.GenerativeModel(
            model_name="gemini-2.5-pro",
            system_instruction="""You are an Executive Report Writer.
            You craft crisp executive summaries that highlight risks, impact, and decisive actions.
            Compile analysis and recommendations into a concise report for the COO.
            Use clear headings, bullets, and prioritized recommendations."""
        )

        return {
            "analyst": Agent(
                name="Data Analyst",
                role="Customer Support Data Analyst",
                goal="Analyze customer support data to identify trends, recurring issues, and key pain points.",
                backstory="Expert data analyst specializing in customer support operations.",
                model=analyst_model
            ),
            "optimizer": Agent(
                name="Process Optimizer",
                role="Process Optimization Specialist",
                goal="Identify bottlenecks and inefficiencies, propose actionable improvements.",
                backstory="Specialist in optimizing business processes and operational fixes.",
                model=optimizer_model
            ),
            "writer": Agent(
                name="Report Writer",
                role="Executive Report Writer",
                goal="Compile analysis into a concise report for the COO.",
                backstory="Expert at crafting executive summaries for C-level executives.",
                model=writer_model
            )
        }

    def _get_mock_support_data(self) -> str:
        """Return mock customer support data."""
        return """Recent Support Data Summary:
- 50 tickets related to 'login issues'. High resolution time (avg 48h).
- 30 tickets about 'billing discrepancies'. Mostly resolved within 12h.
- 20 tickets on 'feature requests'. Often closed without resolution.
- Frequent feedback mentions 'confusing user interface' for password reset.
- High volume of calls related to 'account verification process'.
- Sentiment analysis shows growing frustration with 'login issues' resolution time.
- Support agent notes indicate difficulty reproducing 'login issues'."""

    def run(self, data_query: str) -> str:
        """Run the multi-agent workflow sequentially."""
        print("--- Starting Customer Support Analysis Workflow ---\n")

        # Step 1: Data Analyst
        print(f"🔍 {self.agents['analyst'].name} is analyzing the data...")
        analyst_prompt = f"""
        Analyze the following customer support data for {data_query}:

        {self.support_data}

        Identify the top 3-5 recurring issues, quantify frequency and impact,
        and summarize sentiment. Provide specific numbers and percentages.
        """

        analyst_response = self.agents['analyst'].model.generate_content(analyst_prompt)
        analyst_output = analyst_response.text
        print(f"✅ Analysis complete\n")

        # Small delay to avoid rate limiting
        time.sleep(1)

        # Step 2: Process Optimizer
        print(f"⚙️ {self.agents['optimizer'].name} is identifying bottlenecks...")
        optimizer_prompt = f"""
        Based on this analysis from our data analyst:

        {analyst_output}

        Identify the primary process bottlenecks driving these issues and recommend
        2-3 actionable improvements ranked by impact. Include rationale and estimated effort.
        """

        optimizer_response = self.agents['optimizer'].model.generate_content(optimizer_prompt)
        optimizer_output = optimizer_response.text
        print(f"✅ Optimization recommendations ready\n")

        # Small delay to avoid rate limiting
        time.sleep(1)

        # Step 3: Report Writer
        print(f"📝 {self.agents['writer'].name} is compiling the executive report...")
        writer_prompt = f"""
        Combine the following analysis and optimization recommendations into an
        executive-ready COO summary:

        ANALYSIS:
        {analyst_output}

        RECOMMENDATIONS:
        {optimizer_output}

        Create a report with three sections: Critical Issues, Bottlenecks, Recommended Fixes.
        Keep it under one page with clear headings and bullets.
        """

        writer_response = self.agents['writer'].model.generate_content(writer_prompt)
        final_report = writer_response.text
        print(f"✅ Report complete\n")

        return final_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a simplified multi-agent customer support analysis."
    )
    parser.add_argument(
        "--data-query",
        default="last quarter support data",
        help="Optional label describing which data slice to analyze.",
    )
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise SystemExit("Set GEMINI_API_KEY (or GOOGLE_API_KEY) in your .env file")

    args = parse_args()

    workflow = CustomerSupportWorkflow(api_key)
    report = workflow.run(args.data_query)

    print("--- Final Report for COO ---")
    print("=" * 60)
    print(report)
    print("=" * 60)


if __name__ == "__main__":
    main()