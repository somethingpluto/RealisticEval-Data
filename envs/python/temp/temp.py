def read_sequences_from_file(filename):
    """Read sequences from a file and return them as a list of lists."""
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            # Assuming sequences are comma-separated in the file
            seq = list(map(int, line.strip().split(',')))  # Convert to a list of integers
            sequences.append(seq)
    return sequences


def is_munodi_sequence(sequence):
    """Check if the given sequence is a Munodi sequence."""
    if len(sequence) < 2:
        return False  # A sequence with less than 2 elements cannot be a Munodi sequence

    common_difference = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i - 1] != common_difference:
            return False  # Found a different difference, not a Munodi sequence
    return True  # All differences are the same


def check_sequences(filename):
    """Read sequences from a file and determine if each is a Munodi sequence."""
    sequences = read_sequences_from_file(filename)
    results = {}
    for seq in sequences:
        results[tuple(seq)] = is_munodi_sequence(seq)
    return results

import unittest


class TestCheckSequences(unittest.TestCase):
    def setUp(self):
        """Set up the test cases with sequences."""
        # Create a temporary file with test cases
        self.test_file = 'test_sequences.dat'
        with open(self.test_file, 'w') as f:
            f.write("2,4,6,8\n")    # Munodi sequence (d = 2)
            f.write("1,3,5,7\n")    # Munodi sequence (d = 2)
            f.write("10,20,30\n")   # Munodi sequence (d = 10)
            f.write("1,2,4,8\n")    # Not a Munodi sequence (d changes)
            f.write("5,10,15,20\n") # Munodi sequence (d = 5)

    def test_sequences(self):
        """Test the sequences for Munodi property."""
        expected_results = {
            (2, 4, 6, 8): True,
            (1, 3, 5, 7): True,
            (10, 20, 30): True,
            (1, 2, 4, 8): False,
            (5, 10, 15, 20): True,
        }
        results = check_sequences(self.test_file)
        for seq in expected_results:
            self.assertEqual(results[seq], expected_results[seq])

    def tearDown(self):
        """Clean up the test file after tests."""
        import os
        os.remove(self.test_file)
if __name__ == '__main__':
    unittest.main()