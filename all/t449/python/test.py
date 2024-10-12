class TestBase64Encoding(unittest.TestCase):

    def test_convert_simple_string_to_base64(self):
        self.assertEqual(convert_to_base64("Hello, World!"), "SGVsbG8sIFdvcmxkIQ==")

    def test_convert_empty_string_to_base64(self):
        self.assertEqual(convert_to_base64(""), "")

    def test_convert_string_with_spaces_to_base64(self):
        self.assertEqual(convert_to_base64("Test String with Spaces"), "VGVzdCBTdHJpbmcgd2l0aCBTcGFjZXM=")

    def test_convert_string_with_special_characters_to_base64(self):
        self.assertEqual(convert_to_base64("Special characters: @#&*()"), "U3BlY2lhbCBjaGFyYWN0ZXJzOiBAIyYqKCk=")

    def test_convert_string_with_non_ascii_characters_to_base64(self):
        self.assertEqual(convert_to_base64("你好，世界！"), "5L2g5aW977yM5LiW55WM77yB")

    def test_convert_long_string_to_base64(self):
        long_string = "This is a very long string that exceeds normal lengths for testing purposes."
        self.assertEqual(convert_to_base64(long_string),
                         "VGhpcyBpcyBhIHZlcnkgbG9uZyBzdHJpbmcgdGhhdCBleGNlZWRzIG5vcm1hbCBsZW5ndGhzIGZvciB0ZXN0aW5nIHB1cnBvc2VzLg==")
