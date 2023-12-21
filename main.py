import time
import streamlit as st

st.set_page_config(page_title='Farewell', page_icon='👋🏽', layout='wide')
with st.spinner('Wait for it...'):
    time.sleep(5)
st.snow()
time.sleep(7)
st.markdown("<h1 style='text-align: left; color: red;'>Sai's Farewell</h1>", unsafe_allow_html=True)
st.toast("saiphanikumar2000@gmail.com", icon='📧')
st.toast("https://www.linkedin.com/in/saiphani-kumar-b33431177/")
st.write(
    """As I prepare to embark on a new chapter in my career journey, I wanted to take a moment to express my deepest gratitude to each and every one of you.
            
            
Working alongside such an incredible team has been an absolute privilege. The support, camaraderie, and shared experiences have made my time here truly memorable and rewarding.


            
I am profoundly grateful for the opportunities I've had to learn, grow, and contribute within this amazing company. The knowledge and experiences gained here will undoubtedly shape my future endeavors.\n
            """,)
time.sleep(5)
st.toast("saiphanikumar2000@gmail.com", icon='📧')
st.toast("https://www.linkedin.com/in/saiphani-kumar-b33431177/")
c = st.container()
c.text("https://www.linkedin.com/in/saiphani-kumar-b33431177/")
