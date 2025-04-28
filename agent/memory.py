import streamlit as st
from agent.mood import detect_mood

def update_user_mood(user_input: str):
    mood = detect_mood(user_input)
    if "user_mood_history" not in st.session_state:
        st.session_state.user_mood_history = []
    st.session_state.user_mood_history.append(mood)

def get_user_history():
    if "user_mood_history" in st.session_state:
        return st.session_state.user_mood_history
    return []
