# agent/progress.py
import streamlit as st

def generate_weekly_summary(user_name: str) -> str:
    """Generate a simple weekly summary based on chat history"""

    mood_counts = {
        "happy": 0,
        "sad": 0,
        "angry": 0,
        "neutral": 0,
    }

    # Kira mood dari semua mesej user
    for role, content in st.session_state.messages:
        if role == "user":
            from agent.mood import detect_mood
            mood = detect_mood(content)
            if mood in mood_counts:
                mood_counts[mood] += 1

    # Ringkasan mood
    summary = (
        f"**Ringkasan Mingguan untuk {user_name}**\n\n"
        f"- 😄 Gembira: {mood_counts['happy']} kali\n"
        f"- 😢 Sedih: {mood_counts['sad']} kali\n"
        f"- 😡 Marah: {mood_counts['angry']} kali\n"
        f"- 😐 Neutral: {mood_counts['neutral']} kali\n\n"
        "Secara keseluruhan, anda telah menunjukkan ketahanan dan semangat dalam perjalanan emosi anda. "
        "Teruskan usaha memperbaiki diri, dan jangan ragu untuk berbincang lagi minggu depan!"
    )

    return summary
