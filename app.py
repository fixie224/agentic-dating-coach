# app.py
import streamlit as st
from agent.coach import dating_coach_response

st.set_page_config(page_title="AI Dating Coach Hafizi", page_icon="💖")

st.title("💖 AI Dating Coach Hafizi 💖")
st.write("Bercakap dengan AI Dating Coach peribadi anda!")

# Session State
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
    st.subheader("Sebelum mula, kenali anda dulu...")

    st.session_state.user_name = st.text_input("Nama anda?", value=st.session_state.user_name)
    st.session_state.main_issue = st.text_input("Masalah hubungan anda?", value=st.session_state.main_issue)

    if st.session_state.user_name and st.session_state.main_issue:
        if st.button("Mula Chat!"):
            st.session_state.onboard_complete = True
    st.stop()

# Display chat history
for role, content in st.session_state.messages:
    st.chat_message(role).markdown(content)

# Chat input
user_input = st.chat_input("Tanya apa-apa masalah hubungan anda...")

if user_input:
    memory_context = f"User bernama {st.session_state.user_name}. Masalah utama: {st.session_state.main_issue}."
    full_input = f"{memory_context}\n\nUser says: {user_input}"

    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(("user", user_input))

    response = dating_coach_response(full_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append(("assistant", response))
