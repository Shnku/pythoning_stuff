from operator import index, indexOf
from PIL import Image, ImageOps
from img_resize import resize_half
from print_canvas_size import create_a4_canvas


def create_grid(photo, no):
    photo = ImageOps.expand(photo, 10, "white")
    print(photo)
    list_of_pics = [photo for _ in range(no)]
    a4_size = create_a4_canvas(ppi=300)
    canvas = Image.new("RGB", size=a4_size, color="white")

    pos_x, pos_y = 0, 0
    for pic in list_of_pics:
        canvas.paste(pic, (int(pos_x), int(pos_y)))
        pos_x += photo.width
        if pos_x + photo.width >= a4_size[0]:
            pos_x, pos_y = 0, pos_y + photo.height
            if pos_y + photo.height >= a4_size[1]:
                print("less printed as page overflow")
                break

    canvas.show()
    return canvas


def main():
    with Image.open("./demo_resized.jpg") as photo:
        photo = resize_half(photo)
        # photo.show()
        print(photo)
        grid = create_grid(photo, no=30)
        grid.save("demo_grid_a4.jpg")


if __name__ == "__main__":
    main()
