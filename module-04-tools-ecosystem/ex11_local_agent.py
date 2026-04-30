"""Module 4, Exercise 11: Local Agent with Function Calling."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types
from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def get_weather(city: str) -> str:
    """Mock weather tool."""
    mock_data = {
        "Seoul": "15°C, partly cloudy",
        "Tokyo": "20°C, sunny",
        "London": "10°C, rainy",
    }
    return mock_data.get(city, f"Weather data not available for {city}")


WEATHER_TOOL = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="get_weather",
            description="Get current weather for a city",
            parameters=types.Schema(
                type="OBJECT",
                properties={"city": types.Schema(type="STRING", description="City name")},
                required=["city"],
            ),
        )
    ]
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="What's the weather like in Seoul and Tokyo today?",
        config=types.GenerateContentConfig(tools=[WEATHER_TOOL]),
    )

    log_lines = []
    for part in response.candidates[0].content.parts:
        if part.function_call:
            fc = part.function_call
            result = get_weather(**dict(fc.args))
            line = f"Tool call: {fc.name}({dict(fc.args)}) → {result}"
            print(line)
            log_lines.append(line)

    final = response.text or "(tool call returned — send result back for final answer)"
    print(f"\nFinal response:\n{final}")
    log_lines.append(f"\nFinal response:\n{final}")

    output_path = os.path.join(OUTPUT_DIR, "ex11_local_agent.txt")
    with open(output_path, "w") as f:
        f.write("\n".join(log_lines))
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
