import base64
import re

def is_base64_image(image_data: str) -> None:
    """
    Checks if the provided image data is a valid Base64 encoded image string.

    Args:
        image_data (str): The image data string to be validated.
    """
    # Regular expression to match a Base64 encoded image string
    base64_regex = re.compile(r'^data:image/(png|jpeg|jpg|gif|bmp);base64,')
    
    # Check if the image data matches the Base64 image pattern
    if not base64_regex.match(image_data):
        return False
    
    # Extract the Base64 encoded part of the string
    base64_data = image_data.split(',')[1]
    
    # Attempt to decode the Base64 string
    try:
        base64.b64decode(base64_data, validate=True)
    except Exception:
        return False
    
    return True
import unittest


class TestIsBase64Image(unittest.TestCase):

    def test_valid_png(self):
        valid_png = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA'
        self.assertTrue(is_base64_image(valid_png))

    def test_valid_jpeg(self):
        valid_jpeg = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAA'
        self.assertTrue(is_base64_image(valid_jpeg))

    def test_invalid_format(self):
        invalid_format = 'data:text/plain;base64,SGVsbG8gd29ybGQ='
        self.assertFalse(is_base64_image(invalid_format))

    def test_invalid_base64_characters(self):
        invalid_base64 = 'data:image/png;base64,invalidBase64String@#%'
        self.assertFalse(is_base64_image(invalid_base64))

    def test_empty_string(self):
        self.assertFalse(is_base64_image(''))

if __name__ == '__main__':
    unittest.main()