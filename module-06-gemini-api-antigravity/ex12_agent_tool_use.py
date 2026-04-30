"""Module 6, Exercise 12: Multi-turn Agent with Tool Use."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types
from shared.client import get_client


def search_web(query: str) -> str:
    """Mock web search tool."""
    return f"[Mock search result for '{query}'] Found 3 relevant articles."


SEARCH_TOOL = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="search_web",
            description="Search the web for current information",
            parameters=types.Schema(
                type="OBJECT",
                properties={"query": types.Schema(type="STRING", description="Search query")},
                required=["query"],
            ),
        )
    ]
)


def run_agent(user_message: str) -> str:
    client = get_client()
    history = [types.Content(role="user", parts=[types.Part.from_text(user_message)])]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=history,
        config=types.GenerateContentConfig(tools=[SEARCH_TOOL]),
    )

    for part in response.candidates[0].content.parts:
        if part.function_call:
            fc = part.function_call
            tool_result = search_web(**dict(fc.args))
            return f"Tool used: {fc.name}({dict(fc.args)})\nResult: {tool_result}"

    return response.text


def main() -> None:
    result = run_agent("What are the latest updates to Gemini models?")
    print(result)


if __name__ == "__main__":
    main()
