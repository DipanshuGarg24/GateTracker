# Dipanshu Garg
import streamlit as st


st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-right:0rem;
                    padding-left:0rem;
                }
        </style>
        """, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

st.markdown("<h1 style='text-align:center'>🎯🎯 GATE 🎯🎯 </h1>",unsafe_allow_html=True)
st.divider()

st.markdown("<h5 style = 'text-align:center;text-color:yellow'> Hi,My name is Dipanshu garg , i got AIR - 48 in GATE CSE 24 exam . Let's think about the GATE exam very well and make the most out of the resources and FAQs provided here to ace your preparation</h5>",unsafe_allow_html=True)

# HERE I WILL PROVIDE SOME BUTTONS
if st.button("Preparation Material",type="primary",use_container_width=True):
    st.info("Under construction ... once complete i will notfiy through linkedin post ")
st.divider()

st.markdown("<h1>Frequently Asked Questions .... </h1>",unsafe_allow_html=True)
x = st.checkbox("FAQS click here ",value=0)
if x:
    # Ques 1
    with st.expander("Q1. What is the GATE exam? Who can give this exam?"):
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q2. Can you describe your journey of preparing for the GATE exam?"): #2
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q3. Is it possible to crack the GATE exam without any coaching help?"): #3
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q4. How can I start my preparation for the GATE exam? Can you provide a roadmap?"): #4
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q5. From which subject should I start my GATE preparation?"): #5
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q6. Which test series is the best for GATE CSE or Data Analytics?"): #6
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q7. When should I start taking test series for the GATE exam?"): #7
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q8. What are some good YouTube playlists for self-study for the GATE exam?"): #8
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q9. If I want to take coaching, which coaching institute should I choose for the GATE exam?"): #9
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q10. There are only 8-9 months left until the GATE exam. Can I still crack it?"): #10
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q11. How many hours should I study daily for the GATE exam?"): #11
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q12. Can you provide notes with questions for GATE preparation?"): #12
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q13. How should I approach solving previous years' GATE questions?"): #13
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q14. How can I prepare for the GATE exam while working a job?"): #14
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q15. What is the importance of short notes in GATE preparation, and how are they useful?"): #15
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q16. I am unable to solve problems even though I understand the topics. What should I do? I feel frustrated."): #16
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q17. Which subject should I start with for GATE preparation?"): #17
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q18. Which test series should I buy for the GATE exam?"): #18
        with st.chat_message(name='user'):
            st.write("Test series play a vital role in GATE preparation, and they should be chosen wisely. The test series should have very few errors and contain exam-oriented questions that are not too hard or too easy. My personal suggestion (not a paid promotion) is to buy test series from Go Classes or Unacademy.")
    with st.expander("Q19. Do I need to read from standard textbooks? What is the importance of reading standard books, or can I skip them?"): #19
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q20. Are there any other resources you would suggest for GATE preparation?"): #20
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q21. I am in the first year of college. How can I start preparing for the GATE exam?"): #21
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")
    with st.expander("Q22. My college placements are happening, and I am scared. How should I balance preparing for the GATE exam?"): #22
        st.audio('Kbps.mp3')
        st.write("hello my name is dipanshu garg")

# here all the questions end

# section for any doubt then person can ask :)
with st.container():
    st.write("---")
    st.header("Any Other Question ...")
    st.write("Still doubt left ... don't hesitate ask your question :) ")
    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/dipanshuaggarwal17@gmail.com" , method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)


#footer
st.divider()
st.markdown("<h4 style = 'text-align:center'>Made with 💝 By Dipanshu Garg</h4>",unsafe_allow_html=True)
st.markdown("<h6 style = 'text-align:center'>Follow me on Linkedin and other social media platforms </h6>",unsafe_allow_html=True)
st.text("")
# making some social media buttons :)
st.markdown("""
    <div style="display: flex; justify-content:center;">
        <div style="margin-right: 20px;">
              <a href=''><img src='https://img.icons8.com/fluent/48/000000/github.png' width='30'></a>
        </div>
        <div  style="margin-right: 20px;">
            <a href=''><img src='https://img.icons8.com/fluent/48/000000/linkedin.png' width='30'></a>
        </div>
        <div >
            <a href=''><img src='https://img.icons8.com/fluent/48/000000/instagram-new.png' width='30'></a>
        </div>
    </div>
    """, unsafe_allow_html=True)

