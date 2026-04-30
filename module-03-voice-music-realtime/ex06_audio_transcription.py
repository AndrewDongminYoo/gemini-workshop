"""Module 3, Exercise 6: Audio Transcription."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types
from shared.client import get_client

AUDIO_FILE = os.path.join(os.path.dirname(__file__), "../assets/audio_sample.mp3")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
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
    output_path = os.path.join(OUTPUT_DIR, "ex06_transcription.txt")
    with open(output_path, "w") as f:
        f.write(response.text)
    print(response.text)
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
