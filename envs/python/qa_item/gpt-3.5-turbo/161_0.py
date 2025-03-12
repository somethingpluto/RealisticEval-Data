from typing import Dict, List

def generate_combinations(map: Dict[str, List[int]]) -> List[List[int]]:
    """
    Produces all combinations of numeric arrays for each key in the given map object and returns them as a two-dimensional array.

    Args:
        map (Dict[str, List[int]]): A map where each key is a string, and each value is an array of numbers.

    Returns:
        List[List[int]]: An array of arrays, where each sub-array is a unique combination of numbers from the map's values.
    """
    def helper(key_index, current_combination, combinations):
        if key_index == len(keys):
            combinations.append(current_combination.copy())
            return
        key = keys[key_index]
        for num in map[key]:
            helper(key_index + 1, current_combination + [num], combinations)

    keys = list(map.keys())
    combinations = []
    helper(0, [], combinations)
    return combinations
import unittest


class TestGenerateCombinations(unittest.TestCase):

    def test_single_key_multiple_values(self):
        # Test: generates combinations for a single key with multiple values
        map_data = {'a': [1, 2, 3]}
        expected = [[1], [2], [3]]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_multiple_keys_single_values(self):
        # Test: generates combinations for multiple keys with single values
        map_data = {'a': [1], 'b': [2]}
        expected = [[1, 2]]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_multiple_keys_multiple_values(self):
        # Test: generates combinations for multiple keys with multiple values
        map_data = {'a': [1, 2], 'b': [3, 4]}
        expected = [
            [1, 3], [1, 4],
            [2, 3], [2, 4]
        ]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_empty_map(self):
        # Test: handles an empty map
        map_data = {}
        expected = [[]]
        self.assertEqual(generate_combinations(map_data), expected)

    def test_empty_array_values(self):
        # Test: handles keys with empty arrays as values
        map_data = {'a': [], 'b': [1, 2]}
        expected = []
        self.assertEqual(generate_combinations(map_data), expected)

if __name__ == '__main__':
    unittest.main()