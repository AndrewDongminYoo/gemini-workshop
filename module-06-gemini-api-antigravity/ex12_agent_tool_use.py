"""Module 6, Exercise 12: Agent with Real Web Search via Wikipedia API.

Uses Wikipedia's public REST API as a real (non-mock) search tool,
demonstrating a complete tool-use cycle with actual external data.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import requests
from google.genai import types

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def search_wikipedia(query: str) -> str:
    """Search Wikipedia and return the article summary."""
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")
    try:
        r = requests.get(url, timeout=5, headers={"User-Agent": "gemini-workshop/1.0"})
        if r.status_code == 200:
            data = r.json()
            return data.get("extract", "No summary available.")[:500]
        return f"Wikipedia returned status {r.status_code} for '{query}'"
    except requests.RequestException as e:
        return f"Search failed: {e}"


SEARCH_TOOL = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="search_wikipedia",
            description="Search Wikipedia for factual information about a topic",
            parameters=types.Schema(
                type="OBJECT",
                properties={
                    "query": types.Schema(
                        type="STRING",
                        description="The topic to search for on Wikipedia",
                    )
                },
                required=["query"],
            ),
        )
    ]
)


def run_agent(question: str) -> str:
    client = get_client()
    history = [types.Content(role="user", parts=[types.Part.from_text(text=question)])]
    log_lines = [f"Question: {question}\n"]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history,
        config=types.GenerateContentConfig(tools=[SEARCH_TOOL]),
    )

    tool_results = []
    for part in response.candidates[0].content.parts:
        if part.function_call:
            fc = part.function_call
            result = search_wikipedia(**dict(fc.args))
            entry = f"[Tool] {fc.name}(query='{dict(fc.args).get('query', '')}') →\n{result}"
            print(entry)
            log_lines.append(entry)
            tool_results.append(
                types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=fc.name,
                            response={"result": result},
                        )
                    ],
                )
            )

    if tool_results:
        history.append(response.candidates[0].content)
        history.extend(tool_results)
        final_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history,
            config=types.GenerateContentConfig(tools=[SEARCH_TOOL]),
        )
        final = final_response.text or ""
    else:
        final = response.text or ""

    log_lines.append(f"\n[Final Answer]\n{final.strip()}")
    return "\n".join(log_lines)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    result = run_agent(
        "What are the key differences between Gemini and GPT-4? "
        "Search Wikipedia for background on both models."
    )
    print(f"\n{result}")

    output_path = os.path.join(OUTPUT_DIR, "ex12_agent_tool_use.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
