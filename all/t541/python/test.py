class TestFilterArray(unittest.TestCase):

    def test_filters_out_numbers_less_than_or_equal_to_ten(self):
        unfiltered_array = [5, 12, 3, 18, 7, 10, 15]
        result = filter_array(unfiltered_array, is_greater_than_ten)
        self.assertEqual(result, [12, 18, 15])

    def test_returns_empty_array_when_all_elements_are_disqualified(self):
        unfiltered_array = [1, 2, 3, 4, 5]
        result = filter_array(unfiltered_array, is_greater_than_ten)
        self.assertEqual(result, [])

    def test_returns_same_array_when_all_elements_are_qualified(self):
        unfiltered_array = [11, 12, 15, 20]
        result = filter_array(unfiltered_array, is_greater_than_ten)
        self.assertEqual(result, [11, 12, 15, 20])

    def test_handles_empty_array_input(self):
        unfiltered_array = []
        result = filter_array(unfiltered_array, is_greater_than_ten)
        self.assertEqual(result, [])

    def test_filters_out_strings_based_on_length(self):
        unfiltered_array = ['a', 'ab', 'abc', 'abcd', 'abcde']
        result = filter_array(unfiltered_array, is_longer_than_three_chars)
        self.assertEqual(result, ['abcd', 'abcde'])

    def test_correctly_filters_array_with_mixed_types(self):
        unfiltered_array = [1, 'hello', True, 'world', None]
        result = filter_array(unfiltered_array, is_string)
        self.assertEqual(result, ['hello', 'world'])

    def test_filters_based_on_object_property(self):
        unfiltered_array = [{'value': 3}, {'value': 5}, {'value': 7}]
        result = filter_array(unfiltered_array, has_value_greater_than_five)
        self.assertEqual(result, [{'value': 7}])

    def test_returns_empty_array_when_no_qualifying_function_provided(self):
        unfiltered_array = [1, 2, 3, 4, 5]
        result = filter_array(unfiltered_array, lambda x: False)  # Always returns false
        self.assertEqual(result, [])
