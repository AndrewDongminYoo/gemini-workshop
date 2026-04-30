"""Module 2, Exercise 4: Pixel Art Generation."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    result = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt="A cute cat in 16-bit pixel art style, retro video game aesthetic",
        config={"number_of_images": 1},
    )
    output_path = os.path.join(OUTPUT_DIR, "ex04_pixel_art.png")
    with open(output_path, "wb") as f:
        f.write(result.generated_images[0].image.image_bytes)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
