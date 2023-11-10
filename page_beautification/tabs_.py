import streamlit as st

tab1, tab2 = st.tabs(["Cat", "Dog"])

tab1.image("https://static.streamlit.io/examples/cat.jpg")
tab2.image("https://static.streamlit.io/examples/dog.jpg")