"""Module 1, Exercise 1: Video Understanding with Gemini."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    # Ref: https://github.com/patrickloeber/workshop-gemini-aistudio-toolkit
    # Workshop prompt: describe what happens in a video
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Describe what you see if I gave you a short video of a busy street.",
    )
    output_path = os.path.join(OUTPUT_DIR, "ex01_video_understanding.txt")
    with open(output_path, "w") as f:
        f.write(response.text)
    print(response.text)
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
