from __future__ import annotations

import argparse
import os
from typing import Optional

from agents import Agent, Runner, function_tool

DEFAULT_MODEL = "gpt-4.1-mini"
DEFAULT_INSTRUCTIONS = (
    "You are a concise research copilot. Break down user requests into steps, "
    "use the available tools when they help, and keep answers brief and actionable."
)


@function_tool
def search_local_docs(query: str) -> str:
    """Stubbed tool that pretends to search project documentation."""
    return (
        "This is a placeholder result for '{query}'. "
        "Wire this up to your documentation store or search API."
    ).format(query=query)


@function_tool
def get_weather(city: str) -> str:
    """Stubbed tool that returns fake weather data."""
    return (
        f"The current weather in {city} is 72°F, sunny, with a light breeze. "
        "Replace this with a real weather client."
    )


def build_agent(model: str = DEFAULT_MODEL) -> Agent:
    """Create a sample agent configured with instructions and tools."""
    return Agent(
        name="Sample Agent",
        model=model,
        instructions=DEFAULT_INSTRUCTIONS,
        tools=[search_local_docs, get_weather],
    )


def run_prompt(prompt: str, model: str = DEFAULT_MODEL, session_id: Optional[str] = None) -> str:
    """Execute a single prompt against the agent and return the final output."""
    agent = build_agent(model=model)
    result = Runner.run_sync(agent, prompt, session_id=session_id)
    return result.final_output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the sample OpenAI Agents SDK workflow.")
    parser.add_argument("prompt", help="User prompt for the agent to handle.")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Model to use (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--session",
        default=None,
        help="Session identifier for conversational memory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY must be set to run the sample agent.")

    response = run_prompt(args.prompt, model=args.model, session_id=args.session)

    print("\nAgent response:\n")
    print(response)


if __name__ == "__main__":
    main()
