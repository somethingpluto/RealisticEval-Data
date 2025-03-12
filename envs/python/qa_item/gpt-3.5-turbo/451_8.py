from PIL import Image

def convert_image_to_bits(image_path: str):
    img = Image.open(image_path)
    img = img.convert('L')
    img_data = list(img.getdata())
    bits = [1 if pixel == 255 else 0 for pixel in img_data]
    
    return bits
import os
import unittest

from PIL import Image


class TestConvertImageToBits(unittest.TestCase):

    def setUp(self):
        """Create test images before each test."""
        # Create a white image (all pixels white)
        self.white_image_path = 'white_image.bmp'
        white_image = Image.new('1', (2, 2), color=1)  # 1 is for white
        white_image.save(self.white_image_path)

        # Create a black image (all pixels black)
        self.black_image_path = 'black_image.bmp'
        black_image = Image.new('1', (2, 2), color=0)  # 0 is for black
        black_image.save(self.black_image_path)

        # Create a mixed image (half white, half black)
        self.mixed_image_path = 'mixed_image.bmp'
        mixed_image = Image.new('1', (2, 2))
        mixed_image.putpixel((0, 0), 1)  # White
        mixed_image.putpixel((0, 1), 0)  # Black
        mixed_image.putpixel((1, 0), 0)  # Black
        mixed_image.putpixel((1, 1), 1)  # White
        mixed_image.save(self.mixed_image_path)

    def tearDown(self):
        """Remove the test images after each test."""
        os.remove(self.white_image_path)
        os.remove(self.black_image_path)
        os.remove(self.mixed_image_path)

    def test_white_image(self):
        """Test converting a white image."""
        expected_output = [1, 1, 1, 1]  # All pixels should be 1 (white)
        result = convert_image_to_bits(self.white_image_path)
        self.assertEqual(result, expected_output)

    def test_black_image(self):
        """Test converting a black image."""
        expected_output = [0, 0, 0, 0]  # All pixels should be 0 (black)
        result = convert_image_to_bits(self.black_image_path)
        self.assertEqual(result, expected_output)

    def test_mixed_image(self):
        """Test converting a mixed image."""
        expected_output = [1, 0, 0, 1]  # 1 white, 3 black
        result = convert_image_to_bits(self.mixed_image_path)
        self.assertEqual(result, expected_output)

    def test_invalid_image_path(self):
        """Test converting an invalid image path."""
        with self.assertRaises(FileNotFoundError):
            convert_image_to_bits('invalid_image_path.bmp')

    def test_large_image(self):
        """Test converting a larger image."""
        # Create a larger image (3x3)
        large_image_path = 'large_image.bmp'
        large_image = Image.new('1', (3, 3))
        large_image.putpixel((0, 0), 1)
        large_image.putpixel((1, 1), 1)
        large_image.putpixel((2, 2), 1)
        large_image.save(large_image_path)

        expected_output = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 1
        ]
        result = convert_image_to_bits(large_image_path)
        self.assertEqual(result, expected_output)

        # Clean up
        os.remove(large_image_path)

if __name__ == '__main__':
    unittest.main()