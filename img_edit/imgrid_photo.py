from PIL import Image, ImageOps
from img_resize import resize_half


with Image.open("demo.jpg") as photo:
    photo.show()

print(photo)
