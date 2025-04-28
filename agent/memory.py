# agent/memory.py

import pickle
import os

MEMORY_FILE = "user_memory.pkl"

def save_memory(data):
    with open(MEMORY_FILE, "wb") as f:
        pickle.dump(data, f)

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "rb") as f:
            return pickle.load(f)
    else:
        return {
            "user_name": "",
            "main_issue": "",
            "messages": [],
            "onboard_complete": False
        }
