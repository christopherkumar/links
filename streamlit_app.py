# Section 1: Imports
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image, ImageDraw

# Section 2: Initial Setup
load_css()

# Section 3: Display Picture
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
st.image(result)

# Section 4: Name and Header
st.header('Christopher Vishnu Kumar')

# Section 5: Social Links with Custom Buttons
# Define URLs and links
img_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
    "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",
    "https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg",
]
links = [
    "https://www.linkedin.com/in/christopher-kumar-26b5792b1/",
    "https://github.com/christopherkumar",
    "https://www.instagram.com/christopherkumar812/",
]
# Custom CSS and Markdown for displaying buttons
st.markdown(f"""
<div class="centered-buttons">
    <a href="{links[0]}" target="_blank"><img src="{img_urls[0]}" /></a>
    <a href="{links[1]}" target="_blank"><img src="{img_urls[1]}" /></a>
    <a href="{links[2]}" target="_blank"><img src="{img_urls[2]}" /></a>
</div>
""", unsafe_allow_html=True)

# Section 6: Experience and Education
st.markdown("""
<div class="centered-text-with-bg">
    Intern at Cogninet AI
    <br>
    Bachelor of Engineering (Honours) - Computer Systems Engineering
    <br>
    University of the South Pacific - Foundation Science Programme
</div>
""", unsafe_allow_html=True)

# Additional Setup (if any)
icon_size = 20
