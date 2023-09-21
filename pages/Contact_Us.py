import streamlit as st
from Send_email import send_email
import pandas as pd

df = pd.read_csv("topics.csv")
with st.form(key ="email_forms"):
    user_email= st.text_input("Your email adderss",placeholder="Enter your email...")
    option = st.selectbox(''
     'What topic do you want to discuss?',
         df["topic"])
    raw_message= st.text_area("Message",placeholder= "Your message...")
    message=f"""\
Subject: You have received an email from{user_email}

From:{user_email}
{raw_message}"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)