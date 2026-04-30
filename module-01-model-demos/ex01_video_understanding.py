"""Module 1, Exercise 1: Video Understanding with Gemini."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client


def main() -> None:
    client = get_client()
    # Ref: https://github.com/patrickloeber/workshop-gemini-aistudio-toolkit
    # Workshop prompt: describe what happens in a video
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Describe what you see if I gave you a short video of a busy street.",
    )
    print(response.text)


if __name__ == "__main__":
    main()
