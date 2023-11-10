import streamlit as st

def rate_yourself():
    with st.sidebar:
        st.title('Rate Yourself')
        languages = st.text_input('Enter the programming laguages you know with comma seperation', value='python')
        languages = [i.strip() for i in languages.split(', ')]

    st.subheader('How would you rate your experience in the following programming languages & tools?')

    for language in languages:
        st.write(language)
        st.slider(language, min_value=0., max_value=10., step=.5)    

def bmi_calculator():
    st.title('BMI Calculator')

    with st.form('BMI Calculator'):
        col1, col2, col3 = st.columns([3,2,1])
    with col1:
        weight = st.number_input("Enter your weight in KGs :")
    with col2:
        height = st.number_input("Enter your height in meter :")
    with col3:
        submit = st.form_submit_button('Calculate')

    if submit:
        bmi = round((weight / (height**2)), 2)
        if bmi <= 18.5:
            st.error("Underweight")
        elif bmi > 18.5 and bmi <= 24.9:
            st.success("Healthy / Normal")
        else:
            st.warning('Overweight')    

option = st.sidebar.selectbox('Menu', ['BMI', 'Rate Yourself'])

if option == 'BMI':
    bmi_calculator()
elif option == 'Rate Yourself':
    rate_yourself()