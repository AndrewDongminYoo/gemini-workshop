"""Module 2, Exercise 5: Video Generation with Veo."""
import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    operation = client.models.generate_videos(
        model="veo-2.0-generate-001",
        prompt="A time-lapse of clouds moving over a mountain range at sunset",
        config={"number_of_videos": 1, "duration_seconds": 5},
    )
    print("Generating video... (this may take 1-2 minutes)")
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)

    output_path = os.path.join(OUTPUT_DIR, "ex05_video.mp4")
    with open(output_path, "wb") as f:
        f.write(operation.response.generated_videos[0].video.video_bytes)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
