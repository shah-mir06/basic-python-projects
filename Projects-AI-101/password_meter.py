import streamlit as st

def check_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    return score

st.title("Welcome to Password Strength Meter.")
st.markdown("---")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password:
        score = check_password(password)
        if score == 0:
            st.write("Very Weak Password")
        elif score == 1:
            st.write("Weak Password")
        elif score == 2:
            st.write("Moderate Password")
        else:
            st.write("Strong Password")
    else:
        ("Please Enter your Password")

st.markdown("---")
st.write("\n**Developed by Shah Mir Usman**")

