import os
from PIL import Image

def convert_png_to_ico(png_file_path, ico_file_path, icon_sizes=[(32, 32)]):
    images = []
    for size in icon_sizes:
        images.append(Image.open(png_file_path).resize(size))

    images[0].save(ico_file_path, format="ICO", sizes=[(image.width, image.height) for image in images], save_all=True)
import unittest
from unittest.mock import patch, MagicMock


class TestConvertPngToIco(unittest.TestCase):
    @patch('PIL.Image.open')
    def test_single_icon_size(self, mock_open):
        mock_image = mock_open.return_value.__enter__.return_value
        convert_png_to_ico('source.png', 'output.ico', [(64, 64)])
        mock_image.save.assert_called_with('output.ico', format='ICO', sizes=[(64, 64)])

    @patch('PIL.Image.open')
    def test_multiple_icon_sizes(self, mock_open):
        mock_image = mock_open.return_value.__enter__.return_value
        convert_png_to_ico('source.png', 'output.ico', [(16, 16), (32, 32), (64, 64)])
        mock_image.save.assert_called_with('output.ico', format='ICO', sizes=[(16, 16), (32, 32), (64, 64)])

    @patch('PIL.Image.open')
    def test_default_icon_size(self, mock_open):
        mock_image = mock_open.return_value.__enter__.return_value
        convert_png_to_ico('source.png', 'output.ico')
        mock_image.save.assert_called_with('output.ico', format='ICO', sizes=[(32, 32)])

    @patch('PIL.Image.open')
    def test_file_handling(self, mock_open):
        mock_image = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_image
        convert_png_to_ico('source.png', 'output.ico')
        # Check if save was called correctly
        mock_image.save.assert_called_once_with('output.ico', format='ICO', sizes=[(32, 32)])

    @patch('PIL.Image.open')
    def test_invalid_image_path(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            convert_png_to_ico('invalid.png', 'output.ico')

if __name__ == '__main__':
    unittest.main()