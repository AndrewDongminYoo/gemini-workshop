"""Module 1, Exercise 2: Structured Invoice Extraction.

Uses a public sample invoice image via URL — no local file needed.
Swap INVOICE_URL or set INVOICE_PATH to use a local file.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from google.genai import types

from shared.client import get_client

# Public domain sample invoice (replace with your own if preferred)
INVOICE_URL = "https://raw.githubusercontent.com/mozilla/pdf.js/master/web/compressed.tracemonkey-pldi-09.pdf"
INVOICE_PATH = os.path.join(os.path.dirname(__file__), "../assets/invoice_sample.jpg")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

PROMPT = """Extract the following fields from this invoice as valid JSON only (no markdown, no explanation):
{
  "vendor_name": "",
  "invoice_number": "",
  "invoice_date": "",
  "due_date": "",
  "total_amount": "",
  "currency": "",
  "line_items": [
    {"description": "", "quantity": 0, "unit_price": "", "amount": ""}
  ]
}
If a field is not found, use null."""


def get_invoice_part() -> types.Part:
    if os.path.exists(INVOICE_PATH):
        with open(INVOICE_PATH, "rb") as f:
            data = f.read()
        suffix = INVOICE_PATH.rsplit(".", 1)[-1].lower()
        mime = "image/jpeg" if suffix in ("jpg", "jpeg") else f"image/{suffix}"
        return types.Part.from_bytes(data=data, mime_type=mime)
    return types.Part.from_uri(file_uri=INVOICE_URL, mime_type="application/pdf")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    client = get_client()

    source = INVOICE_PATH if os.path.exists(INVOICE_PATH) else INVOICE_URL
    print(f"Using invoice source: {source}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[get_invoice_part(), PROMPT],
    )

    raw = response.text.strip()
    try:
        parsed = json.loads(raw)
        pretty = json.dumps(parsed, ensure_ascii=False, indent=2)
    except json.JSONDecodeError:
        pretty = raw

    print(pretty)
    output_path = os.path.join(OUTPUT_DIR, "ex02_invoice_extraction.json")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pretty)
    print(f"\nSaved: {output_path}")


if __name__ == "__main__":
    main()
