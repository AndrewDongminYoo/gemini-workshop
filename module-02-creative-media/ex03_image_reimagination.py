"""Module 2, Exercise 3: Image Reimagination with Imagen."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    result = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt="A cozy coffee shop in watercolor painting style, warm lighting",
        config={"number_of_images": 1},
    )
    output_path = os.path.join(OUTPUT_DIR, "ex03_image_reimagination.png")
    with open(output_path, "wb") as f:
        f.write(result.generated_images[0].image.image_bytes)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
