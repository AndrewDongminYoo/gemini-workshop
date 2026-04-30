# Gemini & AI Studio Workshop

Personal learning repository following the
[Research to Reality: Mastering the Gemini & AI Studio Toolkit](https://github.com/patrickloeber/workshop-gemini-aistudio-toolkit) workshop
by Patrick Loeber.

Each module contains a `notes.md` for prompts/observations and runnable Python scripts with
real inputs (YouTube video, local audio, public invoice PDF, Wikipedia API).

---

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # fill in GEMINI_API_KEY
```

Get a free API key at [aistudio.google.com](https://aistudio.google.com).

---

## Project Structure

```plaintext
gemini-workshop/
├── shared/
│   └── client.py                  # Gemini API client (all scripts import this)
├── module-01-model-demos/
│   ├── ex01_video_understanding.py
│   ├── ex02_invoice_extraction.py
│   ├── notes.md
│   └── output/
├── module-02-creative-media/
│   ├── ex03_image_reimagination.py
│   ├── ex04_pixel_art.py
│   ├── ex05_video_generation.py
│   ├── notes.md
│   └── output/
├── module-03-voice-music-realtime/
│   ├── ex06_audio_transcription.py
│   ├── ex07_text_to_speech.py
│   ├── ex08_music_generation.py
│   ├── ex09_live_voice.py
│   ├── notes.md
│   └── output/
├── module-04-tools-ecosystem/
│   ├── ex10_embeddings.py
│   ├── ex11_local_agent.py
│   ├── notes.md
│   └── output/
├── module-05-vibe-coding/
│   └── notes.md                   # AI Studio UI — no Python scripts
├── module-06-gemini-api-antigravity/
│   ├── ex12_agent_tool_use.py
│   ├── ex13_minimal_agent.py
│   ├── notes.md
│   └── output/
├── assets/
│   ├── audio_sample.mp3           # Korean conversation (60 s, right-channel extract)
│   └── invoice_sample.jpg         # (optional) place a local invoice image here
├── .env.example
├── requirements.txt
└── README.md
```

Script output files are written to each module's `output/` directory and are gitignored.

---

## Modules & Exercises

### Module 1 — Model Demos

| Script                        | What it does                                                                                                          |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `ex01_video_understanding.py` | Sends a YouTube URL directly to Gemini and runs three analysis prompts: summary, key takeaway, and tech/tool mentions |
| `ex02_invoice_extraction.py`  | Extracts structured JSON from an invoice image (falls back to a public PDF if no local file is present)               |

**Real input:** YouTube video [`ZhpV1UIqpcE`](https://www.youtube.com/watch?v=ZhpV1UIqpcE) — golf stinger shot compilation with Min Woo Lee tutorial.

### Module 2 — Creative & Media Generation

| Script                        | What it does                                         |
| ----------------------------- | ---------------------------------------------------- |
| `ex03_image_reimagination.py` | Generates a styled image with Imagen 3               |
| `ex04_pixel_art.py`           | Generates pixel art with Imagen 3                    |
| `ex05_video_generation.py`    | Async video generation with Veo 2 (polls until done) |

### Module 3 — Voice, Music & Real-Time

| Script                        | What it does                                                                                                 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `ex06_audio_transcription.py` | Transcribes `assets/audio_sample.mp3` (Korean conversation)                                                  |
| `ex07_text_to_speech.py`      | Generates the same quarterly-results announcement in two tones: formal (Aoede voice) and casual (Puck voice) |
| `ex08_music_generation.py`    | Lyria music generation placeholder; falls back to a text description prompt                                  |
| `ex09_live_voice.py`          | Live API setup guide and connection pattern for real-time voice                                              |

**Real input:** `assets/audio_sample.mp3` — 60-second right-channel extract from a Korean workplace conversation (ffmpeg `pan=mono|c0=c1`).

### Module 4 — Tools & Ecosystem

| Script                | What it does                                                                                                                                                           |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ex10_embeddings.py`  | Cross-lingual semantic similarity: same financial-stress concept in Korean and English scores higher cosine similarity (~0.75) than same-language but unrelated topics |
| `ex11_local_agent.py` | Mock weather tool with Gemini function calling                                                                                                                         |

**Key finding:** `gemini-embedding-001` correctly clusters Korean `"영끌해서 집 샀는데 금리가 오르고 있어서 힘들다"` with its English equivalent (sim ≈ 0.75), above same-language unrelated pairs.

### Module 5 — Vibe Coding (notes only)

AI Studio's no-code App Builder — notes recorded in `module-05-vibe-coding/notes.md`.
No Python scripts (UI-only workflow).

### Module 6 — Gemini API + Antigravity

| Script                   | What it does                                                                                                                |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `ex12_agent_tool_use.py` | Two-turn agent with a real Wikipedia REST API search tool; asks Gemini to compare Gemini vs GPT-4 using live Wikipedia data |
| `ex13_minimal_agent.py`  | Minimal think→act→observe agent loop                                                                                        |

**Real tool:** Wikipedia REST API `https://en.wikipedia.org/api/rest_v1/page/summary/{topic}` — no API key required.

---

## Running Scripts

```bash
source .venv/bin/activate

# Module 1
python module-01-model-demos/ex01_video_understanding.py
python module-01-model-demos/ex02_invoice_extraction.py

# Module 3
python module-03-voice-music-realtime/ex06_audio_transcription.py
python module-03-voice-music-realtime/ex07_text_to_speech.py

# Module 4
python module-04-tools-ecosystem/ex10_embeddings.py
python module-04-tools-ecosystem/ex11_local_agent.py

# Module 6
python module-06-gemini-api-antigravity/ex12_agent_tool_use.py
python module-06-gemini-api-antigravity/ex13_minimal_agent.py
```

All scripts write results to their module's `output/` directory.

---

## Architecture

All scripts share a single API client from `shared/client.py`:

```python
from shared.client import get_client
client = get_client()
```

`get_client()` reads `GEMINI_API_KEY` from the `.env` file at the project root using an
absolute path (`Path(__file__).resolve().parent.parent / ".env"`), so scripts can be run
from any working directory.

---

## Models Used

| Model                          | Used for                                                      |
| ------------------------------ | ------------------------------------------------------------- |
| `gemini-2.5-flash`             | Default generation, video understanding, transcription, agent |
| `gemini-2.5-flash-preview-tts` | Text-to-speech (TTS)                                          |
| `gemini-embedding-001`         | Text embeddings and semantic similarity                       |
| `imagen-3.0-generate-002`      | Image generation                                              |
| `veo-2.0-generate-001`         | Video generation                                              |

> **Note:** `gemini-2.0-flash` was deprecated for new projects. Use `gemini-2.5-flash`.
> `text-embedding-004` was replaced by `gemini-embedding-001`.
> The `gemini-2.5-flash` endpoint may return 503 during peak demand — retry after a few seconds.

---

## Assets

| File                        | Source                                                                  |
| --------------------------- | ----------------------------------------------------------------------- |
| `assets/audio_sample.mp3`   | Right-channel extract from a personal M4A recording (10:00–11:00), 60 s |
| `assets/invoice_sample.jpg` | Optional local invoice; `ex02` falls back to a public PDF if absent     |

To extract your own audio sample from an M4A with stereo channel separation:

```bash
ffmpeg -ss 600 -i "input.m4a" -t 60 \
  -af "pan=mono|c0=c1,afade=t=in:d=0.5,afade=t=out:st=59.5:d=0.5" \
  -codec:a libmp3lame -q:a 2 assets/audio_sample.mp3
```

(`c0=c1` isolates the right channel; swap to `c0=c0` for the left channel.)

---

## Free Tier Limits

The free Gemini API tier allows 20 requests/day for some models. If you hit a
`429 RESOURCE_EXHAUSTED` error, wait until the daily quota resets or use a paid key.
