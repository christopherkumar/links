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
    # Load and process the image
    img = Image.open('dp.png').convert("RGBA")
    size = min(img.size)
    left = (img.size[0] - size) / 2
    top = (img.size[1] - size) / 2
    right = (img.size[0] + size) / 2
    bottom = (img.size[1] + size) / 2
    img = img.crop((left, top, right, bottom))
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=255)
    img = img.resize((200, 200))
    result = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    st.image(result, caption=None)

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
    <div class="centered-text-with-bg">
        Intern at Cogninet AI
        <br>
        Bachelor of Engineering (Honours) - Computer Systems Engineering
        <br>
        University of the South Pacific - Foundation Science Programme
    </div>
    """, unsafe_allow_html=True)
