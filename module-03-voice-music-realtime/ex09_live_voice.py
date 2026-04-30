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


def main() -> None:
    # Live voice conversation uses the client.aio.live.connect() API
    # Full interactive demo: https://github.com/google-gemini/cookbook/tree/main/examples/live_api
    print("Live Voice setup:")
    print("  client = get_client()")
    print("  async with client.aio.live.connect(model='gemini-2.0-flash-live-001') as session:")
    print("      # Send audio chunks and receive streamed audio back")
    print()
    print("Run the interactive demo from the Gemini cookbook for full audio I/O.")

    client = get_client()
    print(f"\nClient ready: {type(client)}")


if __name__ == "__main__":
    main()
