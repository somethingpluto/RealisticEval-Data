from PIL import Image


def convert_image_to_bits(image_path):
    """
    Converts an image to a binary representation.

    Args:
        image_path (str): The file path of the image to convert.

    Returns:
        list: A list of bits representing the image, where 1 is for white pixels
              and 0 is for black pixels.
    """
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
