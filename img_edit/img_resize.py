from PIL import Image


def resize_half(image_source):
    with Image.open(image_source) as img:
        print(img)
        height, width = img.size
        img = img.resize((int(height / 2), int(width / 2)))
        print(img)
        img.show()
        return img


def main():
    path = "./demo.jpg"
    pic = resize_half(image_source=path)
    pic.save("demo_resized.jpg")


if __name__ == "__main__":
    main()
