"""Module 2, Exercise 3: Image Reimagination with Imagen."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client


def main() -> None:
    client = get_client()
    # Uses Imagen 3 for image generation
    # Ref: workshop prompt for reimagining a photo in a new style
    result = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt="A cozy coffee shop in watercolor painting style, warm lighting",
        config={"number_of_images": 1},
    )
    image = result.generated_images[0].image
    with open("output_reimagination.png", "wb") as f:
        f.write(image.image_bytes)
    print("Saved: output_reimagination.png")


if __name__ == "__main__":
    main()
