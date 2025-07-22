import streamlit as st

# App title
st.title("📧 Email Username Extractor")

# User input
email = st.text_input("Enter your email address:")

# Extract username
def extract_username(email):
    if "@" in email:
        return email.split("@")[0]
    return "Invalid email address"

# Display result
if email:
    username = extract_username(email)
    st.success(f"Username: {username}")
