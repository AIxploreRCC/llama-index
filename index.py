import os, streamlit as st


import openai 

openai.api_key = st.secrets["pass"]

# Create Text Area Widget to enable user to enter texts
article_text = st.text_area('Enter your scientific texts to summarize')

