import random
import string

def generate_uuid() -> str:
    characters = string.ascii_letters + string.digits
    uuid = ''.join(random.choices(string.ascii_uppercase, k=1) + 
                   random.choices(string.ascii_lowercase, k=1) + 
                   random.choices(string.digits, k=1) + 
                   random.choices(characters, k=33))
    return uuid
import re
import unittest


class TestGenerateUUID(unittest.TestCase):

    def test_should_return_a_string(self):
        result = generate_uuid()
        self.assertIsInstance(result, str)

    def test_should_return_a_string_of_length_36(self):
        result = generate_uuid()
        self.assertEqual(len(result), 36)

    def test_should_generate_different_UUIDs_on_consecutive_calls(self):
        uuid1 = generate_uuid()
        uuid2 = generate_uuid()
        self.assertNotEqual(uuid1, uuid2)

    def test_should_generate_UUIDs_that_include_uppercase(self):
        result = generate_uuid()
        self.assertTrue(re.search(r'[A-Z]', result) is not None)  # At least one uppercase letter

    def test_should_generate_UUIDs_that_include_lowercase(self):
        result = generate_uuid()
        self.assertTrue(re.search(r'[a-z]', result) is not None)  # At least one lowercase letter

    def test_should_generate_UUIDs_that_include_digits(self):
        result = generate_uuid()
        self.assertTrue(re.search(r'[0-9]', result) is not None)  # At least one digit

if __name__ == '__main__':
    unittest.main()