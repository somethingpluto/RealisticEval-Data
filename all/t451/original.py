from PIL import Image


def convert_image_to_bits(image_path):
    # partly generated with chatgpt :skull:
    image = Image.open(image_path)
    image = image.convert('1')

    pixel_data = image.load()

    w, h = image.size

    bits_array = []

    for y in range(h):
        for x in range(w):
            pixel = pixel_data[x, y]
            bit = 1 if pixel == 255 else 0
            bits_array.append(bit)

    return bits_array
