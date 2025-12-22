from backend.voice_bot.stt import speech_to_text
from backend.voice_bot.utils import save_temp_audio

async def process_audio(file):
    file_path = save_temp_audio(file)
    text = speech_to_text(file_path)
    return text
