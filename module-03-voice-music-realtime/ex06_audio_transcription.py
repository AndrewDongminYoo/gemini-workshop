"""Module 3, Exercise 6: Audio Transcription."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types
from shared.client import get_client

AUDIO_FILE = os.path.join(os.path.dirname(__file__), "../assets/audio_sample.mp3")


def main() -> None:
    client = get_client()
    if not os.path.exists(AUDIO_FILE):
        print(f"Audio file not found: {AUDIO_FILE}")
        print("Add assets/audio_sample.mp3 first.")
        return

    with open(AUDIO_FILE, "rb") as f:
        audio_bytes = f.read()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Transcribe the following audio accurately.",
            types.Part.from_bytes(data=audio_bytes, mime_type="audio/mp3"),
        ],
    )
    print(response.text)


if __name__ == "__main__":
    main()
