"""
4.py
This script creates a Streamlit app that serves as a medical vocabulary dictionary. It allows users to search for English medical terms, view their translations, and listen to the pronunciation of the terms. The app uses the gTTS library to generate audio files for the terms.
"""
import streamlit as st
import pandas as pd
from gtts import gTTS
import os

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("medical_vocabulary.csv", quotechar='"', encoding='utf-8', on_bad_lines='skip', engine='python')
    return df

df = load_data()

# Build wordlist from English medical terms
wordlist_df = df[['medical_english_original']].drop_duplicates().sort_values(by='medical_english_original').reset_index(drop=True)
wordlist_df.columns = ['English Medical Terms']

# UI setup
st.set_page_config(page_title="Medical Dictionary", layout="wide")
st.title("📘 Medical Vocabulary Dictionary")

# Input
search_term = st.text_input("🔍 Enter an English medical term:").strip().lower()

# Search results
if search_term:
    result_df = df[df['medical_english_original'].str.lower().str.contains(search_term)]

    if not result_df.empty:
        st.write("### 📖 Result:")
        st.dataframe(result_df[['medical_english_original', 'vietnamese_translation']], use_container_width=True)

        # Audio pronunciation
        audio_file = f"audio_{search_term}.mp3"
        if not os.path.exists(audio_file):
            tts = gTTS(search_term)
            tts.save(audio_file)

        st.audio(audio_file, format="audio/mp3")
        with open(audio_file, "rb") as f:
            st.download_button("⬇️ Download Pronunciation", f, file_name=audio_file)
    else:
        st.warning("No match found.")
else:
    st.info("Enter a term to search.")

# Show full wordlist
if st.checkbox("📘 Show Full Wordlist"):
    st.dataframe(wordlist_df, use_container_width=True, height=500)
