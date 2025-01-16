from PIL import Image, ImageOps
import os

input_folder = r"F:\File\Path\Input" #input By Folder 
output_folder = r"F:\File\Redirect\Output"  # Output By Folder

border_size = '#' #change the border width 
border_color = "#"  #Border Colour

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    try:
        # Check for .jpg, .jpeg, .png, .webp extensions
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            img_path = os.path.join(input_folder, filename)

            with Image.open(img_path) as img:
                # Add border (no resizing)
                img_with_border = ImageOps.expand(img, border=border_size, fill=border_color)

                # Save the image with border in the output folder
                output_path = os.path.join(output_folder, filename)
                img_with_border.save(output_path)
                print(f"Your File Name : {filename} ")
                print("Successfully Completed")
        else:
            print(f"{filename} is not a valid image file.")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Embed By @rno")
print("Pull Before Push")
