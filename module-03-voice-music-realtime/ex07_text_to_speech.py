"""Module 3, Exercise 7: Text-to-Speech with tone comparison.

Generates the same content in two contrasting tones (formal vs casual)
to demonstrate Gemini's speech style control.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
TTS_MODEL = "gemini-2.5-flash-preview-tts"

VARIANTS = [
    {
        "label": "formal",
        "text": (
            "Ladies and gentlemen, the quarterly performance review indicates "
            "a significant improvement in key metrics. Revenue has increased by "
            "eighteen percent compared to the previous quarter, and customer "
            "satisfaction scores have reached an all-time high."
        ),
        "voice": "Aoede",
    },
    {
        "label": "casual",
        "text": (
            "Hey! So I just checked the numbers and — wow — we actually crushed it "
            "this quarter. Revenue is up eighteen percent, which is huge, and "
            "our customer satisfaction scores? Best. Ever. Seriously, the team "
            "absolutely nailed it."
        ),
        "voice": "Puck",
    },
]


def synthesize(client, text: str, voice: str, output_path: str) -> None:
    response = client.models.generate_content(
        model=TTS_MODEL,
        contents=text,
        config=types.GenerateContentConfig(
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
                )
            )
        ),
    )
    audio_data = response.candidates[0].content.parts[0].inline_data.data
    with open(output_path, "wb") as f:
        f.write(audio_data)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()

    for variant in VARIANTS:
        output_path = os.path.join(OUTPUT_DIR, f"ex07_tts_{variant['label']}.wav")
        print(f"Synthesizing [{variant['label']}] with voice '{variant['voice']}'...")
        synthesize(client, variant["text"], variant["voice"], output_path)
        print(f"  Saved: {output_path}")

    print("\nCompare the two files to hear the difference in tone and delivery.")


if __name__ == "__main__":
    main()
