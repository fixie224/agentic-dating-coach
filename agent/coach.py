# agent/coach.py

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from agent.persona import get_persona_prompt
from agent.mood import detect_mood
from agent.memory import update_user_mood, get_user_history, analyze_user_emotional_trend

openai_api_key = st.secrets["OPENAI_API_KEY"]

def dating_coach_response(user_input: str) -> str:
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        openai_api_key=openai_api_key
    )

    # Mood detection
    mood = detect_mood(user_input)
    update_user_mood(mood)

    # Emotional trend analysis
    trend = analyze_user_emotional_trend()

    system_prompt = get_persona_prompt()

    mood_instruction = ""

    if trend == "sad":
        mood_instruction = (
            "Secara keseluruhan, user sering dalam mood sedih. "
            "Jawab dengan penuh empati, perlahan, dan pastikan beri semangat untuk memperbaiki keyakinan diri user."
        )
    elif trend == "happy":
        mood_instruction = (
            "Secara keseluruhan, user biasanya ceria. "
            "Jawab dengan ringan, penuh semangat, dan encourage positivity."
        )
    elif trend == "angry":
        mood_instruction = (
            "Secara keseluruhan, user kerap marah/tegang. "
            "Jawab dengan penuh ketenangan, stabilkan emosi user tanpa menghakimi."
        )
    else:
        mood_instruction = (
            "User dalam mood neutral. Jawab dengan gaya normal mesra dan profesional."
        )

    messages = [
        system_prompt,
        HumanMessage(content=f"{mood_instruction}\n\nUser says: {user_input}")
    ]

    response = llm.invoke(messages)
    return response.content
