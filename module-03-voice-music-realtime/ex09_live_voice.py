"""Module 3, Exercise 9: Live Voice Conversation.

Prerequisites:
    pip install pyaudio

Note: Live voice requires the Gemini Live API (WebSocket-based).
This script demonstrates the setup pattern.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.client import get_client

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Live Voice setup:")
    print("  client = get_client()")
    print("  async with client.aio.live.connect(model='gemini-3.1-flash-live-preview') as session:")
    print("      # Send audio chunks and receive streamed audio back")
    print()
    print("Run the interactive demo from the Gemini cookbook for full audio I/O.")

    client = get_client()
    setup_note = (
        "Live Voice requires the Gemini Live API (WebSocket).\n"
        "Model: gemini-3.1-flash-live-preview\n"
        "Ref: https://github.com/google-gemini/cookbook/tree/main/examples/live_api\n"
    )
    output_path = os.path.join(OUTPUT_DIR, "ex09_live_voice_setup.txt")
    with open(output_path, "w") as f:
        f.write(setup_note)
    print(f"\nClient ready: {type(client)}")
    print(f"Saved setup note: {output_path}")


if __name__ == "__main__":
    main()
