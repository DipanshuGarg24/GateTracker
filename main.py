import streamlit as st

# basic like title
# text and some thing different
#
# st.title("Hi What are you doing write now :) ")
# st.text("hi my name is dipanshu garg")
#
# x1 = list(st.columns(4))
# x1[0].text("hii")
# x1[1].text("hii")
# x1[2].text("hii")
# x1[3].text("hii")
#
# # x2.text("hello")
#
# # Lets Create that whatever i am thinking of
# st.markdown("<H1>Hi my name is dipanshu garg </H1>",unsafe_allow_html=True)

def makeContent():
    st.markdown("<h1 style='text-align: center;'>Computer Network</h1>", unsafe_allow_html=True)
    st.markdown("<hr>",unsafe_allow_html=True)

    # making the coulmns
    # lets say five coulmns
    head = list(st.columns(5))
    head[0].text("")
    head[1].text("Concept")
    head[2].text("1.Revision")
    head[3].text("PYQS")
    head[4].text("revision")

    x = list(st.columns(5))
    x[0].text("IPV4 Adressing")
    x[1].checkbox("",key=2)
    x[2].checkbox("",key=3)
    x[3].checkbox("",key=4)

    y = list(st.columns(5))
    y[0].text(" Error Control")
    y[1].checkbox("", key=21)
    y[2].checkbox("", key=31)
    y[3].checkbox("", key=41)
    topics = ["IPV4 Adressing","Error Control"]

makeContent()
