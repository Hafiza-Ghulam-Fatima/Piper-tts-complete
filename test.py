import wave
from piper import PiperVoice

voice = PiperVoice.load("models/ur_PK-fasih-medium.onnx")

text = "السلام علیکم، یہ میرا ٹیسٹ ہے۔"

with wave.open("test_python.wav", "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

print("Done! test_python.wav ban gayi hai.")