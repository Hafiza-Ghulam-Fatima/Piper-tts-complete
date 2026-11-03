"""
download_models.py

Ensures every Piper voice model needed by this project exists locally in
voices/. If a model is missing, it's pulled from the Hugging Face repo
instead of being tracked in git (keeps the repo small, avoids the
100MB GitHub file-size limit).

Run this once after cloning the repo:
    python download_models.py

Or import ensure_models() at the top of any script (check_latency.py,
test.py, etc.) so models are fetched automatically before synthesis.
"""

import os
from huggingface_hub import hf_hub_download

# ---- EDIT THIS to match your actual HF repo ----
HF_REPO_ID = "Zaibun594/piper-tts-fyp-voices"
VOICES_DIR = "voices"

# Every voice needs both the .onnx weights and its .onnx.json config
MODEL_FILES = [
    "cori-high.onnx", "cori-high.onnx.json",
    "en_US-amy-medium.onnx", "en_US-amy-medium.onnx.json",
    "en_US-lessac-high.onnx", "en_US-lessac-high.onnx.json",
    "en_US-lessac-medium.onnx", "en_US-lessac-medium.onnx.json",
    "en_US-libritts_r-medium.onnx", "en_US-libritts_r-medium.onnx.json",
    "en_US-ryan-high.onnx", "en_US-ryan-high.onnx.json",
    "john.onnx", "john.onnx.json",
    "ur_PK-fasih-medium.onnx", "ur_PK-fasih-medium.onnx.json",
]


def ensure_models():
    """Download any missing model files from Hugging Face into voices/."""
    os.makedirs(VOICES_DIR, exist_ok=True)

    for filename in MODEL_FILES:
        local_path = os.path.join(VOICES_DIR, filename)
        if os.path.exists(local_path):
            continue  # already have it, skip

        print(f"Downloading {filename} from Hugging Face...")
        downloaded_path = hf_hub_download(
            repo_id=HF_REPO_ID,
            filename=filename,
            local_dir=VOICES_DIR,
        )
        print(f"  -> saved to {downloaded_path}")

    print("All models present in voices/.")


if __name__ == "__main__":
    ensure_models()
