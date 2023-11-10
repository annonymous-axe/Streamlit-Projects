import streamlit as st

st.subheader('1. Radio Button')
sex = st.radio("Select you gender", options=('Male', 'Female', 'Prefer not to say'), help='Choose one', horizontal=True)
st.write('Selected Gender\t:', sex)

st.subheader('2. Select Box')
option = st.selectbox("Select options you prefer", options=('Data Analyst', 'ML', 'DL', 'AI'), help='Choose one')
st.write("You've selected\t:", option)

st.subheader('3. Multi-Select Box')
options = st.multiselect("Select options you interested", options=('Data Analyst', 'ML', 'DL', 'AI'), help='Choose multiple', default='AI')
# st.write("You've in list\t:", options)

st.subheader('4. Button')
if st.button('Say Hi'):
    st.write('Hi')
else:
    st.write('Click the button.')

st.subheader('5. Checkbox')
if st.checkbox('Agree all terms and conditions', help="You must agree to proceed"):
    st.write('Now, you may proceed.')

st.subheader('6. Color Picker')
color = st.color_picker('Choose Your Favorite color', value='#d61ce8')
st.write("You've selected\t:", color, "color")

st.button('Submit your response')
