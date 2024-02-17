import streamlit as st
from st_functions import st_button, load_css
from PIL import Image, ImageDraw

load_css()

col1, col2, col3 = st.columns(3)
# Load the image
img = Image.open('dp.png').convert("RGBA")

# Ensure the image is square
size = min(img.size)
left = (img.size[0] - size) / 2
top = (img.size[1] - size) / 2
right = (img.size[0] + size) / 2
bottom = (img.size[1] + size) / 2
img = img.crop((left, top, right, bottom))

# Create a circular mask to apply
mask = Image.new('L', img.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + img.size, fill=255)

# Apply mask to the image, keeping transparency
result = Image.new('RGBA', img.size, (0, 0, 0, 0))
result.paste(img, (0, 0), mask)

# Display the circular image
col2.image(result, use_column_width=True)

st.markdown('<style>h1{margin-top: 0px; margin-bottom: 0px;}</style>', unsafe_allow_html=True)
st.header('Christopher Vishnu Kumar', anchor=None)

# Custom CSS to center the buttons and add spacing
st.markdown("""
<style>
.centered-buttons {
    display: flex;
    justify-content: center;
    gap: 5px;
}
.centered-buttons a {
    display: inline-block; /* Allows the gap to take effect */
}
.centered-buttons img {
    border-radius: 50%; /* Makes the images circular */
    width: 40px; /* Sets the image size, adjust as needed */
    height: 40px; /* Sets the image size, adjust as needed */
}
</style>
""", unsafe_allow_html=True)

# Placeholder URLs for the images
img_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",  # LinkedIn
    "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",  # GitHub
    "https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg",  # Instagram
]

# Links associated with each button
links = [
    "https://www.linkedin.com/in/christopher-kumar-26b5792b1/",
    "https://github.com/christopherkumar",
    "https://www.instagram.com/christopherkumar812/",
]

# Using Markdown to create a centered container for the buttons
st.markdown(f"""
<div class="centered-buttons">
    <a href="{links[0]}" target="_blank"><img src="{img_urls[0]}" /></a>
    <a href="{links[1]}" target="_blank"><img src="{img_urls[1]}" /></a>
    <a href="{links[2]}" target="_blank"><img src="{img_urls[2]}" /></a>
</div>
""", unsafe_allow_html=True)

# Using Markdown to center text within a rectangle with rounded edges
st.markdown("""
<style>
.centered-text-with-bg {
    text-align: center;
    background-color: #f0f2f6;
    border-radius: 20px;
    padding: 20px;
    margin: 10px;
}
</style>
<div class="centered-text-with-bg">
    Intern at Cogninet AI
    <br>
    Bachelor of Engineering (Honours) - Computer Systems Engineering
    <br>
    University of the South Pacific - Foundation Science Programme
</div>
""", unsafe_allow_html=True)

icon_size = 20
