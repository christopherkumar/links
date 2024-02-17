import streamlit as st
from st_functions import st_button, load_css
from PIL import Image, ImageDraw

load_css()

col1, col2, col3 = st.columns(3)
img = Image.open('dp.png')
# Ensure the image is square for the circular crop
size = min(img.size)
left = (img.size[0] - size) / 2
top = (img.size[1] - size) / 2
right = (img.size[0] + size) / 2
bottom = (img.size[1] + size) / 2
img = img.crop((left, top, right, bottom))
# Create a circular mask
mask = Image.new('L', img.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + img.size, fill=255)
# Apply the mask to the image
img.putalpha(mask)
# Convert to RGB (in case of PNGs with transparency)
img = img.convert("RGB")
# Display the circular image
col2.image(img, use_column_width=True)

st.header('Christopher Vishnu Kumar')

st.info('Bachelor of Engineering (Honours) - Computer Systems Engineering')

icon_size = 20

#st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
#st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
#st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
#st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
#st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', icon_size)
#st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
#st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
