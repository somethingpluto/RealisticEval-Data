
def convert_png_to_ico(png_file_path, ico_file_path, icon_sizes=[(32, 32)]):
    # Create the ICO file
    ico_file = f"{ico_file_path}.ico"
    
    # Create the ICO file header
    ico_header = f"{ico_file_path}.ico\n\n"
    for i in range(16):
        ico_header += f"{i}\t{png_file_path}\t{png_file_path}\n\n"
    
    # Create the ICO file content
    for i in range(16):
        icon_size = icon_sizes[i]
        icon_data = f"{png_file_path}\t{icon_size}\t{png_file_path}\n"
        for j in range(16):
            icon_data += f"{i}\t{j}\t{icon_size}\t{png_file_path}\n\n"
    
    # Save the ICO file
    ico_file.write(ico_header)
    ico_file.write(f"{ico_file_path}.ico\n")
    ico_file.write(icon_data)
    
    return ico_file_path

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