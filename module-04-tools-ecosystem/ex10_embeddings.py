"""Module 4, Exercise 10: Text Embeddings."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

TEXTS = [
    "The quick brown fox jumps over the lazy dog",
    "A fast auburn fox leaps above a sleepy canine",
    "I love machine learning and artificial intelligence",
]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = sum(x**2 for x in a) ** 0.5
    norm_b = sum(x**2 for x in b) ** 0.5
    return dot / (norm_a * norm_b)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    embeddings = []
    for text in TEXTS:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=text,
        )
        embeddings.append(result.embeddings[0].values)

    lines = ["Cosine similarities:"]
    for i in range(len(TEXTS)):
        for j in range(i + 1, len(TEXTS)):
            sim = cosine_similarity(embeddings[i], embeddings[j])
            lines.append(f"  [{i}] vs [{j}]: {sim:.4f}")
    lines.append("\nTexts:")
    for i, t in enumerate(TEXTS):
        lines.append(f"  [{i}] {t}")

    output = "\n".join(lines)
    print(output)

    output_path = os.path.join(OUTPUT_DIR, "ex10_embeddings.txt")
    with open(output_path, "w") as f:
        f.write(output)
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
