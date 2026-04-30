"""Module 1, Exercise 1: Video Understanding with Gemini.

Passes a YouTube URL directly to the Gemini API — no download required.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types

from shared.client import get_client

YOUTUBE_URL = "https://www.youtube.com/watch?v=ZhpV1UIqpcE"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

PROMPTS = [
    "Summarize what this video is about in 3 bullet points.",
    "What is the main message or key takeaway from this video?",
    "List any specific terms, tools, or technologies mentioned.",
]


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()

    video_part = types.Part.from_uri(file_uri=YOUTUBE_URL, mime_type="video/*")
    lines = [f"Video: {YOUTUBE_URL}\n"]

    for prompt in PROMPTS:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[video_part, prompt],
        )
        lines.append(f"Q: {prompt}")
        lines.append(f"A: {response.text.strip()}\n")

    output = "\n".join(lines)
    print(output)

    output_path = os.path.join(OUTPUT_DIR, "ex01_video_understanding.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
