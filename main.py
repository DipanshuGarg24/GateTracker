import streamlit as st
from data import *

# st.set_page_config(layout="wide")

# Title :)
st.markdown("<h1 style='text-align:center'>🎯 Gate Tracker 🏴‍☠️</h1>",unsafe_allow_html=True)
st.divider()
#-----------------------------------------------------------------------------

# -- Getting the Data :)
# Become easyfor me


# -- For Updating the checkbox
def updateCheckbox(subName):
    if subName == None:
        return
    x = st.button(f"HEllo {subName}")
    if x:
        st.checkbox("hellp")

# login system :)

login = True
if not login:
    pass
else:
    st.info("Note : Topic with * marks are important")
    subSelect = st.selectbox("Choose the Subject Name",[None , "Operating system","Computer Organization"],index=0)
    # here i need to display the content of the choosen subject
    updateCheckbox(subSelect)


# ------------------------------------------------------------------
# lets make some footer :)
st.divider()
st.markdown("<h5 style = 'text-align:center'>Made with 💝 By Dipanshu Garg</h1>",unsafe_allow_html=True)
st.text("")
# making some social media buttons :)
st.markdown("""
    <div style="display: flex; justify-content:center;">
        <div style="margin-right: 20px;">
              <a href='https://www.facebook.com/YourPage'><img src='https://img.icons8.com/fluent/48/000000/gmail.png' width='30'></a>
        </div>
        <div  style="margin-right: 20px;">
            <a href='https://www.facebook.com/YourPage'><img src='https://img.icons8.com/fluent/48/000000/linkedin.png' width='30'></a>
        </div>
        <div >
            <a href='https://www.facebook.com/YourPage'><img src='https://img.icons8.com/fluent/48/000000/instagram-new.png' width='30'></a>
        </div>
    </div>
    """, unsafe_allow_html=True)


