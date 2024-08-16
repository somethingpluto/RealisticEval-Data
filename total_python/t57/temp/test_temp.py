import unittest
from PIL import Image
import os
from io import BytesIO


class TestConvertPNGToICO(unittest.TestCase):

    def setUp(self):
        """Create a sample PNG image for testing."""
        self.png_file_path = 'test_image.png'
        self.ico_file_path = 'test_image.ico'
        # Create a small red PNG image for testing
        image = Image.new("RGBA", (100, 100), "red")
        image.save(self.png_file_path)

    def tearDown(self):
        """Remove files created during the test."""
        os.remove(self.png_file_path)
        if os.path.exists(self.ico_file_path):
            os.remove(self.ico_file_path)

    def test_valid_conversion(self):
        """Test converting a valid PNG file to an ICO file."""
        convert_png_to_ico(self.png_file_path, self.ico_file_path)
        # Check if ICO file was created
        self.assertTrue(os.path.exists(self.ico_file_path))

    def test_invalid_png_path(self):
        """Test behavior with a non-existing PNG file."""
        with self.assertRaises(FileNotFoundError):
            convert_png_to_ico('nonexistent.png', self.ico_file_path)

    def test_invalid_icon_sizes(self):
        """Test with invalid icon sizes."""
        with self.assertRaises(ValueError):
            convert_png_to_ico(self.png_file_path, self.ico_file_path,
                               icon_sizes=[(3000, 3000)])  # Unusually large size

    def test_zero_size_icon(self):
        """Test with zero size icon dimensions."""
        with self.assertRaises(ValueError):
            convert_png_to_ico(self.png_file_path, self.ico_file_path, icon_sizes=[(0, 0)])

    def test_multiple_icon_sizes(self):
        """Test conversion with multiple icon sizes."""
        icon_sizes = [(16, 16), (32, 32), (64, 64)]
        convert_png_to_ico(self.png_file_path, self.ico_file_path, icon_sizes=icon_sizes)
        # Check the file and possibly the size
        with open(self.ico_file_path, 'rb') as f:
            ico_image = Image.open(BytesIO(f.read()))
            self.assertEqual(len(ico_image.info['sizes']), len(icon_sizes))

from PIL import Image


def convert_png_to_ico(png_file_path, ico_file_path, icon_sizes=[(32, 32)]):
    """
    Convert a PNG image file to an ICO format file.

    Args:
    png_file_path (str): Path to the source PNG image file.
    ico_file_path (str): Path to save the ICO file.
    icon_sizes (list): List of tuples specifying the sizes to include in the ICO file.
    """
    # Open the image file using Pillow
    with Image.open(png_file_path) as img:
        # Convert the image to ICO and save it
        img.save(ico_file_path, format='ICO', sizes=icon_sizes)