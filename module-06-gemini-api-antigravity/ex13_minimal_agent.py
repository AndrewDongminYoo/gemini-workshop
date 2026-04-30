"""Module 6, Exercise 13: Minimal Agent pattern.

Demonstrates the simplest possible agent loop:
  think → act → observe → repeat
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

SYSTEM_PROMPT = """You are a helpful research assistant.
When given a question, think step by step and provide a clear, concise answer.
If you need to look something up, say SEARCH: <query> on its own line."""


def minimal_agent(question: str, max_turns: int = 3) -> None:
    client = get_client()
    messages = [{"role": "user", "content": question}]

    for turn in range(max_turns):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question if turn == 0 else messages[-1]["content"],
            config={"system_instruction": SYSTEM_PROMPT},
        )
        answer = response.text
        print(f"\n[Turn {turn + 1}]\n{answer}")

        if "SEARCH:" in answer:
            search_query = answer.split("SEARCH:")[1].split("\n")[0].strip()
            mock_result = f"[Mock: results for '{search_query}']"
            messages.append({"role": "assistant", "content": answer})
            messages.append({"role": "user", "content": f"Search result: {mock_result}\nContinue."})
        else:
            break


def main() -> None:
    minimal_agent("Explain the key differences between Gemini Flash and Gemini Pro models.")


if __name__ == "__main__":
    main()
