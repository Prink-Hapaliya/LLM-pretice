# components/image_uploader.py

import streamlit as st
from PIL import Image
import io
from detection.detection import detection

class ImageUploader:
    def __init__(self):
        self.uploaded_image = None
        self.image_bytes = None
        self.detection = detection()

    def render(self):
        with st.container():
            st.markdown('<div class="center">', unsafe_allow_html=True)
            uploaded_file = st.file_uploader(
                "📤 Upload an Image",
                type=["png", "jpg", "jpeg", "gif"],
                accept_multiple_files=False,
                key="image_uploader"
            )
            st.markdown('</div>', unsafe_allow_html=True)

            if uploaded_file is not None:
                try:
                    self.image_bytes = uploaded_file.read()
                    self.image_convert = Image.open(io.BytesIO(self.image_bytes))
                    self.uploaded_image = self.detection.run(self.image_convert)
                    # Image(self.uploaded_image)
                except Exception as e:
                    st.error(f"Error uploading image: {e}")
        return self.uploaded_image
