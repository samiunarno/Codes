from PIL import Image, ImageOps
import os


input_folder = r"C:\Users\SMT\Downloads\Resiz" #input Folder 
output_folder = r"C:\Users\SMT\Downloads\Resiz_Output" #output Folder


resize_width = 600  
resize_height = 400  
border_size = 100 
border_color = "white"  


os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
           
            img_resized = img.resize((resize_width, resize_height))

            
            img_with_border = ImageOps.expand(img_resized, border=border_size, fill=border_color)

           
            output_path = os.path.join(output_folder, filename)
            img_with_border.save(output_path)
            print(f"{filename} Successfully Complete")

print("Success" "By Arno")
print("Push Before Pull ")
