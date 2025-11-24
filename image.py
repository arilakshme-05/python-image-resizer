import os
from PIL import Image,ImageDraw
input_folder="input_images"
output_folder="resized_images"
new_width=800
new_height=600
output_format="JPEG"
num_samples=5
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
for i in range(1,num_samples+1):
    img=Image.new("RGB",(500+i*50,400+i*50),(100+i*20,150+i*15,200+i*10))
    d=ImageDraw.Draw(img)
    d.text((10,10),f"Sample{i}",fill=(255,255,255))
    img.save(os.path.join(input_folder,f"sample{i}.png"))
print(f"{num_samples} sample images created in '{input_folder}'")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
def resize_image(img,max_width,max_height):
    original_width,original_height=img.size
    ratio=min(max_width/original_width,max_height/original_height)
    new_size=(int(original_width*ratio),int(original_height*ratio))
    return img.resize(new_size,resample=Image.Resampling.LANCZOS)
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png",".jpg",".jpeg",".bmp",".gif")):
        input_path=os.path.join(input_folder,filename)
        output_path=os.path.join(output_folder,os.path.splitext(filename)[0]+"."+output_format.lower())
        with Image.open(input_path) as img:
            resized_img=resize_image(img,new_width,new_height)
            resized_img.save(output_path,output_format)
        print(f"Processed {filename} -> {output_path}")
print("All images resized successfully!")

