import base64
import imghdr

def is_base64_image(image_data: str) -> None:
    try:
        # Check if the provided image data is a valid Base64 encoded string
        if not base64.b64encode(base64.b64decode(image_data)) == image_data.encode():
            print("Provided image data is not a valid Base64 encoded image string.")
            return

        # Decode the Base64 image data and check if it is a valid image format
        decoded_image = base64.b64decode(image_data)
        image_format = imghdr.what(None, h=decoded_image)
        
        if image_format is None:
            print("Provided image data is not a valid image format.")
        else:
            print("Provided image data is a valid Base64 encoded image string.")
    except Exception as e:
        print("Error occurred while validating image data:", e)
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