"""Module 3, Exercise 7: Text-to-Speech with tone control."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types
from shared.client import get_client

TEXT = "Welcome to the Gemini workshop! Today we explore the future of AI."
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=TEXT,
        config=types.GenerateContentConfig(
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Aoede")
                )
            )
        ),
    )
    audio_data = response.candidates[0].content.parts[0].inline_data.data
    output_path = os.path.join(OUTPUT_DIR, "ex07_tts.wav")
    with open(output_path, "wb") as f:
        f.write(audio_data)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
