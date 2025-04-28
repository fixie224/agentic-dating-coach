import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from agent.persona import detect_mood

# Load API Key dari Streamlit Secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

def dating_coach_response(user_input: str) -> str:
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        openai_api_key=openai_api_key
    )

    # Mood Detection
    detected_mood = detect_mood(user_input)

    # Save Current Mood ke Session
    if "previous_mood" not in st.session_state:
        st.session_state.previous_mood = None

    mood_transition = ""
    if st.session_state.previous_mood:
        if st.session_state.previous_mood != detected_mood:
            mood_transition = f"User sebelum ini mood '{st.session_state.previous_mood}' tetapi sekarang '{detected_mood}'."

    st.session_state.previous_mood = detected_mood

    # Tone and Style based on Detected Mood
    if detected_mood == "sad":
        mood_style = (
            "Jawab dengan ayat yang panjang dan penuh empati. "
            "Berikan galakan kuat dan berikan contoh kisah motivasi yang sesuai."
        )
    elif detected_mood == "happy":
        mood_style = (
            "Jawab dengan ayat pendek, mesra, penuh excitement. "
            "Gunakan emoji yang sesuai untuk menggembirakan user. 🎉😊"
        )
    elif detected_mood == "angry":
        mood_style = (
            "Jawab dengan perlahan, profesional, elakkan provokasi. "
            "Berikan perspektif neutral dan banyakkan kesabaran dalam ayat."
        )
    else:
        mood_style = (
            "Jawab secara santai, professional, dengan gaya coaching biasa."
        )

    # Persona Instruction + Adaptive Mood
    system_prompt = SystemMessage(
        content=(
            f"Anda adalah Hafizi, AI Dating Coach berpengalaman.\n"
            f"Personaliti anda: tenang, empati, mesra, sedikit humor.\n"
            f"{mood_style}\n"
            f"{mood_transition}\n"
            "Sentiasa gunakan contoh praktikal, beri sokongan dan motivasi kepada user."
        )
    )

    messages = [
        system_prompt,
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content
