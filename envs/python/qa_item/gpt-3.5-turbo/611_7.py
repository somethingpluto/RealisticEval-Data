import string
import random

def generate_random_string() -> str:
    letters = string.ascii_letters
    upper_case_letters = string.ascii_uppercase
    lower_case_letters = string.ascii_lowercase

    upper_case_char = random.choice(upper_case_letters)
    lower_case_char = random.choice(lower_case_letters)

    remaining_chars = ''.join(random.choices(letters, k=23))
    
    return upper_case_char + lower_case_char + remaining_chars
import unittest


class TestGenerateRandomString(unittest.TestCase):

    def test_length(self):
        random_string = generate_random_string()
        self.assertEqual(len(random_string), 25, "The generated string length should be 25.")

    def test_contains_upper_case(self):
        random_string = generate_random_string()
        self.assertTrue(any(char.isupper() for char in random_string),
                        "The generated string should contain at least one uppercase letter.")

    def test_contains_lower_case(self):
        random_string = generate_random_string()
        self.assertTrue(any(char.islower() for char in random_string),
                        "The generated string should contain at least one lowercase letter.")

    def test_randomness(self):
        string1 = generate_random_string()
        string2 = generate_random_string()
        self.assertNotEqual(string1, string2, "Two generated strings should not be the same.")

    def test_multiple_generations(self):
        num_tests = 100
        has_upper_case = False
        has_lower_case = False

        for _ in range(num_tests):
            random_string = generate_random_string()
            has_upper_case |= any(char.isupper() for char in random_string)
            has_lower_case |= any(char.islower() for char in random_string)

        self.assertTrue(has_upper_case, "At least one generated string should contain an uppercase letter.")
        self.assertTrue(has_lower_case, "At least one generated string should contain a lowercase letter.")

if __name__ == '__main__':
    unittest.main()