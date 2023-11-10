import streamlit as st

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