# utils/css.py

def inject_css():
    import streamlit as st
    st.markdown(
        """
        <style>
        /* Center the content */
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        /* Style the send button */
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
            font-size: 16px;
            height: 50px; /* Match the height of text input */
        }

        /* Hover effect for send button */
        .stButton > button:hover {
            background-color: #45a049;
        }

        /* Style the text input */
        .stTextInput>div>div>input {
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 10px;
            transition: border 0.3s ease-in-out;
            height: 50px; /* Ensure height matches the button */
            font-size: 16px;
        }

        /* Focus effect for text input */
        .stTextInput>div>div>input:focus {
            border-color: #4CAF50;
            outline: none;
        }

        /* Style for the uploaded image */
        .uploaded-image {
            max-width: 100%;
            border-radius: 10px;
            transition: transform 0.3s ease-in-out;
        }

        /* Hover effect for uploaded image */
        .uploaded-image:hover {
            transform: scale(1.02);
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .stButton > button {
                width: 100%;
                height: 50px;
            }
            .stTextInput>div>div>input {
                width: 100%;
                height: 50px;
            }
        }

        /* Align text input and send button horizontally */
        .input-container {
            display: flex;
            width: 100%;
            max-width: 600px;
            gap: 10px;
        }

        .input-container > div {
            flex: 1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
