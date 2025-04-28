import streamlit as st
from agent.coach import dating_coach_response
from agent.memory import get_user_history

st.set_page_config(page_title=" berborak dengan Hafizi", page_icon="💖")

st.title("💖 Berborak dengan Hafizi 💖")
st.caption("Bercakap dengan AI Dating Coach yang memahami anda!")

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "main_issue" not in st.session_state:
    st.session_state.main_issue = ""
if "onboard_complete" not in st.session_state:
    st.session_state.onboard_complete = False

# Onboarding
if not st.session_state.onboard_complete:
    st.subheader("Kenali Anda Dulu")
    st.session_state.user_name = st.text_input("Nama anda?", value=st.session_state.user_name)
    st.session_state.main_issue = st.text_input("Masalah hubungan anda?", value=st.session_state.main_issue)
    if st.session_state.user_name and st.session_state.main_issue:
        if st.button("Mula Chat"):
            st.session_state.onboard_complete = True
    st.stop()

# Display chat history
for role, content in st.session_state.messages:
    if role == "user":
        st.chat_message("user").markdown(content)
    else:
        st.chat_message("assistant").markdown(content)

# Chat input
user_input = st.chat_input("Tanya apa-apa masalah hubungan anda...")

if user_input:
    memory_context = f"User bernama {st.session_state.user_name}. Masalah utama: {st.session_state.main_issue}."
    full_input = f"{memory_context}\n\n{user_input}"

    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(("user", user_input))

    # Get AI response
    response = dating_coach_response(full_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append(("assistant", response))

# Display Memory Tracker Sidebar
with st.sidebar:
    st.subheader("🧠 Mood Tracker")
    st.markdown("**Sejarah Mood User:**")
    history = get_user_history()
    st.text(history)
