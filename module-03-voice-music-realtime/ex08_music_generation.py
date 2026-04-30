"""Module 3, Exercise 8: Music Generation."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    print("Music generation note:")
    print("Lyria RealTime is accessed via AI Studio's music generation feature.")
    print("For API-based music, use the Live API with Lyria RealTime model.")
    print("Ref: https://ai.google.dev/gemini-api/docs/music-generation")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Describe a 30-second upbeat jazz piece suitable for a cafe background.",
    )
    output_path = os.path.join(OUTPUT_DIR, "ex08_music_description.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"\nMusic description:\n{response.text}")
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
