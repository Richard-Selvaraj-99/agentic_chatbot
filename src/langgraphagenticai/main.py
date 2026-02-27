import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """loads the necessary functions from objects and functions """
    ui=LoadStreamlitUI()
    user_input= ui.load_streamlit_ui()

    if not user_input:
        st.error("error failed to load user input from UI")
    
    user_message=st.chat_input("human ask monke aswer:")
