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
