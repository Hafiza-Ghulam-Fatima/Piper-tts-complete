# TTS API — Integration Guide

This service converts text into speech audio. It is meant to sit
between **Group 2 (LLM)** and **Group 4 (Avatar)** in the pipeline:

```
Group 2 (LLM) → [this API] → Group 4 (Avatar)
```

## Running the API

```bash
cd backend
pip install -r requirements.txt
python download_models.py   # only needed once, downloads voice models
uvicorn app:app --reload --port 8000
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### `POST /synthesize`

**For Group 2 (LLM) to call.** Converts text into speech audio.

Request body (JSON):
```json
{
  "text": "یہ ٹیسٹ ہے",
  "voice": "ur_PK-fasih-medium"
}
```

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | The text to speak. Must not be empty. |
| `voice` | string | no | Defaults to `ur_PK-fasih-medium`. See available voices below. |

Response: raw audio bytes, `Content-Type: audio/wav`.

**Available voices:**
- `ur_PK-fasih-medium` (Urdu)
- `en_US-amy-medium`, `en_US-kristin-medium`, `en_US-ryan-medium`,
  `en_US-ryan-high`, `en_GB-alan-medium` (English)

### `GET /health`

Simple check that the service is running. Returns `{"status": "ok"}`.

## Example integration (what Group 2's code might look like)

```python
import requests

response = requests.post(
    "http://<tts-server-address>/synthesize",
    json={"text": llm_generated_text, "voice": "ur_PK-fasih-medium"},
)
audio_bytes = response.content  # hand this off to Group 4 (avatar)
```

## Testing without the real LLM

Until Group 2's service is ready, use `dummy_llm_client.py` at the
repo root to simulate a request:

```bash
python dummy_llm_client.py
```

This sends a hardcoded Urdu sentence to `/synthesize` and saves the
result as `dummy_llm_output.wav`, so you can confirm the pipeline
works before the real LLM is wired in.

## Notes for Group 4 (Avatar)

The API returns a standard `.wav` file (raw audio bytes in the HTTP
response body) — no extra encoding or wrapping. Save the response
content directly to a `.wav` file, or feed the bytes straight into
whatever audio-input step the avatar model expects.
