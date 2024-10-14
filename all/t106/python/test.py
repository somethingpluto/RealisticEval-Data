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
