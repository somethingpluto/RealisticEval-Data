class TestGenerateUniquePairs(unittest.TestCase):

    def test_generates_unique_pairs_from_three_elements(self):
        items = ['A', 'B', 'C']
        result = generate_unique_pairs(items)
        self.assertEqual(result, [['A', 'B'], ['A', 'C'], ['B', 'C']])

    def test_generates_unique_pairs_from_two_elements(self):
        items = ['A', 'B']
        result = generate_unique_pairs(items)
        self.assertEqual(result, [['A', 'B']])

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
        self.assertEqual(result, [[1, 'A'], [1, {'key': 'value'}], ['A', {'key': 'value'}]])

    def test_generates_pairs_from_array_with_more_than_three_elements(self):
        items = ['A', 'B', 'C', 'D']
        result = generate_unique_pairs(items)
        self.assertEqual(result, [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']])
