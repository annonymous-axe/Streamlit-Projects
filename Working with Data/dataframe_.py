import streamlit as st
import pandas as pd

path = "C:\\Users\\Kamlesh Baviskar\\OneDrive\\Desktop\\StreamLit Projects\\Working with Data\\Data.csv"
df = pd.read_csv(path)
st.subheader("1. Displaying the whole DataFrame")
st.dataframe(df)

st.subheader("2. Displaying the head of DataFrame")
st.dataframe(df.head())

st.subheader("3. Displaying the tail of DataFrame")
st.dataframe(df.tail())

st.subheader("4. Displaing first 2 rows")
st.dataframe(df.head(2))

st.subheader("5. Displaying JSON")

js = [{"pid": 1, "name":"5 star"},
      {"pid": 2, "name":"Milky-Bar"},
      {"pid": 3, "name":"Multigrain BreadButter"},
      {"pid": 4, "name":"Butter"},
      {"pid": 5, "name":"Dairy Milk"},]

st.json(js)

st.subheader("6. Discribe the dataframe")
# st.write(df.describe())
# st.subheader(df.describe())
st.table(df.describe())