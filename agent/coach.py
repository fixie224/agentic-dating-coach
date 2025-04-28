# agent/coach.py
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from agent.persona import get_persona_prompt
from agent.mood import detect_mood
from agent.memory import update_user_mood, get_user_history

openai_api_key = st.secrets["OPENAI_API_KEY"]

def dating_coach_response(user_input: str) -> str:
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        openai_api_key=openai_api_key
    )

    mood = detect_mood(user_input)
    system_prompt = get_persona_prompt()

    mood_instruction = ""
    if mood == "sad":
        mood_instruction = "User sedang bersedih. Jawab dengan comforting words dan semangat."
    elif mood == "happy":
        mood_instruction = "User gembira. Balas dengan penuh energy dan positivity."
    elif mood == "angry":
        mood_instruction = "User marah. Tenangkan dia dengan nada neutral dan supportive."

    messages = [
        system_prompt,
        HumanMessage(content=f"{mood_instruction}\n\nUser says: {user_input}")
    ]

    # Simpan mood ke dalam memory tracker
    update_user_mood(mood)

    response = llm.invoke(messages)
    return response.content
