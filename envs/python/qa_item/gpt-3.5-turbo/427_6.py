from typing import Dict

def check_sequences(filename:str) -> Dict:
    sequences = {}
    
    def is_munodi_sequence(seq):
        while seq[-1] != 1:
            if seq[-1] % 2 == 0:
                seq.append(seq[-1] // 2)
            else:
                seq.append(3 * seq[-1] + 1)
        return seq
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            nums = list(map(int, line.strip().split(',')))
            if is_munodi_sequence(nums) == [1]:
                sequences[tuple(nums)] = True
            else:
                sequences[tuple(nums)] = False
                
    return sequences
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