import os
import unittest


class TestConvertPngToIco(unittest.TestCase):
    def test_valid_input(self):
        """Test converting a valid PNG file to ICO format with a standard icon size."""
        convert_png_to_ico('path/to/input.png', 'path/to/output.ico')
        self.assertTrue(os.path.exists('path/to/output.ico'))

    def test_multiple_sizes(self):
        """Test converting a PNG to ICO with multiple icon sizes."""
        sizes = [(16, 16), (32, 32), (64, 64), (128, 128), (256, 256)]
        convert_png_to_ico('path/to/input.png', 'path/to/output.ico', icon_sizes=sizes)
        with Image.open('path/to/output.ico') as img:
            self.assertEqual(len(img.info['sizes']), len(sizes))

    def test_nonexistent_input_file(self):
        """Test the function's response to a nonexistent input file."""
        with self.assertRaises(FileNotFoundError):
            convert_png_to_ico('nonexistent.png', 'path/to/output.ico')

    def test_invalid_icon_size(self):
        """Test passing an invalid icon size."""
        with self.assertRaises(ValueError):
            convert_png_to_ico('path/to/input.png', 'path/to/output.ico', icon_sizes=[(300, 300)])  # Assuming 300x300 is not supported

    def test_output_overwrite(self):
        """Test that the function overwrites an existing ICO file without error."""
        # Create an initial ICO file
        open('path/to/output.ico', 'a').close()
        convert_png_to_ico('path/to/input.png', 'path/to/output.ico')
        self.assertTrue(os.path.exists('path/to/output.ico'))
