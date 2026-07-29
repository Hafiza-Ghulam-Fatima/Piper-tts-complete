"""
Simulates what the LLM group (Group 2) will eventually send to our
TTS API. Use this to test the backend end-to-end before the real
LLM integration exists.

Run the API first (in another terminal):
    cd backend
    uvicorn app:app --reload --port 8000

Then run this script:
    python dummy_llm_client.py
"""

import requests

#API_URL = "http://127.0.0.1:8000/synthesize"
API_URL = "https://fyp-tts-api-production.up.railway.app/synthesize"

# Pretend this text came from the LLM group's response.
DUMMY_LLM_OUTPUT = "السلام علیکم، آپ کیسے ہیں؟ یہ ایک ٹیسٹ پیغام ہے۔"


def main() -> None:
    payload = {
        "text": DUMMY_LLM_OUTPUT,
        "voice": "ur_PK-fasih-medium",
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code != 200:
        print(f"[error] {response.status_code}: {response.text}")
        return

    with open("dummy_llm_output.wav", "wb") as f:
        f.write(response.content)

    print("Done! Saved as dummy_llm_output.wav")


if __name__ == "__main__":
    main()
