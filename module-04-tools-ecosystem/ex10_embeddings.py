"""Module 4, Exercise 10: Text Embeddings."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

TEXTS = [
    "The quick brown fox jumps over the lazy dog",
    "A fast auburn fox leaps above a sleepy canine",
    "I love machine learning and artificial intelligence",
]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x ** 2 for x in a) ** 0.5
    norm_b = sum(x ** 2 for x in b) ** 0.5
    return dot / (norm_a * norm_b)


def main() -> None:
    client = get_client()
    embeddings = []
    for text in TEXTS:
        result = client.models.embed_content(
            model="text-embedding-004",
            contents=text,
        )
        embeddings.append(result.embeddings[0].values)

    print("Cosine similarities:")
    for i in range(len(TEXTS)):
        for j in range(i + 1, len(TEXTS)):
            sim = cosine_similarity(embeddings[i], embeddings[j])
            print(f"  [{i}] vs [{j}]: {sim:.4f}")
    print("\nTexts:")
    for i, t in enumerate(TEXTS):
        print(f"  [{i}] {t}")


if __name__ == "__main__":
    main()
