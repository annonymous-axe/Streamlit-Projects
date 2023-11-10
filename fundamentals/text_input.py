import streamlit as st
from datetime import datetime

st.subheader('1. Text Input')
name = st.text_input('Enter your name :', placeholder='Kamlesh Baviskar')
st.write('Welcome, ', name)

st.subheader('2. Password Input')
password = st.text_input('Enter your password: ', placeholder='kam@143', type='password')

st.subheader('3. Text Area')
text_area = st.text_area('Tell me about your self in 500 words.', max_chars=500, help='Maximum characters aloowed are 500!')

st.subheader('4. Numeric Input')
st.number_input('Enter your age:', min_value=10, max_value=80, step=1, value=20)

st.subheader('5. Date Input')
today = datetime.now().date()
date = st.date_input("Enter Date :", min_value=today, value=today, max_value=today.replace(today.year + 1))
st.write("You've selected date\t:", datetime.strftime(date, "%m/%d/%Y"))