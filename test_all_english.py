import wave
from piper import PiperVoice
from download_models import ensure_models
ensure_models()
voices_to_test = {
    "amy": "models/en_US-amy-medium.onnx",
    "kristin": "models/en_US-kristin-medium.onnx",
    "ryan_medium": "models/en_US-ryan-medium.onnx",
    "ryan_high": "models/en_US-ryan-high.onnx",
    "alan": "models/en_GB-alan-medium.onnx",
}

text = "Hello, this is my AI avatar assistant. I hope this voice sounds natural and clear."

for name, path in voices_to_test.items():
    print(f"Generating: {name}...")
    voice = PiperVoice.load(path)
    with wave.open(f"english_test_{name}.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

print("\nDone! Saari voices generate ho gayi hain — folder mein english_test_*.wav files check karo.")