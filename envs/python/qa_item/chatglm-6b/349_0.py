
from typing import List, Any

def generate_combinations(input_lists: List[List[Any]]) -> List[List[Any]]:
    """
    Generates all possible combinations of elements from a list of lists.
    Each combination consists of picking exactly one element from each list in the input list of lists.
    This method is useful for generating product variations, scenarios in decision-making tools,
    or any context where all possible combinations of a set of options need to be explored.

    Args:
        input_lists (List[List[Any]]): A list of lists containing the elements to combine.
                                         The lists must not be empty but can contain elements of any type.

    Returns:
        List[List[Any]]: A list of lists, where each inner list represents a possible combination of elements
                         taken from the input lists. Returns an empty list if the input list is empty.
    """
    # Create a dictionary to store the combinations
    combinations = {}

    # Iterate over the input lists
    for i in range(len(input_lists)):
        # Iterate over the sublists of the current input list
        for j in range(i, len(input_lists)):
            # If the current sublist is empty, add it to the dictionary
            if input_lists[j] == []:
                combinations[input_lists[j]] = []
            # If the current sublist contains an element, add it to the dictionary
            else:
                combinations[input_lists[j]].append(input_lists[j][0])

    # Return the dictionary of combinations
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