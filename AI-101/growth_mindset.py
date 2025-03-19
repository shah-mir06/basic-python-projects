import streamlit as st
import random

affirmations =[
    "Mistakes help me learn and grow!",
    "I can do hard things!",
    "Challenges help me become stronger!",
    "I am constantly learning and improving!",
    "My effort and attitude determine my abilities!"]

challenges = [
    "Write down one mistake you learned from today.",
    "Try a new problem without fear of failure.",
    "Give yourself positive feedback on a challenge you faced.",
    "Ask for constructive feedback from a friend or teacher.",
    "Reflect on how you overcame a past obstacle."]

st.title("Welcome to Growth Mindset Challenge!")
st.markdown("---")

affirmation = random.choice(affirmations)
st.subheader("Today's Affirmation:")
st.success(affirmation)

challenge = random.choice(challenges)
st.subheader("Your Growth Mindset Challenge:")
st.info(challenge)

st.markdown("### Share Your Reflection")
reflection = st.text_area("How did this challenge help you grow?")
if st.button("Submit Reflection"):
    if reflection:
        st.success("Thank you for sharing! Keep growing!")
    else:
        st.warning("Please write something before submitting!")

st.markdown("---")
st.write("\nDeveloped by Shah Mir Usman")
st.markdown("---")
