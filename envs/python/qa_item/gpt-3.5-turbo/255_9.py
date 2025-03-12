from typing import List
from PIL import Image

def convert_image_to_bits(image_path: str) -> List:
    image = Image.open(image_path)
    image = image.convert("L")  # Convert image to black and white mode
    
    pixel_data = list(image.getdata())
    bits = [1 if pixel == 255 else 0 for pixel in pixel_data]  # Convert white pixel to 1, black pixel to 0
    
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