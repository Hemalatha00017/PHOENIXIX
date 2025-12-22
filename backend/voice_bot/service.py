import uuid
from backend.voice_bot.stt import speech_to_text

async def process_audio(audio):
    file_id = f"{uuid.uuid4()}.wav"
    file_path = f"backend/voice_bot/audio/{file_id}"

    with open(file_path, "wb") as f:
        f.write(await audio.read())

    text = speech_to_text(file_path)

    conversation = {
        "audio_file": file_path,
        "transcription": text,
        "hot_lead": classify_text(text)
    }

    return conversation


def classify_text(text: str) -> bool:
    keywords = ["urgent", "appointment", "pain", "emergency", "payment"]
    return any(word in text.lower() for word in keywords)
