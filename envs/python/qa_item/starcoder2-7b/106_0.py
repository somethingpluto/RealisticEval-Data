import base64
from PIL import Image
from io import BytesIO

def is_base64_image(image_data: str) -> bool:
    """
    Checks if the provided image data is a valid Base64 encoded image string.

    Args:
        image_data (str): The image data string to be validated.

    Returns:
        bool: True if the image data is a valid Base64 encoded image string, False otherwise.
    """
    try:
        # Try to decode the image data
        decoded_image = base64.b64decode(image_data)

        # Try to open the image with PIL
        image = Image.open(BytesIO(decoded_image))

        # If the image is opened successfully, it's a valid Base64 encoded image
        return True
    except (base64.binascii.Error, IOError, AttributeError, ImportError):
        # If any of the above exceptions are raised, the image data is not a valid Base64 encoded image
        return False
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