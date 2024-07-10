#import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as palm
from langdetect import detect
from googletrans import Translator

load_dotenv()

Api_key = os.getenv("API_KEY")

palm.configure(api_key=Api_key)
translator = Translator()

i=0
model_list = palm.list_models()
for model in model_list:
    if i == 1:
        model_name = model.name
        break
    i += 1

print(model_name)