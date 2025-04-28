import streamlit as st
from agent.coach import dating_coach_response
from agent.memory import get_user_history

# Setup Streamlit Page
st.set_page_config(page_title="💖 AI Dating Coach Hafizi 💖", page_icon="💖")

st.title("💖 AI Dating Coach Hafizi 💖")
st.write("Bercakap dengan AI Dating Coach peribadi anda!")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "main_issue" not in st.session_state:
    st.session_state.main_issue = ""
if "onboard_complete" not in st.session_state:
    st.session_state.onboard_complete = False

# Onboarding Step
if not st.session_state.onboard_complete:
    st.subheader("Sebelum mula, mari kenali anda...")

    st.session_state.user_name = st.text_input("Nama anda?", value=st.session_state.user_name)
    st.session_state.main_issue = st.text_input("Apa masalah hubungan anda?", value=st.session_state.main_issue)

    if st.session_state.user_name and st.session_state.main_issue:
        if st.button("Mula Chat! 🚀"):
            st.session_state.onboard_complete = True
    st.stop()

# Display Chat History
for message in st.session_state.messages:
    role, content = message
    if role == "user":
        st.chat_message("user").markdown(content)
    else:
        st.chat_message("assistant").markdown(content)

# Chat Input
user_input = st.chat_input("Tanya apa-apa masalah hubungan anda...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(("user", user_input))

    # Add Memory Context
    memory_context = f"User bernama {st.session_state.user_name}. Masalah utama: {st.session_state.main_issue}."

    # Get AI Response
    response = dating_coach_response(f"{memory_context}\n\n{user_input}")

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append(("assistant", response))

# Sidebar Memory Tracker
with st.sidebar:
    st.header("🧠 Mood Tracker")
    mood_history = get_user_history()
    if mood_history:
        st.write("Sejarah Mood User:")
        for idx, mood in enumerate(mood_history, 1):
            st.write(f"{idx}. {mood}")
    else:
        st.write("Belum ada mood direkodkan lagi.")
