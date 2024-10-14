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
