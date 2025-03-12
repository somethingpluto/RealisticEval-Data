from typing import List, Any
from itertools import product

def generate_combinations(input_lists: List[List[Any]]) -> List[List[Any]]:
    combinations = list(product(*input_lists))
    return combinations
import unittest
from typing import List


class TestGenerateCombinations(unittest.TestCase):

    def test_empty_input(self):
        input_data: List[List[str]] = []
        expected: List[List[str]] = []
        self.assertEqual(generate_combinations(input_data), expected, "Testing with empty input")

    def test_single_empty_list(self):
        input_data: List[List[str]] = [[]]  # Equivalent to Arrays.asList(new ArrayList<>())
        expected: List[List[str]] = []
        self.assertEqual(generate_combinations(input_data), expected, "Testing with a single empty list")

    def test_single_non_empty_list(self):
        input_data: List[List[str]] = [["a", "b", "c"]]  # Equivalent to Arrays.asList(Arrays.asList("a", "b", "c"))
        expected: List[List[str]] = [["a"], ["b"], ["c"]]
        self.assertEqual(generate_combinations(input_data), expected, "Testing with a single non-empty list")

    def test_multiple_lists(self):
        input_data: List[List[str]] = [["a", "b"], ["1", "2"]]  # Equivalent to Arrays.asList(Arrays.asList("a", "b"), Arrays.asList("1", "2"))
        expected: List[List[str]] = [["a", "1"], ["a", "2"], ["b", "1"], ["b", "2"]]
        self.assertEqual(generate_combinations(input_data), expected, "Testing with multiple lists")

    def test_input_containing_empty_list(self):
        input_data: List[List[str]] = [["a", "b"], [], ["1", "2"]]  # Equivalent to the Java example
        expected: List[List[str]] = []
        self.assertEqual(generate_combinations(input_data), expected, "Testing with an input that contains an empty list")

if __name__ == '__main__':
    unittest.main()