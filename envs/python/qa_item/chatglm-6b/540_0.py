
def generate_unique_pairs(array: list) -> list:
    """
    Generates all unique combinations of pairs from a list.

    Args:
        array (list): The input list from which combinations are generated.

    Returns:
        list of lists: A list of lists, where each inner list contains a unique pair of elements.
    """
    # Create a set to store the unique pairs
    unique_pairs = set()

    # Iterate over the input list
    for i in range(len(array)):
        # If the current pair is already in the set, don't generate it
        if array[i] in unique_pairs:
            continue

        # Add the current pair to the set and generate a new pair
        unique_pairs.add(array[i])
        for j in range(i+1, len(array)):
            array[i], array[j] = array[j], array[i]

    # Return the list of lists
    return list(unique_pairs)

import unittest


class TestGenerateUniquePairs(unittest.TestCase):

    def test_generates_unique_pairs_from_three_elements(self):
        items = ['A', 'B', 'C']
        result = generate_unique_pairs(items)
        self.assertEqual(result, [('A', 'B'), ('A', 'C'), ('B', 'C')])

    def test_generates_unique_pairs_from_two_elements(self):
        items = ['A', 'B']
        result = generate_unique_pairs(items)
        self.assertEqual(result, [('A', 'B')])

    def test_returns_empty_array_when_input_array_is_empty(self):
        items = []
        result = generate_unique_pairs(items)
        self.assertEqual(result, [])

    def test_returns_empty_array_when_input_array_has_one_element(self):
        items = ['A']
        result = generate_unique_pairs(items)
        self.assertEqual(result, [])

    def test_handles_array_with_different_types_of_elements(self):
        items = [1, 'A', {'key': 'value'}]
        result = generate_unique_pairs(items)
        self.assertEqual(result, [(1, 'A'), (1, {'key': 'value'}), ('A', {'key': 'value'})])

    def test_generates_pairs_from_array_with_more_than_three_elements(self):
        items = ['A', 'B', 'C', 'D']
        result = generate_unique_pairs(items)
        self.assertEqual(result, [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')])
if __name__ == '__main__':
    unittest.main()