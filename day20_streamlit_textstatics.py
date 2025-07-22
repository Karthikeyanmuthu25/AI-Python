# TextStatistics.py

import streamlit as st
import re

# Streamlit App Title
st.title("📝 Text Statistics Tool")

# Input from user
text = st.text_area("Enter your paragraph below:", height=200)

# Function to calculate statistics
def compute_stats(text):
    words = text.split()
    num_words = len(words)

    # Simple sentence split using punctuation
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    num_sentences = len(sentences)

    num_chars = len(text)

    return num_words, num_sentences, num_chars

# Button to trigger analysis
if st.button("Analyze Text"):
    if text.strip():
        words, sentences, chars = compute_stats(text)

        st.subheader("📊 Statistics")
        st.write(f"**Word Count:** {words}")
        st.write(f"**Sentence Count:** {sentences}")
        st.write(f"**Character Count:** {chars}")
    else:
        st.warning("Please enter some text before analyzing.")
