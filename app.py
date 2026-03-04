import streamlit as st
import google.generativeai as genai
import os

# 1. Konfigurasi API Key (Ambil dari Environment Variable agar aman)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

st.title("Aplikasi AI Saya 🚀")

# 2. Tempat user mengetik
user_input = st.text_input("Tanya sesuatu:")

if user_input:
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 3. Masukkan PROMPT kamu di sini
    full_prompt = f"Instruksi: [MASUKKAN PROMPT DARI AI STUDIO DI SINI]. Pertanyaan user: {user_input}"
    
    response = model.generate_content(full_prompt)
    st.write(response.text)