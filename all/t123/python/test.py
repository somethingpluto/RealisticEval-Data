import unittest


class TestScaleToRange(unittest.TestCase):
    def test_simple_scaling(self):
        result = scale_to_range([1, 2, 3, 4, 5], 1, 5, 10, 50)
        self.assertEqual(result, [10, 20, 30, 40, 50])

    def test_scaling_with_negative_input_range(self):
        result = scale_to_range([-5, 0, 5], -5, 5, 0, 100)
        self.assertEqual(result, [0, 50, 100])

    def test_scaling_with_negative_output_range(self):
        result = scale_to_range([0, 50, 100], 0, 100, -100, 100)
        self.assertEqual(result, [-100, 0, 100])

    def test_input_array_containing_the_same_value(self):
        result = scale_to_range([2, 2, 2], 1, 3, 0, 10)
        self.assertEqual(result, [5, 5, 5])

    def test_input_value_out_of_range_should_throw_an_error(self):
        with self.assertRaises(ValueError):
            scale_to_range([1, 2, 3, 6], 1, 5, 0, 10)
