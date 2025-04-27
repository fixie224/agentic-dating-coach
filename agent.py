import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import streamlit as st

# Load API Key secara Secure dari Streamlit Secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Function utama untuk dapatkan jawapan Dating Coach
def dating_coach_response(user_input):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,  # ➔ Friendly, kreatif sikit
        openai_api_key=openai_api_key
    )

    # Setup Persona AI Coach Hafizi
    system_prompt = SystemMessage(
        content=(
            "Anda adalah Hafizi, seorang AI Dating Coach yang sangat berpengalaman dalam membantu individu "
            "yang pemalu atau pernah gagal dalam hubungan. "
            "Anda bercakap dengan gaya yang tenang, penuh empati, mesra, dan sedikit humor untuk membuatkan user rasa selesa. "
            "Jawapan anda mestilah penuh dengan contoh praktikal, bukan sekadar teori. "
            "Selalu beri semangat kepada user untuk teruskan usaha walaupun mereka gagal sebelum ini. "
            "Jika perlu, gunakan gaya motivasi dan sedikit humor untuk menaikkan semangat user."
        )
    )

    messages = [
        system_prompt,
        HumanMessage(content=user_input)
    ]

    # Dapatkan response dari LLM
    response = llm.invoke(messages)
    return response.content
