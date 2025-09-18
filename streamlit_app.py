import streamlit as st

st.title("Welcome, this is a test page")
st.write(
    "I use this page to explore what I can do with Streamlit."
)

x = st.slider('Get points by moving the slider!')
st.write('You get ', x * x, ' points!')
