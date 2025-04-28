# agent/memory.py
import streamlit as st

def update_user_mood(mood: str):
    """Update user mood history in Streamlit session."""
    if "mood_history" not in st.session_state:
        st.session_state.mood_history = []
    st.session_state.mood_history.append(mood)

def get_user_history():
    """Get user mood history."""
    return st.session_state.get("mood_history", [])
