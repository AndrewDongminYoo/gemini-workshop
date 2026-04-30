"""Module 2, Exercise 4: Pixel Art Generation."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client


def main() -> None:
    client = get_client()
    result = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt="A cute cat in 16-bit pixel art style, retro video game aesthetic",
        config={"number_of_images": 1},
    )
    image = result.generated_images[0].image
    with open("output_pixel_art.png", "wb") as f:
        f.write(image.image_bytes)
    print("Saved: output_pixel_art.png")


if __name__ == "__main__":
    main()
