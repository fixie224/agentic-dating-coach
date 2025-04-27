import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from agent.persona import get_persona_prompt

# Load API Key securely
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Function utama untuk dapatkan jawapan Dating Coach
def dating_coach_response(user_input, selected_persona):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,  # ➔ Friendly & kreatif sikit
        openai_api_key=openai_api_key
    )

    # Setup Persona ikut pilihan user
    persona_prompt = get_persona_prompt(selected_persona)

    system_prompt = SystemMessage(
        content=persona_prompt
    )

    messages = [
        system_prompt,
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content
