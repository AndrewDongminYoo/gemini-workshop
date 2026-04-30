"""Module 4, Exercise 10: Cross-lingual Text Embeddings.

Demonstrates that text-embedding-004 captures semantic similarity
across Korean and English — same meaning scores high regardless of language.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

TEXTS = [
    ("A1_ko", "영끌해서 집 샀는데 금리가 계속 오르고 있어서 너무 힘들다"),
    ("A2_ko", "주택담보대출 이자 부담이 늘어서 매달 적자야"),
    (
        "A3_en",
        "I bought a house with maximum leverage but rising interest rates are crushing me",
    ),
    ("B1_ko", "오늘 저녁 뭐 먹을지 고민이야, 치킨이 땡기는데"),
    ("B2_en", "I can't decide what to have for dinner tonight"),
]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b, strict=False))
    norm_a = sum(x**2 for x in a) ** 0.5
    norm_b = sum(x**2 for x in b) ** 0.5
    return dot / (norm_a * norm_b)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()

    labels, sentences = zip(*TEXTS, strict=False)
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=list(sentences),
    )
    embeddings = [emb.values for emb in result.embeddings]

    lines = ["=== Cross-lingual Semantic Similarity ===\n"]
    lines.append("Texts:")
    for label, sentence in TEXTS:
        lines.append(f"  [{label}] {sentence}")

    lines.append("\nCosine similarities (higher = more similar meaning):")
    for i in range(len(TEXTS)):
        for j in range(i + 1, len(TEXTS)):
            sim = cosine_similarity(embeddings[i], embeddings[j])
            tag = "← SAME LANGUAGE" if labels[i][-2:] == labels[j][-2:] else ""
            lines.append(f"  [{labels[i]}] vs [{labels[j]}]: {sim:.4f}  {tag}")

    output = "\n".join(lines)
    print(output)

    output_path = os.path.join(OUTPUT_DIR, "ex10_embeddings.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
