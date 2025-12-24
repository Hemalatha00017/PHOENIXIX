from backend.services.classifier import classify_intent
from backend.voice_bot.stt import speech_to_text

def process_audio(file_path: str):
    stt_result = speech_to_text(file_path)

    # 🔥 FIX: extract text safely
    if isinstance(stt_result, dict):
        text = stt_result.get("text", "")
    else:
        text = stt_result

    analysis = classify_intent(text)

    return {
        "transcription": stt_result,
        "analysis": analysis
    }
