# Gemini & AI Studio Workshop

Personal learning repository following the
[Research to Reality: Mastering the Gemini & AI Studio Toolkit](https://github.com/patrickloeber/workshop-gemini-aistudio-toolkit) workshop.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # .env에 GEMINI_API_KEY 입력
```

## Structure

| 폴더 | 내용 |
|------|------|
| `module-01-model-demos/` | Gemini 모델 비교, 영상 이해, 인보이스 추출 |
| `module-02-creative-media/` | 이미지·영상 생성 |
| `module-03-voice-music-realtime/` | 음성, 음악, 실시간 대화 |
| `module-04-tools-ecosystem/` | 임베딩, 로컬 에이전트 |
| `module-05-vibe-coding/` | AI Studio 노코드 실습 (메모만) |
| `module-06-gemini-api-antigravity/` | Gemini API + Antigravity 에이전트 |

## Running a Script

```bash
source .venv/bin/activate
python module-01-model-demos/ex01_video_understanding.py
```

## Assets

`assets/` 폴더에 실습용 샘플 파일(인보이스 이미지, 오디오)을 저장합니다.
워크샵 레포에서 직접 다운로드하거나 직접 준비하세요.
