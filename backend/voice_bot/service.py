from backend.voice_bot.stt import speech_to_text
from backend.services.classifier import classify_lead

def process_audio(audio_path: str):
    transcript = speech_to_text(audio_path)

    lead_status = classify_lead(transcript)

    return {
        "transcript": transcript,
        "lead_status": lead_status
    }

