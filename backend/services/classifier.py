# backend/services/classifier.py

INTENT_RULES = {
    "HOT": {
        "keywords": ["emergency", "pain", "urgent", "bleeding", "accident"],
        "score": 90
    },
    "APPOINTMENT": {
        "keywords": ["appointment", "book", "schedule", "consult"],
        "score": 75
    },
    "ENQUIRY": {
        "keywords": ["price", "cost", "details", "charges"],
        "score": 50
    },
    "FOLLOW_UP": {
        "keywords": ["call later", "callback", "tomorrow"],
        "score": 40
    },
    "NOT_INTERESTED": {
        "keywords": ["not interested", "don't call", "stop"],
        "score": 0
    }
}

def classify_intent(text: str):
    text = text.lower()

    best_match = {
        "intent": "UNKNOWN",
        "score": 10,
        "matched_keyword": None
    }

    for intent, rule in INTENT_RULES.items():
        for keyword in rule["keywords"]:
            if keyword in text:
                return {
                    "intent": intent,
                    "score": rule["score"],
                    "matched_keyword": keyword
                }

    return best_match


