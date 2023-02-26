import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time
import requests

import requests


st.set_page_config(
	page_title = "The Magician",
	page_icon = "",
	initial_sidebar_state="expanded",
)

API_KEY = st.secrets["API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

with st.form(key="my_form"):
    labels = st.multiselect('Pick Labels',["Positive", "Negative", "Netural","Angry"])
    inputs = st.text_area("Enter Text for Classify", 
		      "Hi, I got selected!")
    
    playload = {
        "inputs": inputs,
        "parameters": {"candidate_labels": labels},
    }
    submitted = st.form_submit_button("Classify!!!")
    if submitted:
          output = query(playload)
          st.write(output)