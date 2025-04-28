# agent/emotion.py

def detect_emotion_and_tone(text):
    text = text.lower()

    if any(word in text for word in ["sedih", "kecewa", "frust", "patah hati"]):
        return "sedih", "Jawab dengan nada tenang, beri semangat dan gunakan emoji 😢🙏"
    elif any(word in text for word in ["marah", "geram", "bengang"]):
        return "marah", "Jawab dengan nada memahami, acknowledge perasaan user, gunakan emoji 😠🤝"
    elif any(word in text for word in ["gembira", "bahagia", "happy", "seronok"]):
        return "gembira", "Jawab dengan nada ceria, gunakan emoji 😄🎉"
    elif any(word in text for word in ["takut", "risau", "cemas"]):
        return "takut", "Jawab dengan nada menenangkan, beri reassurance, gunakan emoji 😨🤗"
    else:
        return "neutral", "Jawab dengan nada neutral profesional."
