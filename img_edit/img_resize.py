from PIL import Image


def resize_half(img):
    print(img)
    height, width = img.size
    img = img.resize((int(height / 2), int(width / 2)))
    print(img)
    return img


def main():
    path = "./demo.jpg"
    with Image.open(path) as pic:
        pic = resize_half(pic)
        pic.save("demo_resized.jpg")


if __name__ == "__main__":
    main()
