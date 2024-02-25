from PIL import Image

def change_image_background(image_path, output_path, new_color=(255, 255, 255)):
    with Image.open(image_path) as im:
        im = im.convert("RGBA")

        # Create a new background image with the specified color
        background = Image.new("RGB", im.size, new_color)
        
        # Paste the image on top of the background
        im = Image.alpha_composite(background, im)

        # Save the result
        im.convert("RGB").save(output_path, "PNG")
