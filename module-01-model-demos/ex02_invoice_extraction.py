"""Module 1, Exercise 2: Structured Invoice Extraction."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

PROMPT = """Extract the following fields from the invoice image as JSON:
- vendor_name
- invoice_number
- invoice_date
- total_amount
- line_items (list of {description, quantity, unit_price})

Return only valid JSON."""


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()
    # Replace with actual image path: assets/invoice_sample.jpg
    print("Exercise 2: Invoice Extraction (stub)")
    print("Add an invoice image to assets/ and update this script.")
    print("Prompt to use:")
    print(PROMPT)

    output_path = os.path.join(OUTPUT_DIR, "ex02_invoice_prompt.txt")
    with open(output_path, "w") as f:
        f.write(PROMPT)
    print(f"\nSaved prompt: {output_path}")


if __name__ == "__main__":
    main()
