import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

# CSS Load
with st.container():
    load_css()

# Display Picture
with st.container():
    st.image(Image.open('dp.png'))

# Name
with st.container():
    st.header('Christopher Vishnu Kumar', anchor=None)

# Socials -> Buttons
with st.container():
    img_urls = ["https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
                "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",
                "https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg"]
    links = ["https://www.linkedin.com/in/christopher-kumar-26b5792b1/",
             "https://github.com/christopherkumar",
             "https://www.instagram.com/christopherkumar812/"]
    st.markdown(f"""
    <div class="centered-buttons">
        <a href="{links[0]}" target="_blank"><img src="{img_urls[0]}" /></a>
        <a href="{links[1]}" target="_blank"><img src="{img_urls[1]}" /></a>
        <a href="{links[2]}" target="_blank"><img src="{img_urls[2]}" /></a>
    </div>
    """, unsafe_allow_html=True)

# Experience/Education
with st.container():
    st.markdown("""
    <div class="centered-text-with-bg text-black">
        Intern at Cogninet AI
        <br>
        Bachelor of Engineering (Honours) - Computer Systems Engineering
        <br>
        University of the South Pacific - Foundation Science Programme
    </div>
    """, unsafe_allow_html=True)
