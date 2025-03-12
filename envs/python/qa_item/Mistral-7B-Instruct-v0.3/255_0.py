from PIL import Image
from typing import List

def convert_image_to_bits(image_path: str) -> List[int]:
    """
    Convert a picture to an array of binary bits.

    Args:
        image_path (str): The path to the image file.

    Returns:
        list: A list of bits (0 or 1) representing the image.
    """
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to grayscale
    img = img.convert('L')

    # Initialize an empty list to store the binary bits
    bits = []

    # Iterate over each pixel in the image
    for pixel in img.getdata():
        # Convert the grayscale value to binary (0 or 1)
        bit = int(str(pixel)[-1])
        bits.append(bit)

    return bits
import unittest
from io import BytesIO
from PIL import Image



class TestConvertImageToBits(unittest.TestCase):

    def create_image(self, mode, size, color):
        """
        Helper method to create an in-memory image.

        Args:
            mode (str): The color mode of the image (e.g., '1' for binary, 'L' for grayscale).
            size (tuple): A tuple of the image size (width, height).
            color (int or tuple): The color to fill the image. 255 for white, 0 for black in '1' mode.

        Returns:
            Image: A PIL Image object.
        """
        image = Image.new(mode, size, color)
        return image

    def test_all_white_image(self):
        image = self.create_image('1', (4, 4), 255)
        expected_bits = [1] * 16
        with BytesIO() as img_bytes:
            image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            result = convert_image_to_bits(img_bytes)
        self.assertEqual(result, expected_bits)

    def test_all_black_image(self):
        image = self.create_image('1', (4, 4), 0)
        expected_bits = [0] * 16
        with BytesIO() as img_bytes:
            image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            result = convert_image_to_bits(img_bytes)
        self.assertEqual(result, expected_bits)

    def test_checkerboard_image(self):
        image = self.create_image('1', (4, 4), 0)
        pixels = image.load()
        for y in range(4):
            for x in range(4):
                if (x + y) % 2 == 0:
                    pixels[x, y] = 255
        expected_bits = [1, 0, 1, 0,
                         0, 1, 0, 1,
                         1, 0, 1, 0,
                         0, 1, 0, 1]
        with BytesIO() as img_bytes:
            image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            result = convert_image_to_bits(img_bytes)
        self.assertEqual(result, expected_bits)

    def test_horizontal_stripes_image(self):
        image = self.create_image('1', (4, 4), 0)
        pixels = image.load()
        for y in range(4):
            for x in range(4):
                if y % 2 == 0:
                    pixels[x, y] = 255
        expected_bits = [1, 1, 1, 1,
                         0, 0, 0, 0,
                         1, 1, 1, 1,
                         0, 0, 0, 0]
        with BytesIO() as img_bytes:
            image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            result = convert_image_to_bits(img_bytes)
        self.assertEqual(result, expected_bits)

    def test_vertical_stripes_image(self):
        image = self.create_image('1', (4, 4), 0)
        pixels = image.load()
        for y in range(4):
            for x in range(4):
                if x % 2 == 0:
                    pixels[x, y] = 255
        expected_bits = [1, 0, 1, 0,
                         1, 0, 1, 0,
                         1, 0, 1, 0,
                         1, 0, 1, 0]
        with BytesIO() as img_bytes:
            image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            result = convert_image_to_bits(img_bytes)
        self.assertEqual(result, expected_bits)
if __name__ == '__main__':
    unittest.main()