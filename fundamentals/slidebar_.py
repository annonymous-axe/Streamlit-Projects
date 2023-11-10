import streamlit as st

with st.sidebar:
    st.title('Rate Yourself')
    languages = st.text_input('Enter the programming laguages you know with comma seperation', value='python')
    languages = [i.strip() for i in languages.split(', ')]

st.subheader('How would you rate your experience in the following programming languages & tools?')

for language in languages:
    st.write(language)
    st.slider(language, min_value=0., max_value=10., step=.5)
