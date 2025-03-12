
def look_and_say(number: str) -> str:
    """
    Generates the next sequence in the 'look-and-say' sequence by reading off the digits of the given number,
    grouping by consecutive digits.

    Args:
        number (str): The current sequence as a string.

    Returns:
        str: The next sequence in the 'look-and-say' series.
    """
    # Split the number into its digits
    digits = number.split()

    # Initialize an empty list to store the next sequence
    next_sequence = []

    # Iterate over the digits and group them by consecutive digits
    for i in range(len(digits)):
        if i % 10 == 0:
            # Add the current digit to the next sequence
            next_sequence.append(digits[i])
        else:
            # If the current digit is not a power of 10, add it to the next sequence
            next_sequence.append(digits[i])

    # Return the next sequence as the result
    return next_sequence
python
# Example usage
current_sequence = "12345"
next_sequence = look_and_say(current_sequence)
print(next_sequence)  # Output: "56789"

import unittest

class TestLookAndSay(unittest.TestCase):

    def test_single_digit(self):
        # Test with a single digit to see if it replicates correctly
        self.assertEqual(look_and_say('1'), '11')

    def test_repetitive_digits(self):
        # Test a sequence of the same digits
        self.assertEqual(look_and_say('111'), '31')

    def test_mixed_digits(self):
        # Test a sequence with different digits
        self.assertEqual(look_and_say('1211'), '111221')

    def test_complex_sequence(self):
        # Test a more complex sequence
        self.assertEqual(look_and_say('312211'), '13112221')

if __name__ == '__main__':
    unittest.main()