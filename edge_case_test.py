import wave
from piper import PiperVoice
from download_models import ensure_models
ensure_models()

voice = PiperVoice.load("models/ur_PK-fasih-medium.onnx")

test_cases = {
    "numbers": "میرا فون نمبر 0300 1234567 ہے اور آج 2026 کا سال ہے۔",
    "punctuation": "کیا آپ ٹھیک ہیں؟ واہ! یہ بہت اچھا ہے، شکریہ۔",
    "mixed_code_switch": "Hello, السلام علیکم۔ میں آپ کا AI اسسٹنٹ ہوں۔",
    "long_sentence": "یہ ایک لمبا جملہ ہے جس میں ہم یہ دیکھنا چاہتے ہیں کہ ماڈل لمبے متن پر کیسا پرفارم کرتا ہے اور کیا آواز کہیں ٹوٹتی ہے یا رفتار میں کوئی فرق آتا ہے یا نہیں۔",
    "rare_words": "استعارہ، تجزیہ، اور مصنوعی ذہانت جیسے الفاظ کیسے بولے جاتے ہیں؟",
    "short_greeting": "السلام علیکم۔",
}

for name, text in test_cases.items():
    filename = f"edge_{name}.wav"
    print(f"Generating: {name}...")
    with wave.open(filename, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

print("\nDone! Saari edge case files ban gayi hain — sun kar note karo kya masla aata hai.")