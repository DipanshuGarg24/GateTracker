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

def updateCheckbox(subName):
    if subName == None:
        return
    st.info("Note : Topic with * marks are important")
    st.text("")
    st.progress(10)
    with st.container(height=300,border=True):
        st.checkbox("1.Computer Network")
        st.checkbox("2.Operating system")
        st.checkbox("3.Computer Organization Architecture")
        st.checkbox("4.")
        st.checkbox("5.")
        st.checkbox("6.")
        st.checkbox("7.")
        st.checkbox("8.")
        st.checkbox("9.")
        st.checkbox("10.")
        st.checkbox("11.")

# login system :)


login = True

if not login:
    with st.empty() as c:
        st.write("Hello Dipanshu Garg")

else:
    st.caption(f"Your Overall Progress : {OvProg}%")
    progBar = st.progress(OvProg)
    st.divider()
    subSelect = st.selectbox("Choose the Subject Name",[None , "Operating system","Computer Organization"],index=0)
    # here i need to display the content of the choosen subject
    updateCheckbox(subSelect)


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

