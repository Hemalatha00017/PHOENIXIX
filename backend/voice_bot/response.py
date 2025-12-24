from datetime import datetime

def generate_response(intent: str) -> str:
    if intent == "greeting":
        return "Hello! How can I assist you today?"
    elif intent == "time_query":
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
    elif intent == "help":
        return "You can ask me about time or say hello!"
    else:
        return "Sorry, I didn't understand that."
