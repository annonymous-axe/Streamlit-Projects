import streamlit as st
import numpy as np
import pandas as pd

# data
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['L-1', 'L-2', 'L-3'] )

st.title("1. Line Chart")
# chart_data = pd.DataFrame(np.random.randn(20,3), columns=['L-1', 'L-2', 'L-3'] )
st.line_chart(chart_data)

st.title("2. Area Chart")
# chart_data = pd.DataFrame(np.random.randn(20,3), columns=['A-1', 'A-2', 'A-3'] )
st.area_chart(chart_data)

st.title("3. Bar Chart")
# chart_data = pd.DataFrame(np.random.randn(20,3), columns=['B-1', 'B-2', 'B-3'] )
st.bar_chart(chart_data)