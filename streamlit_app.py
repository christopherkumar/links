import streamlit as st
from st_functions import st_button, load_css
from PIL import Image, ImageDraw

load_css()

#<editor-fold desc="Display Picture">
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
#</editor-fold>
#<editor-fold desc="Bio">
st.header('Christopher Vishnu Kumar', anchor=None)

# Using Markdown to center text and add a line underneath
st.markdown("""
<style>
.centered-text {
    text-align: center;
}
</style>
<div class="centered-text">
    Bachelor of Engineering (Honours) - Computer Systems Engineering
    <br>
    <hr style="margin-top: 10px; margin-bottom: 10px;">
    University of the South Pacific - Foundation Science Programme
</div>
""", unsafe_allow_html=True)
#</editor-fold>

icon_size = 20

#<editor-fold desc="Buttons">
# st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
# st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
# st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
# st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
# st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', icon_size)
# st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
#</editor-fold>
