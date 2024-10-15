# main.py

import streamlit as st
from components.image_uploader import ImageUploader
from components.image_display import ImageDisplay
from components.input_section import InputSection
from utils.css import inject_css

class StreamlitApp:
    def __init__(self):
        self.uploader = ImageUploader()
        self.display = None
        self.input_section = InputSection()
        image_previous=0

    def run(self):
        st.set_page_config(
            page_title="Animated Image Uploader",
            page_icon="📷",
            layout="centered",
            initial_sidebar_state="auto",
        )
        inject_css()
        st.title("📸 Animated Image Uploader")

        # Render the uploader
        image = self.uploader.render()

        # If image is uploaded, render the display and input section
        if image and image != image_previous:
            self.display = ImageDisplay(image)
            self.display.render()
            self.input_section.render()
            
        image_previous = image

if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
