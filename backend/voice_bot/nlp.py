def detect_intent(text: str) -> str:
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "greeting"
    elif "time" in text:
        return "time_query"
    elif "help" in text:
        return "help"
    else:
        return "unknown"
