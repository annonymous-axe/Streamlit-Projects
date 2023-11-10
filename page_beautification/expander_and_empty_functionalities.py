import streamlit as st
import numpy as np
import time

cases = []
for _ in range(100):
    cases.append(np.random.randint(1,7))
# st.write(cases)

data = []
for i in range(1, 7):
    data.append(cases.count(i))

st.header("Frequency of getting a Face")
st.bar_chart({"data": data})

with st.expander("See Explanation"):
    st.write('''
            The above chart shows some numbers I got from rolling a dice 100 times and its
             basically about how many times each face appers.
            ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.write("You need to wait for 10 seconds.")
with st.empty():
    for seconds in range(1, 11):
        st.write(str(seconds)+" seconds completed.")
        time.sleep(1)
    st.write("You are done!")