import streamlit as st

# basic like title
# text and some thing different

st.title("Hi What are you doing write now :) ")
st.text("hi my name is dipanshu garg")

x1 = list(st.columns(4))
x1[0].text("hii")
x1[1].text("hii")
x1[2].text("hii")
x1[3].text("hii")

# x2.text("hello")

# Lets Create that whatever i am thinking of
st.markdown("<H1>Hi my name is dipanshu garg </H1>",unsafe_allow_html=True)


