# NumberChecker.py
import streamlit as st

st.title("🔢 Number Checker Functions")

# Input
num = st.number_input("Enter a number:", step=1)

# Functions
def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Button to check
if st.button("Check Number"):
    st.write("✅ **Results:**")
    
    st.write(f"👉 Positive: {'Yes' if is_positive(num) else 'No'}")
    st.write(f"👉 Even: {'Yes' if is_even(num) else 'No'}")
    st.write(f"👉 Prime: {'Yes' if is_prime(num) else 'No'}")
