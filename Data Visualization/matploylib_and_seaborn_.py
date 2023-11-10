import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("Data visualization with Matplotlib and Seaborn")

st.text("1. Displaying the Dataset")
df = pd.read_csv("iris.csv")
st.dataframe(df)

st.text("2. Bar plot using Matplotlib")
fig = plt.figure(figsize=(15,8))
df['Species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.text("3. Displot with Seaborn")
fig = plt.figure(figsize=(15,8))
sns.distplot(df['SepalLengthCm'])
st.pyplot(fig)

st.text("4. Display Multiple graphs")

col1, col2 = st.columns(2)

with col1:
    col1.header("KDE=False")
    fig1 = plt.figure()
    sns.distplot(df['SepalLengthCm'], kde=False)
    st.pyplot(fig1)

with col2:
    col2.header("KDE=True")
    fig2 = plt.figure()
    sns.distplot(df['SepalLengthCm'], kde=True)
    st.pyplot(fig2)