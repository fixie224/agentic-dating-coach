# agent/mood.py

def detect_mood(user_input: str) -> str:
    """Simple mood detection based on keywords."""
    user_input_lower = user_input.lower()
    if any(word in user_input_lower for word in ["sedih", "kecewa", "frust", "patah hati", "down"]):
        return "sad"
    elif any(word in user_input_lower for word in ["gembira", "happy", "seronok", "excited"]):
        return "happy"
    elif any(word in user_input_lower for word in ["marah", "geram", "bengang"]):
        return "angry"
    else:
        return "neutral"
