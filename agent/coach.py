# agent/coach.py
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from agent.persona import get_persona_prompt
from agent.mood import detect_mood

openai_api_key = st.secrets["OPENAI_API_KEY"]

def dating_coach_response(user_input: str) -> str:
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        openai_api_key=openai_api_key
    )

    # Mood detection
    mood = detect_mood(user_input)

    system_prompt = get_persona_prompt()

    mood_instruction = ""
    if mood == "sad":
        mood_instruction = (
            "User sedang bersedih. Jawab dengan perlahan, banyakkan perkataan yang comforting, dan berikan sokongan emosi."
        )
    elif mood == "happy":
        mood_instruction = (
            "User sedang gembira. Jawab dengan lebih bertenaga, cepat, dan ringan."
        )
    elif mood == "angry":
        mood_instruction = (
            "User sedang marah atau geram. Jawab dengan tenang, cuba tenangkan perasaan user dan bagi nasihat neutral."
        )

    messages = [
        system_prompt,
        HumanMessage(content=f"{mood_instruction}\n\nUser says: {user_input}")
    ]

    response = llm.invoke(messages)
    return response.content
