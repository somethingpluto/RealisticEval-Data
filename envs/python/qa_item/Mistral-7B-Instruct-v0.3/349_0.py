from itertools import product
from typing import List, Any

def generate_combinations(input_lists: List[List[Any]]) -> List[List[Any]]:
    if not input_lists:
        return []

    if len(input_lists) == 1:
        return [list(i) for i in product(*input_lists)]

    combinations = generate_combinations(input_lists[1:])
    flat_combinations = [comb for comb in combinations for _ in input_lists[0]]
    return [list(i) for i in product(*(input_lists[0]))] + \
           [list(i + (comb[0],)) for comb in flat_combinations]
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