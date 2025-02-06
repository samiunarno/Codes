import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os

def enhance_image(input_image_path, output_image_path, resolution_scale=2):
    # Load the image
    img = cv2.imread(input_image_path)

    if img is None:
        print(f"Error: Unable to load image at {input_image_path}")
        return

    # Get original dimensions
    height, width = img.shape[:2]
    print(f"Original dimensions: Width = {width}, Height = {height}")
    
    # Increase the resolution by scaling the image (resize)
    new_dim = (int(width * resolution_scale), int(height * resolution_scale))
    img_resized = cv2.resize(img, new_dim, interpolation=cv2.INTER_CUBIC)  # INTER_CUBIC for high-quality scaling

    # Convert to RGB (OpenCV uses BGR by default)
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

    # Enhance lighting and contrast
    pil_img = Image.fromarray(img_rgb)

    # Auto adjust brightness, contrast, and sharpness
    enhancer = ImageEnhance.Brightness(pil_img)
    pil_img = enhancer.enhance(1.2)  # Increase brightness by 20%

    enhancer = ImageEnhance.Contrast(pil_img)
    pil_img = enhancer.enhance(1.3)  # Increase contrast by 30%

    enhancer = ImageEnhance.Sharpness(pil_img)
    pil_img = enhancer.enhance(2.0)  # Sharpen the image by a factor of 2

    # Check if the output path has an extension, and if not, add the default one
    if not os.path.splitext(output_image_path)[1]:
        output_image_path += '.jpg'  # default to jpg if no extension is provided

    # Save the enhanced image to the output path
    pil_img.save(output_image_path)

    print(f"Enhanced image saved as: {output_image_path}")

# Get paths from user input
input_path = input("Enter the path of the input image: ")  # User provides input image path
output_path = input("Enter the path for the enhanced image: ")  # User provides output image path

# Get resolution scale from user input (e.g., 2 for doubling the resolution)
resolution_scale = float(input("Enter the resolution scale (e.g., 2 for double size, 1.5 for 1.5x size): "))

# Call the function
enhance_image(input_path, output_path, resolution_scale)
