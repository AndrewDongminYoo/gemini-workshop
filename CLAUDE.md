# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Workshop exercises following the Gemini & AI Studio Toolkit series. Each module is a self-contained learning unit containing numbered Python scripts (`ex01_…`, `ex02_…`, …), a `notes.md`, and an `output/` directory (gitignored).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in GEMINI_API_KEY from aistudio.google.com
```

## Running Scripts

Run any exercise script from the repo root:

```bash
python module-01-model-demos/ex01_video_understanding.py
python module-04-tools-ecosystem/ex11_local_agent.py
```

Output files are written to each module's `output/` subdirectory as `.txt` or `.mp4`.

## Architecture

### Shared Client (`shared/client.py`)

All scripts import `from shared.client import get_client()`. The client:

- Loads `.env` using an absolute path relative to `client.py`, so scripts can be run from any directory.
- Raises `EnvironmentError` if `GEMINI_API_KEY` is not set.
- Returns a configured `google.genai.Client` instance.

New scripts must follow the same import pattern:

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from shared.client import get_client
```

### Default Model

Use `gemini-2.5-flash` for all new scripts. Do not use `gemini-2.0-flash` (deprecated).

### Module Summary

| Module                              | Focus                                                 |
| ----------------------------------- | ----------------------------------------------------- |
| `module-01-model-demos/`            | Video understanding, document/invoice extraction      |
| `module-02-creative-media/`         | Image generation (Imagen 3), video generation (Veo 2) |
| `module-03-voice-music-realtime/`   | Audio transcription, TTS, music generation, Live API  |
| `module-04-tools-ecosystem/`        | Embeddings, function-calling agents                   |
| `module-05-vibe-coding/`            | AI Studio UI notes only — no Python scripts           |
| `module-06-gemini-api-antigravity/` | Multi-turn agents, Wikipedia API tool use             |

### Async / Long-Running Operations

Video generation (Veo 2) uses a polling loop — no `asyncio`. Pattern used in `ex05_video_generation.py`:

```python
operation = client.models.generate_videos(...)
while not operation.done:
    time.sleep(10)
    operation = client.operations.get(operation)
```

### Function Calling (Tool Use)

Tools are defined as `types.Tool(function_declarations=[...])`. Two patterns exist:

- **Mock local tools** — ex11: returns hardcoded data.
- **Real external APIs** — ex12: calls Wikipedia REST API via `requests`.

### Assets

- `assets/audio_sample.mp3` — 60s Korean workplace conversation (right-channel extract).
- `assets/invoice_sample.jpg` — Sample invoice; `ex02` falls back to a public PDF if absent.

## Models Reference

| Model ID                       | Used for                                   |
| ------------------------------ | ------------------------------------------ |
| `gemini-2.5-flash`             | Default: generation, understanding, agents |
| `gemini-2.5-flash-preview-tts` | Text-to-speech                             |
| `gemini-embedding-001`         | Embeddings and semantic similarity         |
| `imagen-3.0-generate-002`      | Image generation                           |
| `veo-2.0-generate-001`         | Video generation                           |

## Free-Tier Limits

The free tier allows 20 requests/day. A `429` error means the quota is exhausted; wait until the next UTC midnight.
