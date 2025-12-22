def speech_to_text(audio_path):
    return "I need an urgent appointment"
import speech_recognition as sr

def speech_to_text(audio_path: str) -> str:
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Speech service unavailable"
