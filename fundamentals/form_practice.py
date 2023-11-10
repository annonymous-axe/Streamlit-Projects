import streamlit as st

with st.form("Without Lines"):
    row1= st.columns(1)

with row1:
    st.header('Outside form')
    out_text_input = st.text_input('Outside text input')
    out_text_area = st.text_area('Outside text area')

# with st.form("Without Lines"):
#     row1, row2, row3 = st.columns(1)

# with row1:
#     st.header('Inside form')
# with row2:
#     in_text_input = st.text_input('Inside text input')
# with row3:
#     in_text_area = st.text_area('Inside text area')

