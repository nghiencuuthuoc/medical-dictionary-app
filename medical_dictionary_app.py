"""
3.py
"""
import streamlit as st
import pandas as pd
from gtts import gTTS
import os
import tempfile


st.set_page_config(page_title="Medical Dictionary",     
                   page_icon="https://raw.githubusercontent.com/nghiencuuthuoc/PharmApp/refs/heads/master/images/nct_logo.png",
    layout="wide",
    initial_sidebar_state="auto",
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("medical_vocabulary.csv")

df = load_data()
english_terms = df['original'].dropna().unique().tolist()
english_terms.sort()

st.write("""
# PharmApp Suite
## 🧠 AI for Drug Discovery and Development 🧪
Copyright 2025 | Nghiên Cứu Thuốc | RnD_Pharma_Plus | www.nghiencuuthuoc.com
""")

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


def load_wordlist():
    with open("wordlist.txt", "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    return pd.DataFrame(words, columns=["English Terms"])

# Hiển thị wordlist nếu checkbox được chọn
if st.checkbox("📝 Show English Wordlist (from wordlist.txt)"):
    wordlist_df = load_wordlist()
    st.dataframe(wordlist_df, use_container_width=True, height=600)


# Xem toàn bộ từ điển
if st.checkbox("📚 Show full dictionary"):
    st.dataframe(df, use_container_width=True, height=800)
