import random
import string

def generate_uuid() -> str:
    """
    Generate a random UUID of length 36.

    The UUID contains at least one uppercase letter, at least one lowercase letter, and at least one digit.

    Returns:
        str: A 36-character UUID string.
    """
    uuid = []
    
    # Ensure at least one uppercase letter
    uuid.append(random.choice(string.ascii_uppercase))
    
    # Ensure at least one lowercase letter
    uuid.append(random.choice(string.ascii_lowercase))
    
    # Ensure at least one digit
    uuid.append(random.choice(string.digits))
    
    # Fill the rest of the UUID with random characters
    for _ in range(33):
        uuid.append(random.choice(string.ascii_letters + string.digits))
    
    # Shuffle the characters to ensure randomness
    random.shuffle(uuid)
    
    # Join the list into a string and return
    return ''.join(uuid)
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