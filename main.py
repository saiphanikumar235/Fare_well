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
st.write("""JDF has been my employer for the past two years. The experience was exceptional and involved a lot of exciting work and learning.\n\nAs I prepare to embark on a new chapter in my career journey, I wanted to take a moment to express my deepest gratitude to each and every one of you.\n\nIt has been an absolute privilege to work with such an incredible team.\n\nThe time I spent here has been truly memorable and rewarding because of the support, camaraderie, and shared experiences.\n\nThe opportunities I've had to learn, grow, and contribute within this amazing company have given me a great deal of gratitude.\n\nMy future endeavors will be shaped by the knowledge and experiences I have gained here.\n\nI am optimistic that we will come across each other soon..\n""", )
time.sleep(5)
st.toast("saiphanikumar2000@gmail.com", icon='📧')
st.toast("https://www.linkedin.com/in/saiphani-kumar-b33431177/")
c = st.container()
c.text("Please feel free to connect with me over email-saiphanikumar2000@gmail.com \n\t\t\tor\nvia linkedin - https://www.linkedin.com/in/saiphani-kumar-b33431177/")
