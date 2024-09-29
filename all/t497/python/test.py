import unittest


class TestBroadcastIndex(unittest.TestCase):

    def setUp(self):
        """Set up sample data for testing."""
        # Data for a standard case
        self.big_index = [0, 2, 1]
        self.big_shape = (3, 4, 5)
        self.shape = (4, 5)

        # Prepare an output index for the standard case
        self.out_index = [0] * len(self.shape)

    def test_standard_case(self):
        """Test standard broadcasting behavior."""
        broadcast_index(self.big_index, self.big_shape, self.shape, self.out_index)
        self.assertEqual(self.out_index, [2, 1], "Failed to correctly broadcast standard case.")

    def test_shape_with_one_dimension(self):
        """Test case where shape contains a dimension of size 1."""
        shape_with_one = (1, 5)
        out_index_with_one = [0] * len(shape_with_one)
        broadcast_index(self.big_index, self.big_shape, shape_with_one, out_index_with_one)
        self.assertEqual(out_index_with_one, [0, 1], "Failed to handle shape with one dimension.")

    def test_empty_shape(self):
        """Test case with an empty shape."""
        empty_shape = ()
        out_index_empty = []
        broadcast_index(self.big_index, self.big_shape, empty_shape, out_index_empty)
        self.assertEqual(out_index_empty, [], "Failed to handle empty shape.")

    def test_bigger_shape(self):
        """Test case where the big_shape is larger than the shape."""
        big_index = [1, 2, 3]
        big_shape = (4, 5, 6)
        shape = (6,)
        out_index_big = [0] * len(shape)
        broadcast_index(big_index, big_shape, shape, out_index_big)
        self.assertEqual(out_index_big, [3], "Failed to handle bigger shape case.")

    def test_shape_with_multiple_ones(self):
        """Test case with multiple dimensions of size 1 in shape."""
        shape_multiple_ones = (1, 4, 1)
        out_index_multiple_ones = [0] * len(shape_multiple_ones)
        broadcast_index(self.big_index, self.big_shape, shape_multiple_ones, out_index_multiple_ones)
        self.assertEqual(out_index_multiple_ones, [0, 2, 0], "Failed to handle shape with multiple ones.")