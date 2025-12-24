def classify_lead(transcript: str):
    transcript = transcript.lower()

    hot_keywords = [
        "appointment", "book", "visit", "consultation",
        "price", "cost", "today", "tomorrow"
    ]

    warm_keywords = [
        "later", "call back", "thinking", "details", "information"
    ]

    cold_keywords = [
        "not interested", "busy", "wrong number", "no need"
    ]

    for word in hot_keywords:
        if word in transcript:
            return "HOT"

    for word in warm_keywords:
        if word in transcript:
            return "WARM"

    for word in cold_keywords:
        if word in transcript:
            return "COLD"

    return "UNKNOWN"

