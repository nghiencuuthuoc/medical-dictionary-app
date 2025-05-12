import streamlit as st
import pandas as pd
from gtts import gTTS
import os

# Load data
df = pd.read_csv("medical_vocabulary.csv")

st.set_page_config(page_title="Medical Dictionary", layout="wide")
st.title("📘 Medical Vocabulary Dictionary")

# Search box
search_term = st.text_input("🔍 Enter an English medical term:").strip().lower()

# Filter and play audio
if search_term:
    result_df = df[df['original'].str.lower() == search_term]
    
    if not result_df.empty:
        st.write("### 📖 Result:")
        st.dataframe(result_df)

        # Tạo âm thanh bằng gTTS
        tts = gTTS(search_term)
        audio_path = f"temp_{search_term}.mp3"
        tts.save(audio_path)

        # Phát âm thanh
        st.audio(audio_path, format="audio/mp3")

        # Xóa file âm thanh sau khi dùng (tuỳ chọn)
        # os.remove(audio_path)
    else:
        st.warning("No exact match found.")
else:
    st.info("Enter a term to search for its Vietnamese translation.")
