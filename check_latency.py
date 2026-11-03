import time
import wave
from piper import PiperVoice

from download_models import ensure_models
ensure_models()

print("Loading model...")
voice = PiperVoice.load("models/ur_PK-fasih-medium.onnx")
print("Model loaded.\n")

test_sentences = [
    "السلام علیکم۔",
    "آج موسم بہت اچھا ہے، میں باہر جانا چاہتی ہوں۔",
    "یہ ایک لمبا جملہ ہے جس سے ہم دیکھ سکیں کہ ماڈل کتنا وقت لیتا ہے اور کوالٹی کیسی رہتی ہے۔"
]

# Warm-up run (discard result, taake pehli call ka overhead na count ho)
print("Warm-up run...")
with wave.open("warmup.wav", "wb") as wav_file:
    voice.synthesize_wav("وارم اپ ٹیسٹ۔", wav_file)
print("Warm-up done.\n")

# Actual latency tests
for i, text in enumerate(test_sentences):
    filename = f"latency_test_{i+1}.wav"

    start = time.time()
    with wave.open(filename, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
    duration = time.time() - start

    # Audio length nikalne ke liye file dobara kholo
    with wave.open(filename, "rb") as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        audio_length = frames / float(rate)

    rtf = duration / audio_length if audio_length > 0 else 0
    print(f"Sentence {i+1}: Generation time = {duration:.3f}s | Audio length = {audio_length:.2f}s | Real-time factor = {rtf:.3f}x")