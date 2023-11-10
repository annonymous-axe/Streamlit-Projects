import streamlit as st
import time

st.set_page_config(page_title="Kamlesh Baviskar", page_icon="-", layout='wide')
with st.spinner("Wait for it..."):
    time.sleep(5)
with st.empty():
    st.write("You are done!")
    time.sleep(2)
    st.write("Thanks for being patient.")
time.sleep(.5)
with st.empty():
    st.write("Processing...")
    time.sleep(1)
    for seconds in range(100):
        time.sleep(.1)
        st.progress(seconds+1, text="Processing...")
    st.success("Completed!")

st.balloons()   
# st.snow()

