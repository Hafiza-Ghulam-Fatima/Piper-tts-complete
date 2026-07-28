"""
Live Text-to-Speech API using Piper.

Run locally:
    uvicorn app:app --reload --port 8000

Endpoint:
    POST /synthesize
    body: {"text": "...", "voice": "ur_PK-fasih-medium"}
    returns: audio/wav bytes
"""

import io
import wave
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from piper import PiperVoice

app = FastAPI(title="FYP TTS API")

# Allow the LLM/avatar services (or a browser frontend) to call this API
# from any origin during development. Narrow this down to specific
# domains before going to production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MODELS_DIR = Path(__file__).parent.parent / "voices"

# Voices are loaded once at startup and kept in memory, so requests
# don't pay the model-loading cost every time.
_voice_cache: dict[str, PiperVoice] = {}


def get_voice(voice_name: str) -> PiperVoice:
    if voice_name not in _voice_cache:
        model_path = MODELS_DIR / f"{voice_name}.onnx"
        if not model_path.exists():
            raise HTTPException(
                status_code=400,
                detail=f"Unknown voice '{voice_name}'. Model file not found: {model_path.name}",
            )
        _voice_cache[voice_name] = PiperVoice.load(str(model_path))
    return _voice_cache[voice_name]


class SynthesizeRequest(BaseModel):
    text: str
    voice: str = "ur_PK-fasih-medium"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/synthesize")
def synthesize(req: SynthesizeRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="text must not be empty")

    voice = get_voice(req.voice)

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        voice.synthesize_wav(req.text, wav_file)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="audio/wav",
        headers={"Content-Disposition": "inline; filename=speech.wav"},
    )
