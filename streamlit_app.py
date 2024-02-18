import streamlit as st
from st_functions import st_button, load_css
from PIL import Image, ImageDraw

# Global CSS to add padding to all containers
st.markdown("""
<style>
/* Targeting all Streamlit containers to have 10px padding */
.stMarkdown, .stImage, .stHeader, .stButton {
    padding: 10px !important;
}
/* Additional styles for custom elements */
.centered-buttons {
    display: flex;
    justify-content: center;
    gap: 5px;
}
.centered-buttons a {
    display: inline-block;
}
.centered-buttons img {
    border-radius: 50%;
    width: 40px;
    height: 40px;
}
.centered-text-with-bg {
    text-align: center;
    background-color: #f0f2f6;
    border-radius: 20px;
    padding: 20px;
    margin: 10px 0; /* Adjusted to only apply margin vertically */
}
</style>
""", unsafe_allow_html=True)

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
.bio-with-rounded-corners {
    text-align: center;
    background-color: #f0f2f6; /* Light grey background */
    border-radius: 20px; /* Rounded corners */
    padding: 20px; /* Inner spacing */
    margin: 10px 0; /* Vertical spacing outside */
    box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Optional: adds a subtle shadow for depth */
}
with st.container():
    st.markdown("""
    <div class="centered-text-with-bg">
        Intern at Cogninet AI
        <br>
        Bachelor of Engineering (Honours) - Computer Systems Engineering
        <br>
        University of the South Pacific - Foundation Science Programme
    </div>
    """, unsafe_allow_html=True)
