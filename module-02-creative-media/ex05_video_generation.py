"""Module 2, Exercise 5: Video Generation with Veo."""
import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client


def main() -> None:
    client = get_client()
    # Veo video generation is async — poll until done
    operation = client.models.generate_videos(
        model="veo-2.0-generate-001",
        prompt="A time-lapse of clouds moving over a mountain range at sunset",
        config={"number_of_videos": 1, "duration_seconds": 5},
    )
    print("Generating video... (this may take 1-2 minutes)")
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)

    video = operation.response.generated_videos[0].video
    with open("output_video.mp4", "wb") as f:
        f.write(video.video_bytes)
    print("Saved: output_video.mp4")


if __name__ == "__main__":
    main()
