import wave
from piper import PiperVoice
from normalize import normalize_urdu_text
from download_models import ensure_models
ensure_models()
voice = PiperVoice.load("models/ur_PK-fasih-medium.onnx")

text = "میرا فون نمبر 0300 1234567 ہے۔"
text2 =  "میرا فون نمبر 0300 1234567 ہے اور آج 2026 کا سال ہے"
test = "میرا نمبر 0300-1234567 ہے۔"

normalized_text = normalize_urdu_text(test)

with wave.open("normalized_test.wav", "wb") as wav_file:
    voice.synthesize_wav(normalized_text, wav_file)

print("Done!")