import streamlit as st
from data import *
import time
# st.set_page_config(layout="wide")
# Title :)
st.markdown("<h1 style='text-align:center'>🎯 Gate Tracker 🏴‍☠️</h1>",unsafe_allow_html=True)
st.divider()
#-----------------------------------------------------------------------------

OvProg = 25



# -- Getting the Data :)
# Become easyfor me



# -- For Updating the checkbox

def MakeQr(data):
    pass

def LoadData():
    pass

def StoreData():
    pass

def updateCheckbox(subindex):
    if subindex == 0:
        return
    st.text("")
    st.subheader(f"{SubList[subindex]}")
    st.caption("Your Subject Progress : ")
    st.progress(10)
    st.text("")
    subject = SubList[subindex]
    if subject not in st.session_state:
        # Initialize checkbox values for the subject
        st.session_state[subject] = {}
        for i in range(20):
            st.session_state[subject][f"topic_{i}"] = False

    subjectref = st.session_state[subject]

    with st.container(height=300,border=True):
        for i in range(20):
            topic_key = f"topic_{i}"
            subjectref[topic_key] = st.checkbox(f"Topic {i + 1}{subject}",subjectref[topic_key])



# login system :)


login = True



if not login:
    with st.empty() as c:
        st.write("Hello Dipanshu Garg")

else:
    st.caption(f"Your Overall Progress : {OvProg}%")
    progBar = st.progress(OvProg)
    st.divider()
    subSelect = st.selectbox("Choose the Subject Name",SubList,index=0)
    # here i need to display the content of the choosen subject
    updateCheckbox(SubList.index(subSelect))


# ------------------Save The Progress in the firebase -------
st.divider()
st.caption("Make sure to save your progress before leaving the website, or you'll lose any marks or progress you've made.")
col = list(st.columns([1,2,1]))
save = col[1].button("Save Progress",type='primary',use_container_width=True)
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# lets make some footer :)
st.divider()
st.markdown("<h5 style = 'text-align:center'>Made with 💝 By Dipanshu Garg</h1>",unsafe_allow_html=True)
st.text("")
# making some social media buttons :)
st.markdown("""
    <div style="display: flex; justify-content:center;">
        <div style="margin-right: 20px;">
              <a href=''><img src='https://img.icons8.com/fluent/48/000000/gmail.png' width='30'></a>
        </div>
        <div  style="margin-right: 20px;">
            <a href=''><img src='https://img.icons8.com/fluent/48/000000/linkedin.png' width='30'></a>
        </div>
        <div >
            <a href=''><img src='https://img.icons8.com/fluent/48/000000/instagram-new.png' width='30'></a>
        </div>
    </div>
    """, unsafe_allow_html=True)
# -----------------------------------------

