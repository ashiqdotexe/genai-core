import streamlit as st
import pandas as pd

st.title("Simple widget")
name = st.text_input("Please enter your name")
if name:
    st.write(f"Hello {name}")
age = st.slider("Please enter your age", 0, 100, 25)
st.write(age)
options = ["Python", "Java", "C++", "Javascript"]
select = st.selectbox("Please choose an option", options)
st.write(select)
data = {
    "name": ["Ashiq", "Adnan", "Aziz"],
    "age": [25, 18, 60],
    "hobby": ["Playing", "Drawing", "Singing"],
}
df = pd.DataFrame(data)
df.to_csv("Sample.csv")

st.write(df)
uploader = st.file_uploader("Please upload a csv", type="csv")
if uploader is not None:
    df1 = pd.read_csv(uploader)
    st.write(df1)
