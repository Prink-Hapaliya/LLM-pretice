# components/input_section.py

import streamlit as st

class InputSection:
    def __init__(self):
        self.text = ""
        self.button_clicked = False

    def render(self):
        st.markdown('<div class="center">', unsafe_allow_html=True)
        # Create a container for input and button
        st.markdown('<div class="input-container">', unsafe_allow_html=True)

        # Use Streamlit's columns to align text input and send button horizontally
        col1, col2 = st.columns([4, 1], gap="small")
        with col1:
            self.text = st.text_input("Enter your message here", key="text_input")
        with col2:
            self.button_clicked = st.button("Send", key="send_button")

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        if self.button_clicked:
            if self.text.strip():
                st.success(f"Message sent: {self.text}")
            else:
                st.warning("Please enter a message before sending.")
