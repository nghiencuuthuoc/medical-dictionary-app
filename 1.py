import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("medical_vocabulary.csv")

st.set_page_config(page_title="Medical Dictionary", layout="centered")
st.title("📘 Medical Vocabulary Dictionary")

# Search box
search_term = st.text_input("🔍 Enter an English medical term:")

# Filter results
if search_term:
    result_df = df[df['original'].str.contains(search_term, case=False, na=False)]
    if not result_df.empty:
        st.write("### 📖 Results:")
        st.table(result_df)
    else:
        st.warning("No matching medical terms found.")
else:
    st.info("Enter a term to search for its Vietnamese translation.")

# Show all option
if st.checkbox("📚 Show full dictionary"):
    # st.dataframe(df)
    st.dataframe(df, use_container_width=True, height=800)
