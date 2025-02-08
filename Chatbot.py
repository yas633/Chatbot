# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:34:20 2025

@author: hp
"""
import pandas as pd 
import streamlit as st
import os
from mistralai import Mistral

st.title("ChatBot YAS 🧠")
st.caption("A Streamlit chatbot powered by Mistral 🤓")
txtinput=st.text_input("Comment je peux vous aider aujourd'hui ?")

    
model = "mistral-large-latest"
client = Mistral(api_key="XimjtoeOsG5fpSy8PTahnxkjy9mgKjK6")

chat_response = client.chat.complete(
     model= model,
     messages = [
         {
             "role": "user",
             "content":txtinput,
         },
     ]
 )
st.write(chat_response.choices[0].message.content)

