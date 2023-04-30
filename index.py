import os, streamlit as st


import openai 

openai.api_key = st.secrets['pass']

# Create Text Area Widget to enable user to enter texts
article_text = st.text_area('Enter your scientific texts to summarize')

# Create Radio Buttons
output_size = st.radio( label = 'What kind of output do you want?', 
                        options= ['To-The-Point', 'Concise', 'Detailed']
                     )

# First, we'll use an if statement to determine the desired output size 
# and set the out_token variable accordingly:

if output_size == 'To-The-Point':
 out_token = 50
elif output_size == 'Concise':
 out_token = 128
else:
 out_token = 516

# Next, we'll add a check to make sure that the input text is long enough 
# to summarize, and display a warning if it is not:

if len(article_text)>100:
 # Generate the summary
 # .......
 
else:
 st.warning('Not enough words to summarize!')
