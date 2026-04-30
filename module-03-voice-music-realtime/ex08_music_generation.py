"""Module 3, Exercise 8: Music Generation."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client


def main() -> None:
    client = get_client()
    # Lyria RealTime — music generation via Gemini
    print("Music generation note:")
    print("Lyria RealTime is accessed via AI Studio's music generation feature.")
    print("For API-based music, use the Live API with Lyria RealTime model.")
    print("Ref: https://ai.google.dev/gemini-api/docs/music-generation")

    # Fallback: describe a music piece with text
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Describe a 30-second upbeat jazz piece suitable for a cafe background.",
    )
    print("\nMusic description prompt result:")
    print(response.text)


if __name__ == "__main__":
    main()
