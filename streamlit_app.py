import streamlit as st
from st_functions import st_button, load_css
from PIL import Image, ImageDraw

# CSS Load
with st.container():
    load_css()

# Display Picture
with st.container():
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
    mask = Image.new('L', (200, 200), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 200, 200), fill=255)

    # Resize the cropped image to 200x200 pixels without antialiasing
    img = img.resize((200, 200))

    # Apply mask to the resized image, keeping transparency
    result = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)

    # Display the circular image centered
    st.image(result, caption=None)

# Name
with st.container():
    st.header('Christopher Vishnu Kumar', anchor=None)

# Socials -> Buttons
with st.container():
    # Custom CSS to center the buttons and add spacing
    st.markdown("""
    <style>
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
    </style>
    """, unsafe_allow_html=True)

    # Placeholder URLs for the images and associated links
    img_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",  # LinkedIn
        "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",  # GitHub
        "https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg",  # Instagram
    ]
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

# Experience/Education
with st.container():
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
