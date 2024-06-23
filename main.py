# Dipanshu Garg
import time

import streamlit as st
# from streamlit_js_eval import streamlit_js_eval


# Function to inject custom CSS based on screen width

# x = int(streamlit_js_eval(js_expressions='screen.width', key = 'SCR'))
# if x<=1000:
st.set_page_config(layout="wide")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    
                }
        </style>
        """, unsafe_allow_html=True)

# Custom CSS and JavaScript to control audio playback
custom_js = """
<script>
const setupAudioControls = () => {
    const audios = document.querySelectorAll("audio");
    audios.forEach(audio => {
        audio.addEventListener("play", function() {
            audios.forEach(otherAudio => {
                if (otherAudio !== audio) {
                    otherAudio.pause();
                }
            });
        });
    });
};

document.addEventListener("DOMContentLoaded", setupAudioControls);
window.addEventListener("load", setupAudioControls);
</script>
"""

# Inject the JavaScript into the Streamlit app
st.markdown(custom_js, unsafe_allow_html=True)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

x = st.columns((1,3,1))

with x[1].container():
    st.markdown("<h1 style='text-align:center'>🎯🎯 GATE 🎯🎯 </h1>",unsafe_allow_html=True)
    st.divider()

    st.markdown("<h5 style = 'text-align:center;text-color:yellow'>Hi, My name is Dipanshu Garg, I got AIR - 48 in GATE CSE 24 exam. I am an upcoming M.Tech CSE student at IIT Bombay. Let's discuss about the GATE exam very well and make the most out of the resources and FAQs provided here to ace your preparation.</h5>",unsafe_allow_html=True)

    # HERE I WILL PROVIDE SOME BUTTONS
    # if st.("www.google.com"):
        
    st.link_button(url="https://t.me/+EDyXlTTlMmRmYzQ1",label="Preparation Material",type="primary",use_container_width=True)
        # st.info("Under construction ... once complete i will notfiy through linkedin post ")
    st.divider()

    with st.expander("Youtube Video Playlist and Videos "):
           st.success("Simply click on the names, and you'll be automatically redirected to the YouTube playlist.")
           with st.container(border=True):

               # 1
               st.write('''1. **Engineering Maths**''')
               cols = list(st.columns(3))
               cols[0].page_link("https://youtube.com/playlist?list=PLiSPNzs4fD9sXOHKPjlxksPJintVIBCHE&si=btmRm2xhaL8i0vaB",label="Maths by Pallav Sir ",icon="🏹")
               cols[1].page_link("https://youtube.com/playlist?list=PLvTTv60o7qj-q4idV59uKIkBPOxe-govX&si=Pl_EU2evbixQGbv4",label="PW fasttrack",icon="🏹")
               cols[2].page_link("https://youtube.com/playlist?list=PLynLXReWAxdHCNElweqqhK_BVxzTs4eaU&si=-W8Rv05fqeY1Ai9n",label="Math by Byjus's ",icon="🏹")
               st.divider()


               # 2
               st.write('''2. **Discrete Maths**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PLC36xJgs4dxEYmhzVBW7nBdftFZ4xmiF1&si=XK5Z3TKACGsEFY_x",
                   label="Amit Khurana Sir", icon = "⭕")
               cols[1].page_link(
                   "https://youtu.be/09_LlHjoEiY?si=QHGmAKXU0_yb0pHV",
                   label="Graph Theorey - FREECODECAMP", icon = "⭕")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH-T76wHeHTlp6hoD-inQLPp&si=fu5jec0kEtxlmcNj",
                   label = "DM by Baba sir",
                   icon = "⭕",
               )

               x[1].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH-Q3tVhgpxptNLwxai5N2Ke&si=bXcu8iN6ALJl9NBe",
                   label = "PW fasttrack",
                   icon = "⭕",
               )
               st.divider()

               # 3

               st.write('''3. **C Programming**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtu.be/zuegQmMdy8M?si=uk_K2ts4vw3YEjac",
                   label="Pointers in C", icon="🔅")
               cols[1].page_link(
                   "https://youtu.be/09_LlHjoEiY?si=QHGmAKXU0_yb0pHV",
                   label="C prog. Crash Course", icon="🔅")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PLynLXReWAxdFJ6un2uX5Rcq2UIxmQVNqz&si=dlFYpTo6j95oaBj-",
                   label="Byjus's Playlist",
                   icon="🔅"
               )

               x[1].page_link(
                   "https://youtube.com/playlist?list=PLBlnK6fEyqRggZZgYpPMUxdY1CYkZtARR&si=UjDT9VOAKiv5JsYo",
                   label="Nesso Academy",
                   icon="🔅",
               )
               st.divider()


               st.write('''4. **Data Structure**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtu.be/B31LgI4Y4DQ?si=4m-Sh93IUAhpzA7C",
                   label="Must Watch", icon="🌐")
               cols[1].page_link(
                   "https://youtube.com/playlist?list=PLir19lgiavA3naiXm-LQY8MrS6Y_X6QIL&si=8BEkvErORyPSqH_R",
                   label="Pankaj Sir", icon="🌐")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH_Phqkk2k_WFWHz0rDBBubC&si=n4Dg_MwSmJ7KpkSn",
                   label="PW crash Course",
                   icon="🌐",
               )

               x[1].page_link(
                   "https://youtu.be/IJDJ0kBx2LM?si=vXnwNUip5QK4PeOR",
                   label="Recursion best video",
                   icon="🌐",
               )
               st.divider()

               #     -------------------------------------

               st.write('''5. **Algorithms**''')

               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtu.be/2ZLl8GAk1X4?si=j_KvC5aVFL6p8taC",
                   label="48hr DSA 😲😲", icon="⚪")
               cols[1].page_link(
                   "https://youtube.com/playlist?list=PLC36xJgs4dxFCQVvjMrrjcY3XrcMm2GHy&si=I6zNw8m8qiIi_yBs",
                   label="Algo by Amit khurana", icon="⚪")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH87NTeUU8AteQQ7cmO33gOY&si=7SK0sNDfLP7Khqx-",
                   label="PW crash Course",
                   icon="⚪",
               )

               x[1].page_link(
                   "https://youtube.com/playlist?list=PLir19lgiavA0rXimkPicWZv7CnErdVpZ9&si=8qfX6dlK_n-0aZ1s",
                   label="Algo by Pankaj Sir ",
                   icon="⚪",
               )

               st.divider()

               # 6
               st.write('''6. **Databases**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PLPvaSRcEQh4kfVIyezAQu9Mvj5FBk_OEN&si=KEWIGXKuCcB6aS-w",
                   label="DBMS by Vijay Sir 😎", icon="🟤")
               cols[1].page_link(
                   "https://youtu.be/ztHopE5Wnpc?si=OkMxeLYpZi9E6Xss",
                   label="Awesome Video-freecodecamp", icon="🟤")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH-Y6z_BaZXV7zDP1tmiaczu&si=czecio8Xwn_UsOiV",
                   label="PW Fasttrack",
                   icon="🟤",
               )
               x[1].page_link(
                   "https://youtube.com/playlist?list=PLC36xJgs4dxGcz7nZaxGxxmbJrcgDXhFk&si=ETD9_tPk2IXE7PEw",
                   label="Amit khurana sir ",
                   icon="🟤",
               )

               st.divider()

               # ------------------------
               st.write('''7. **Digital Electronics**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PL7XXZleXge9Ln2zPAVFiTrvuGpmNAsZpk&si=-apRTvimFAJz-iJs",
                   label="Nesso Academy", icon="🟣")
               cols[1].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH8nznEyq1bdI0M_IfBScJ2H&si=nCsr9RsP1Hfft8mv",
                   label="Crash course - Chandan jha sir ", icon="🟣")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PLgzsL8klq6DLNOHvlkmbvY2QKJ1iu4Djn&si=FxQf3TctSsyBq7O7",
                   label="Gate Academy",
                   icon="🟣",
               )
               x[1].page_link(
                   "https://youtube.com/playlist?list=PLwjK_iyK4LLBC_so3odA64E2MLgIRKafl&si=EwcisOX-dRjo6Uuw",
                   label="All about electrnoics",
                   icon="🟣",
               )
               st.divider()


               st.write('''8. **Computer Architecture**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PLG9aCp4uE-s3WzvFW1nI-7hHWNC8s2RdI&si=f6HDHLl1vyi7Adjy",
                   label="Vishwadeep Gothi Sir", icon="🟡")
               cols[1].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH85a_kkiNN_rj97jPSIWtST&si=RiM484HZYk12LYZQ",
                   label="Vijay Sir -Crash Course", icon="🟡")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PLBlnK6fEyqRgLLlzdgiTUKULKJPYc0A4q&si=ybGe-v3b-JCTR3jH",
                   label="Nesso Academy",
                   icon="🟡",
               )
               st.divider()

               st.write('''9. **Operating system**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PLG9aCp4uE-s17rFjWM8KchGlffXgOzzVP&si=q9CImzxTBAs_jTHN",
                   label="vishwadeep gothi sir", icon="🔵")
               cols[1].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH-PU-aG_BGo9UI-LzsKARSb&si=cScySMMeoOFsoFMH",
                   label="Pw Fasttrack", icon="🔵")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O&si=AmoyJslZAn60KI5s",
                   label="Nesso Academy",
                   icon="🔵",
               )
               st.divider()

               #  ------------------------------------------------------------------------
               st.write('''10. **Computer Network**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PL3eEXnCBViH-hlNCNwdfV7VrEcTquANGa&si=ryyZuw4sfGa16Rwt",
                   label="Ankit Doyla sir ", icon="✅")
               cols[1].page_link(
                   "https://youtu.be/0PbTi_Prpgs?si=N0kYez3-lM5Uuxfh",
                   label="Awesome Video-freecodecamp", icon="✅")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PLC36xJgs4dxHT-TxTy3U1slr5RaBJGaLd&si=3lhUlPi8Rrx0_A82",
                   label="Amit khurana sir",
                   icon="✅",
               )
               x[1].page_link(
                   "https://youtube.com/playlist?list=PLynLXReWAxdHeTnpZG7yqc4By9DH9YmZc&si=sIHCajaNszYSPu-B",
                   label="Byjus exam prep",
                   icon="✅",
               )
               st.divider()

               st.write('''11. **Theorey of Computation**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PLG9aCp4uE-s1P6Z73Gbbh-kdDWwq5Bg7f&si=QcvFn6ZJ89EWAmw6",
                   label="Toc by deva sir", icon="🟢")
               cols[1].page_link(
                   "https://youtube.com/playlist?list=PLPvaSRcEQh4lvkQX4wcN9cy4Rt7RDaZSl&si=gaB7OfL4WP_fM0vU",
                   label="TOC one shots", icon="🟢")
               x = st.columns(2)
               x[0].page_link(
                   "https://youtube.com/playlist?list=PLrjkTql3jnm_TWSXXvWX1_jX-L6f1QJSx&si=AX_-f6r9v5ogCYQf",
                   label="just watch once",
                   icon="🟢"
               )
               x[1].page_link(
                   "https://youtube.com/playlist?list=PLIPZ2_p3RNHiMGiPFIOPJG_ApL43JkILI&si=-w0PeWwPqu_pohB5",
                   label="GO classes superb playlist",
                   icon="🟢",
               )
               st.divider()

               #  -----------------------------------------------
               st.write('''12. **Compiler Design**''')
               cols = list(st.columns(2))
               cols[0].page_link(
                   "https://youtube.com/playlist?list=PLG9aCp4uE-s1NGf_6tQbDBsjLRjquKBE1&si=IpUNS3Ar_I6ecxhV",
                   label="Deva sir playlist", icon="✔")

               x = st.columns(2)
               cols[1].page_link(
                   "https://youtube.com/playlist?list=PLrjkTql3jnm-wW5XdvumCa1u9LjczipjA&si=SKzuJjlIB8bbJckX",
                   label="Education4U",
                   icon="✔",
               )
               x[0].page_link(
                   "https://youtube.com/playlist?list=PLXj4XH7LcRfC9pGMWuM6UWE3V4YZ9TZzM&si=XtMldLusmByT-QGg",
                   label="Sudhakar atchala",
                   icon="✔",
               )
               st.divider()

               st.write('''13. **Aptitude**''')
               with st.chat_message("user"):
                   st.write("Based on my experience, there isn't a single fixed source for aptitude preparation since the syllabus can vary. To improve, you should practice as much as possible. If you get stuck on a question, you can find numerous helpful videos on YouTube. I recommend using RS Aggarwal's books for practice and solving previous years' GATE questions from all branches.")
               st.divider()


    st.markdown("<h1>Frequently Asked Questions .... </h1>",unsafe_allow_html=True)
    x = st.checkbox("FAQS click here ",value=0)
    if x:
        # Ques 1
        with st.expander("Q1. What is the GATE exam? Who can give this exam?"):
            with st.chat_message("ai"):
                st.write('''The Graduate Aptitude Test in Engineering (GATE) is a standardized examination that assesses the understanding of various engineering and science subjects. It is primarily used for admission into postgraduate programs and for recruitment by various public sector undertakings (PSUs) in India.
                            \nEligibility for the GATE Exam:
                            \n1. **Who Can Appear:** The GATE exam is open to candidates who have completed or are in the final year of their Bachelor's degree in Engineering, Technology, Architecture, or a Master's degree in any relevant science subject.
                            \n2. **Interdisciplinary Eligibility:** Yes, students from different branches of engineering or science can take the GATE exam in Computer Science and Engineering (CSE). However, they should ensure they are well-prepared for the CSE syllabus, as it may differ significantly from their primary field of study.
                            \nCandidates are encouraged to review the specific eligibility criteria and syllabus details provided by the GATE organizing institute each year to ensure they meet all requirements and are prepared for the exam content.''')

        with st.expander("Q2. Can you describe your journey of preparing for the GATE exam?"): #2

            with st.chat_message("user"):
                st.write('''Here's how I did it:
                            \n1. After I took my test in 2023 and came home, I looked again at the questions I remembered. I realized that the test wasn't as hard as people make it seem.
                            \n2. First, I printed out all the questions from 2000 to 2022. Then I looked at them to see which ones were easy and which were hard. I didn't actually solve them, just looked.
                            \n3. Then, I made a list of all the stuff I needed to learn. I decided not to join any special classes because I didn't want to spend money, and those classes only care about making money, not helping students.
                            \n4. So, I started looking for free ways to learn. I found videos on YouTube from places like MIT, HARVARD, and FREECODECAMP, and other free stuff from schools.
                            \n5. I also read a lot on Wikipedia and watched lectures from NPTEL. Some people say those lectures are no good, but I think they're great because they're made by top-notch IIT professors. It's funny because we all want to go to IITs but then complain that their lectures are boring and not helpful. Where's the sense in that?
                                 We've formed a mindset that recognizes the abundance of outstanding resources available to us, yet we still feel compelled to gravitate towards coaching centers. We shy away from exploring our subjects independently and hesitate to unleash our full potential.
                            \n6. For some subjects, I read books like CLRS for DS ALGO, but I only focused on the important parts.
                            \n7. To get better at math, I went back to my old school books from grades 11 and 12.
                            \n8. I studied every subject and practiced by solving old test questions. If I didn't understand something, I looked it up on Wikipedia or asked ChatGPT for help.
                            \n9. By the end of August, I had learned most of what I needed to know. I didn't worry about learning everything, just the important stuff. I practiced by doing old test questions from the Byjus exam prep website.
                            \n10. Then, whenever I found something new, I learned about it and made sure to review everything I learned every day.
                            \nThat's pretty much it. 
    ''')
        with st.expander("Q3. Is it possible to crack the GATE exam without any coaching help?"): #3
            with st.chat_message("user"):
                st.write('''Yes, it is possible to crack the GATE exam without any paid coaching. Many of my friends and I got good ranks without any coaching help. You just need a proper plan and the right resources, like YouTube videos and good books.
                        \nHowever, taking coaching can be better because coaching gives you a structured way to study all the topics. This is especially helpful if you are working a job. 
                    \nIf you have a job, I suggest you definitely take coaching and not try to do self-study. But if you are in college and have enough time, self-study can work well. You can use the free resources and study at your own pace.''')
        with st.expander("Q4. How can I start my preparation for the GATE exam? Can you provide a roadmap?"): #4
            with st.chat_message("user"):
                st.write('''Hello Everyone,

Here is a complete roadmap for a self-learner to prepare for the GATE CSE exam.

**Roadmap for GATE CSE Preparation (May to January)**

**Foundation Phase (First 10 Days)**
**May:**
1. **Understand GATE Syllabus and Exam Pattern**
- Familiarize yourself with the complete GATE CSE syllabus.
- Understand the weightage of different subjects and the exam pattern.
- Review previous years' question papers to get an idea of the types of questions asked.

2. **Gather Basic Resources**
- Collect all necessary study materials such as standard textbooks, online resources, and notes.
- Download and organize important lecture notes, PDFs, and YouTube playlists.

3. **Plan Your Study Schedule**
- Create a detailed study plan for the next 8 months.
- Allocate time for each subject based on its weightage and your familiarity with it.
- Include regular breaks and revision periods in your schedule.

4. **Daily Practice of Mathematics and Aptitude**
- Dedicate 30 minutes each day to practicing Mathematics and Aptitude.
- Use any good resource or book for practice.

**Core Subjects Phase (May - June)**
1. **Start with Core Subjects**
- Subjects to cover:
  - C Programming
  - Data Structures (DS)
  - Algorithms
  - Database Management Systems (DBMS)
- Read recommended textbooks such as CLRS for Algorithms.
- Take notes while watching lectures and keep them short and crisp.
- Solve basic Previous Year Questions (PYQs) during the subject completion.

**Deep Dive Phase (July - August)**
2. **Deep Dive into Major Subjects**
- Subjects to cover:
  - Computer Networks (CN)
  - Theory of Computation (TOC)
  - Compiler Design (CD)
  - Operating Systems (OS)
  - Digital Logic Design (DE)
  - Discrete Mathematics (DM)

3. **Consistent Practice and Note-Taking**
- Solve PYQs alongside learning each subject.
- Create PowerPoint presentations (PPTs) for each subject and include difficult problems.
- Daily revision before starting new videos.

**Consolidation Phase (September - October)**
4. **Strengthen Understanding and Practice More**
- Subjects to cover:
  - Mathematics (complete Revision)
  - Computer Organization and Architecture (COA)
- Start solving subject-wise test series.
- Add any extra points learned during problem-solving to your notes.
- Continue daily practice of Mathematics and Aptitude.

**Intensive Practice and Revision Phase (November - December)**
5. **Full Subject Revision and Mock Tests**
- Solve two previous year papers daily.
- Continue with test series: start with subject-wise tests and progress to full-length mock tests.
- Thoroughly revise all subjects.
- Focus on solving complex problems and revising key concepts.

**Final Touch-Up Phase (January)**
6. **Final Revision and Exam Strategy**
- Daily 30-minute meditation to maintain focus and reduce stress.
- Comprehensive daily revision.
- Main focus on revision and solving PYQs.
- Practice time management and simulate exam conditions with mock tests.

**Additional Tips**
- **Daily Routine**: Stick to a consistent daily study routine.
- **Health**: Maintain a balanced diet and get adequate sleep.
- **Breaks**: Take regular short breaks to avoid burnout.
- **Motivation**: Keep yourself motivated and positive throughout your preparation.

Share this roadmap in your network and help fellow aspirants.

All the best, GATE 25 Aspirants!
''')
        with st.expander("Q5. From which subject should I start my GATE preparation?"): #5
             with st.chat_message("user"):
                 st.write('''You can start your preparation with any subject, but it's helpful to follow certain groupings for a better understanding. Here are some suggested sequences:

- **C - Data Structures - Algorithms**: These three subjects should be studied in sequence as they build on each other.
- **Digital Electronics (DE) - Computer Organization and Architecture (COA) - Operating Systems (OS)**: These subjects are related and should be tackled together.
- **Theory of Computation (TOC) - Compiler Design (CD)**: These are best studied in conjunction.
- **Database Management Systems (DBMS) and Computer Networks (CN)**: These can be studied individually at any time.

Additionally, make sure to practice math and aptitude daily to keep your skills sharp.
''')

        with st.expander("Q6. When should I start taking test series for the GATE exam?"): #7
            # st.audio('Kbps.mp3')
            with st.chat_message("user"):
                st.write("There isn't a specific time to start a test series; you don't need to wait until you've completed the entire syllabus. My suggestion is to purchase a test series while you are still preparing your subjects. Take subject tests as you complete each subject. However, start taking full-length mock tests only when you have nearly finished the syllabus to avoid getting demotivated.")

        with st.expander("Q7. How to manage college studies and Gate Preparation ?"):  #
            with st.chat_message("user"):
                st.write('''Managing college studies with GATE preparation can be simple, especially if you're in a tier 3 college where exams might not be very tough. Most college subjects overlap with the GATE syllabus, so GATE preparation directly helps with college studies. Here's how to save time and manage both effectively:

### Key Points to Save Time
- **Stop Wasting Time**: Avoid unproductive activities like unnecessary socializing or bunking classes.
- **Complete College Work in College**: Finish assignments and study during college hours to free up time for GATE prep later.
- **Avoid Extra Burden**: Don’t take on additional responsibilities that can add stress.
- **Skip Unnecessary Lectures**: If possible, skip lectures that don't add value to your GATE preparation or college understanding.

### Additional Tips
- **Set a Consistent Routine**: Establish a daily study schedule that balances both college work and GATE prep.
- **Use Technology**: Utilize online resources and apps for efficient GATE study.
- **Prioritize Important Tasks**: Focus on high-yield topics crucial for both college exams and GATE.
- **Balanced Lifestyle**: Include relaxation and leisure activities to avoid burnout.

By following these strategies, you can effectively manage your time and excel in both college studies and GATE preparation. Stay organized, focused, and consistent.
''')

        with st.expander("Q8. If I want to take coaching, which coaching institute should I choose for the GATE exam?"): #9
            with st.chat_message('user'):
                st.write('''From my point of view, the source or coaching institute doesn't matter as much as some might think. You can choose any coaching institute you prefer, but consider several factors before making your decision:
                            \n1. Ensure the teachers are knowledgeable and approachable.
                            \n2. Check if they have a good doubt-solving team.
                            \n3. Verify that they provide quality Daily Practice Problem Sheets (DPPS).
                            \n4. Don't select a coaching institute just because it's famous for producing top rankers. Evaluate it for yourself by watching their demo lectures and making an informed decision based on your personal assessment.
                            \nRemember, the best coaching institute is the one that meets your specific learning needs and preferences.''')

        with st.expander("Q9. There are only 8-9 months left until the GATE exam. Can I still crack it?"): #10
            with st.chat_message("ai"):
                st.write('''Yes, you can still crack the GATE CSE exam with 8-9 months of preparation if you use your time wisely. Here are some tips:
1. **Create a Study Plan**: Break the syllabus into sections and allocate specific times for each subject. Stick to this schedule.
2. **Focus on Key Subjects**: 
   - Start with important subjects like Data Structures, Algorithms, Operating Systems, Computer Networks, and Databases.
   - Group related subjects (like C - Data Structures - Algorithms, DE - COA - OS) and study them in order.
3. **Daily Practice**: Practice math and aptitude every day since they are crucial for the exam.
4. **Use Good Resources**: Refer to standard textbooks and online resources. Use free platforms like YouTube for better understanding.
5. **Regular Revision**: Revise regularly to keep concepts fresh. Make concise notes for quick revision.
6. **Mock Tests and Previous Papers**: Start solving mock tests and previous years’ papers after covering a good portion of the syllabus. Analyze your performance and improve weak areas.
7. **Stay Consistent and Motivated**: Study regularly without long breaks. Set small goals and celebrate your achievements to stay motivated.

By following these tips and staying focused, you can make the most of your preparation time and perform well in the GATE CSE exam.
''')
        with st.expander("Q10. How many hours should I study daily for the GATE exam?"): #11

            with st.chat_message(name='user'):
                st.write("The number of hours you study each day is not fixed, and it is not accurate to say that studying for 8 hours a day guarantees a good rank, or that studying for only 4 hours a day means you won't achieve a high rank. The most important factor is consistency. You should maintain a steady study routine throughout your journey. Focus on maximizing the number of topics you cover daily and the number of questions you solve. Measure your preparation not by the time spent, but by the progress you make in terms of topics understood and problems solved each day.")

        with st.expander("Q11. How should I approach solving previous years' GATE questions?"): #13

            with st.chat_message("user"):
                st.write('''before you start solving previous year questions, make sure to study the topic well. Then move on to practicing questions. First, try to understand what the problem is actually asking. If you can figure out the "what" in the question, you've solved 90% of the problem. Then, use your technique to find the answer. Always solve the problem step by step; don't try to solve it directly. Also, try to create shortcuts while solving questions, as these will help you later.''')
        with st.expander("Q12. How can I prepare for the GATE exam while working a job?"): #14
            with st.chat_message("user"):
                st.write("Preparing for the GATE exam while working a job requires determination, focus, and smart time management. Start by creating a study plan that fits around your work schedule, allocating dedicated time each day for studying. While it may seem daunting to balance work and study, remember that consistency is key. Even if you can only spare a couple of hours each day, make those hours count by staying focused and disciplined. Prioritize your study topics wisely, focusing on high-weightage areas first to maximize your efforts. Additionally, utilize weekends and any free time effectively, dedicating longer study sessions to cover more complex topics or to revise thoroughly. It's important to stay motivated throughout your preparation journey. Remind yourself of your goals and the reasons why you're pursuing this path. Celebrate small victories along the way, whether it's mastering a difficult concept or scoring well in a mock test. Surround yourself with supportive peers or join study groups where you can share experiences and learn from each other. Most importantly, believe in yourself and your ability to succeed. With dedication, perseverance, and a positive mindset, you can overcome the challenges of balancing work and GATE preparation, and achieve your goals.")
        with st.expander("Q13. What is the importance of short notes in GATE preparation, and how are they useful?"): #15
            with st.chat_message("user"):
                st.write('''Short notes are extremely important for GATE preparation. Imagine you have studied all the subjects and revised them as well. To quickly review everything, you will need short notes. When we are revising a few days before the GATE exam, it becomes difficult to go through long notes. That’s why we use short notes.

Now, the question is how to make short notes. Short notes should always be concise and to the point, and they should cover fewer pages. Showcase all your art and skill in making these short notes. Create your short notes after completing a subject and during your first revision.
''')
        with st.expander("Q14. I am unable to solve problems even though I understand the topics. What should I do? I feel frustrated."): #16
            with st.chat_message("user"):
                st.write('''If you find that you can't solve questions even though you understand the topics during lectures—where everything seems clear but you still struggle with solving questions—then here's a strategy that might help. Initially, when you start solving questions, look at the solutions for the first 10-20 questions. Learn how to approach the questions from these solutions. Then, classify your mistakes into categories such as: 

1. You couldn't solve the question because you hadn't revised properly.
2. You made a silly mistake.
3. You didn't understand the approach, which is why you couldn't solve the question.

Work on the specific problem that prevented you from solving each question. Consistent practice will improve your problem-solving skills and deepen your understanding. Over time, you'll develop the ability to tackle questions independently and confidently. Remember, **practice is the key**.
''')
        with st.expander("Q15. Which test series should I buy for the GATE exam?"): #18
            with st.chat_message(name='user'):
                st.write("Test series play a vital role in GATE preparation, and they should be chosen wisely. The test series should have very few errors and contain exam-oriented questions that are not too hard or too easy. My personal suggestion (not a paid promotion) is to buy test series from Go Classes or Unacademy.")
        with st.expander("Q16. Do I need to read from standard textbooks?"): #19
            with st.chat_message("user"):
                st.write("Standard books are highly beneficial, especially if you have ample time for preparation. However, if time is limited, it's advisable to avoid solely relying on standard books. Instead, focus on targeted resources that cover key concepts efficiently. For topics where clarification is needed or doubts arise, referring to standard books can be invaluable. It's about striking a balance and utilizing standard books judiciously, primarily for cross-verification and clarification purposes.")
        with st.expander("Q17. Are there any other resources you would suggest for GATE preparation?"): #20
            with st.chat_message("user"):
                st.write('''When it comes to GATE preparation, leveraging the right resources can make all the difference. Two invaluable resources that every aspirant should consider are Wikipedia and ChatGPT. These platforms offer unique benefits and can significantly enhance the effectiveness of your study regimen. Consider the following:
    
                        \nWikipedia:
                            Provides comprehensive explanations and insights into various subjects covered in the GATE syllabus.
                            Offers a vast array of articles that delve deep into complex topics, aiding in a thorough understanding of concepts.
                            Serves as a valuable supplementary resource for clarifying doubts and gaining additional insights.
                            Its open-editing model ensures that information remains up-to-date, reflecting the latest developments in different fields.
    
                        \nChatGPT:
                            Acts as a personalized tutor, offering assistance and guidance tailored to individual learning needs.
                            Utilizes its conversational capabilities and vast knowledge base to provide interactive support.
                            Clarifies doubts, offers additional explanations, and suggests relevant resources through engaging conversations.
                            Complements traditional study methods by providing dynamic and accessible assistance.
                        \nThese resources, when used effectively, empower GATE aspirants with the tools and knowledge necessary to excel in their preparation journey. By integrating Wikipedia and ChatGPT into your study routine, you can enhance your understanding, clarify doubts, and ultimately achieve success in the GATE exam.''')
        with st.expander("Q18. I am in the first year of college. How can I start preparing for the GATE exam?"): #21
            with st.chat_message("user"):
                st.write("If you're a first-year student, focus more on your college subjects than on preparing for the Gate exam. It's essential to enhance your coding skills from the beginning. Start by mastering math and aptitude so that later on, things become much easier. Remember, college subjects are what you'll primarily encounter in the Gate exam, so make sure to study them well during your college years. Additionally, start preparing for the Gate exam from the fourth semester onwards.")
        with st.expander("Q19. My college placements are happening, and I am scared. How should I balance preparing for the GATE exam?"): #22
            with st.chat_message("user"):
                st.write("Absolutely! If you're fully committed to cracking the GATE exam and willing to give it your all, my personal suggestion is to go for it wholeheartedly. Taking calculated risks and being prepared to face challenges head-on are essential qualities for success in such endeavors. However, it's crucial to manage your time effectively, as balancing preparation with other commitments can be demanding. Make a detailed study plan, allocating sufficient time for study sessions, practice tests, and revision. Additionally, stay motivated and maintain a positive mindset throughout your preparation journey. Remember, success often requires stepping out of your comfort zone and embracing new challenges. With determination, perseverance, and effective time management, you can maximize your chances of cracking the GATE exam and achieving your goals.")

    # here all the questions end

    # section for any doubt then person can ask :)
    # if 'submitted' not in st.session_state:
    #     st.session_state.submitted = False


    # with st.container():
    #     st.write("---")
    #     st.header("Still doubt left ... Ask your Question")
    #     st.warning("Please avoid asking unnecessary questions that have already been answered above or that can be resolved with a bit of common sense.")

        # with st.form(key='contact_form'):
        #     col1,col2 = st.columns(2)
        #     with col1:
        #         name = st.text_input("Name")
        #     with col2:
        #         email = st.text_input("Email")
        #     message = st.text_area("Message")
        #
        #     submit_button = st.form_submit_button(label='Submit')
        #
        #     if submit_button and not st.session_state.submitted:
        #         st.session_state.submitted = True
        #         # Simulate a processing delay with an animation
        #         with st.spinner('Processing...'):
        #             time.sleep(10)  # Simulate a processing time
        #         st.session_state.submitted = False
        #
        #     # Show success message
        #         st.success("Your message has been sent successfully!")
        # # Every form must have a submit button.
        # # submitted = st.form_submit_button("Submit")
        #
        #     # if submitted:
        #     #     st.write("slider", slider_val, "checkbox", checkbox_val)

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        # contact_form = """
        # <form action="https://formspree.io/f/xoqgbppn" method="POST">
        #     <input type="hidden" name="_captcha" value="false">
        #     <input type="text" name="name" placeholder="Your name" required>
        #     <input type="email" name="email" placeholder="Your email" required>
        #     <textarea name="message" placeholder="Your message here" required></textarea>
        #     <button type="submit">Send</button>
        # </form>
        # """
        # st.markdown(contact_form, unsafe_allow_html=True)


    #footer
    st.divider()
    st.markdown("<h4 style = 'text-align:center'>Made with 💝 By Dipanshu Garg</h4>",unsafe_allow_html=True)
    st.markdown("<h6 style = 'text-align:center'>Follow me on Linkedin  </h6>",unsafe_allow_html=True)
    st.text("")
    # making some social media buttons :)
    st.markdown("""
        <div style="display: flex; justify-content: center;">
        <div>
            <a href='https://www.linkedin.com/in/dipanshu-garg24'><img src='https://img.icons8.com/fluent/48/000000/linkedin.png' width='30'></a>
        </div>
    </div>
    
        """, unsafe_allow_html=True)

