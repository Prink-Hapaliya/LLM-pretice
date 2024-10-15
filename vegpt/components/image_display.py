# components/image_display.py

import streamlit as st
import base64
import io

class ImageDisplay:
    def __init__(self, image):
        self.image = image

    def render(self):
        if self.image:
            st.markdown('<div class="center">', unsafe_allow_html=True)
            # Convert image to base64 for embedding
            img_base64 = self.image_to_base64(self.image)
            image_html = f"""
            <img src="data:image/png;base64,{img_base64}" class="uploaded-image" />
            """
            st.markdown(image_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    def image_to_base64(self, img):
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        img_base64 = base64.b64encode(img_bytes).decode()
        return img_base64
