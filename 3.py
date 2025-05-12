"""
3.py
"""
import streamlit as st
import pandas as pd
from gtts import gTTS
import os
import tempfile

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("medical_vocabulary.csv")

df = load_data()
english_terms = df['original'].dropna().unique().tolist()
english_terms.sort()

st.set_page_config(page_title="Medical Dictionary", layout="wide")
st.title("📘 Medical Vocabulary Dictionary")

# Chọn từ từ dropdown
selected_term = st.selectbox("📂 Select a medical term:", [""] + english_terms)

# Nếu chọn từ dropdown
if selected_term:
    result_df = df[df['original'].str.lower() == selected_term.lower()]
    if not result_df.empty:
        st.write("### 📖 Result:")
        st.dataframe(result_df)

        # Phát âm
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts = gTTS(selected_term)
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
    else:
        st.warning("No match found.")
else:
    st.info("Please select a term from the dropdown.")

# Xem toàn bộ từ điển
if st.checkbox("📚 Show full dictionary"):
    st.dataframe(df, use_container_width=True, height=800)
