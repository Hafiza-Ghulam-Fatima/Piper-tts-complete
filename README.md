# FYP TTS — Piper Setup

Piper TTS setup for the AI avatar assistant project. Uses Piper's Urdu
`fasih` voice plus several English voices.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the model files (hosted separately on Hugging Face,
   since they're too large for GitHub):
   ```bash
   python download_models.py
   ```

## Models

Hosted at: https://huggingface.co/hafizaghulamfatima55/piper-tts-models

- `ur_PK-fasih-medium` — Urdu
- `en_GB-alan-medium`, `en_US-amy-medium`, `en_US-kristin-medium`,
  `en_US-ryan-medium`, `en_US-ryan-high` — English

## Scripts

- `check_latency.py` — measures TTS generation latency
- `edge_case_test.py` — tests edge cases in text input
- `normalize.py` — text normalization before synthesis
- `test.py`, `test_all_english.py`, `test_phn.py` — voice/phoneme tests
