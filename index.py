import os, streamlit as st


import openai 

openai.api_key = st.secrets['pass']

# Create Text Area Widget to enable user to enter texts
article_text = st.text_area('Enter your scientific texts to summarize')

# Create Radio Buttons
output_size = st.radio( label = 'What kind of output do you want?', 
                        options= ['To-The-Point', 'Concise', 'Detailed']
                     )
