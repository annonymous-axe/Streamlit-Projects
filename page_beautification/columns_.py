import numpy as np
import time
import streamlit as st

# static
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# dynamic

num = st.number_input("How many columns do you want?", 1, 10)
cols = st.columns(num)

for col in cols:
    with col:
        st.image("https://static.streamlit.io/examples/dog.jpg")