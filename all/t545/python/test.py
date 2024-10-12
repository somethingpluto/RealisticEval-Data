class TestElementsBeforeNull(unittest.TestCase):

    def test_returns_elements_before_first_null(self):
        input_array = ['element1', 'element2', None, 'element3', 'element4']
        result = elements_before_null(input_array)
        self.assertEqual(result, ['element1', 'element2'])

    def test_returns_empty_array_when_input_is_empty(self):
        input_array = []
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

    def test_returns_same_array_if_no_null(self):
        input_array = ['element1', 'element2', 'element3']
        result = elements_before_null(input_array)
        self.assertEqual(result, ['element1', 'element2', 'element3'])

    def test_returns_empty_array_if_first_element_is_null(self):
        input_array = [None, 'element2', 'element3']
        result = elements_before_null(input_array)
        self.assertEqual(result, [])

    def test_handles_mixed_types_with_null(self):
        input_array = [1, 'text', None, True, False]
        result = elements_before_null(input_array)
        self.assertEqual(result, [1, 'text'])

    def test_handles_array_with_only_null(self):
        input_array = [None]
        result = elements_before_null(input_array)
        self.assertEqual(result, [])
