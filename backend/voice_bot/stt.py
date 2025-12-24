import whisper
import librosa
import numpy as np
import soundfile as sf
import noisereduce as nr
import uuid
import os

# Load Whisper model
model = whisper.load_model("base")

AUDIO_DIR = "backend/voice_bot/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# ---------------------------
# Audio Preprocessing
# ---------------------------

def preprocess_audio(input_path):
    y, sr = librosa.load(input_path, sr=16000)

    # Reject very short audio
    if len(y) < sr:
        raise ValueError("Audio too short")

    # Normalize volume
    y = librosa.util.normalize(y)

    # Noise reduction
    y = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.9)

    # Trim silence
    y, _ = librosa.effects.trim(y, top_db=25)

    clean_path = f"{AUDIO_DIR}/clean_{uuid.uuid4()}.wav"
    sf.write(clean_path, y, sr)

    return clean_path

# ---------------------------
# Speech to Text
# ---------------------------

def speech_to_text(audio_path):
    try:
        clean_audio = preprocess_audio(audio_path)

        result = model.transcribe(
            clean_audio,
            language="en",
            temperature=0,
            beam_size=5,
            best_of=5,
            fp16=False,
            condition_on_previous_text=False
        )

        text = result.get("text", "").strip()
        segments = result.get("segments", [])

        if not text:
            raise ValueError("No speech detected")

        # Confidence score
        confidence = np.mean([seg["avg_logprob"] for seg in segments])

        if confidence < -1.0:
            raise ValueError("Low transcription confidence")

        return {
            "text": text,
            "confidence": round(confidence, 2)
        }

    except Exception as e:
        return {
            "error": str(e)
        }
