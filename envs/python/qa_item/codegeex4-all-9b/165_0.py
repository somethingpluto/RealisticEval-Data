import base64

def base64_to_url_safe(base64: str) -> str:
    """
    Converts a standard Base64 encoded string into a URL-safe Base64 encoded string.

    Args:
        base64 (str): The standard Base64 encoded string to be converted.

    Returns:
        str: The URL-safe Base64 encoded string, which replaces '+' with '-' and '/' with '_'
             and may remove any trailing '=' padding.
    """
    # Replace '+' with '-' and '/' with '_'
    url_safe = base64.replace('+', '-').replace('/', '_')

    # Remove any trailing '=' padding
    padding = len(url_safe) % 4
    if padding:
        url_safe = url_safe[:-padding]

    return url_safe
import unittest


class TestBase64ToUrlSafe(unittest.TestCase):

    def test_correct_conversion_to_url_safe_format(self):
        base64 = "YW55IGNhcm5hbCBwbGVhc3VyZS4+/w=="
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "YW55IGNhcm5hbCBwbGVhc3VyZS4-_w")

    def test_empty_string_input(self):
        base64 = ""
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "")

    def test_remove_trailing_equals(self):
        base64 = "dGVzdA=="
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "dGVzdA")

    def test_no_replacement_needed(self):
        base64 = "dGVzdA"
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "dGVzdA")

    def test_multiple_plus_and_slash(self):
        base64 = "aGVsbG8rL3dvcmxkLw=="
        result = base64_to_url_safe(base64)
        self.assertEqual(result, "aGVsbG8rL3dvcmxkLw")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            base64_to_url_safe(None)  # Testing with None as input

if __name__ == '__main__':
    unittest.main()