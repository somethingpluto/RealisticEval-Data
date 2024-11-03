import unittest


class Tester(unittest.TestCase):

    def setUp(self):
        """Create a new instance of MaxHeap before each test."""
        self.maxHeap = MaxHeap()

    def test_initial_state_of_the_heap(self):
        """Test the initial state of the heap."""
        self.assertTrue(self.maxHeap.is_empty())
        self.assertEqual(self.maxHeap.size(), 0)

    def test_insert_elements_into_the_heap(self):
        """Test inserting elements into the heap."""
        self.maxHeap.insert(10)
        self.maxHeap.insert(20)
        self.maxHeap.insert(5)
        self.assertFalse(self.maxHeap.is_empty())
        self.assertEqual(self.maxHeap.size(), 3)
        self.assertEqual(self.maxHeap.get_max(), 20)  # The maximum should be 20

    def test_extract_maximum_element_from_the_heap(self):
        """Test extracting the maximum element from the heap."""
        self.maxHeap.insert(10)
        self.maxHeap.insert(30)
        self.maxHeap.insert(20)

        maxElement = self.maxHeap.extract_max()
        self.assertEqual(maxElement, 30)  # The maximum extracted should be 30
        self.assertEqual(self.maxHeap.get_max(), 20)  # The next maximum should be 20
        self.assertEqual(self.maxHeap.size(), 2)  # Size should be 2 after extraction

    def test_heap_property_after_multiple_operations(self):
        """Test that the heap maintains max heap property after multiple operations."""
        self.maxHeap.insert(15)
        self.maxHeap.insert(10)
        self.maxHeap.insert(30)
        self.maxHeap.insert(20)
        self.maxHeap.insert(25)

        # Current max should be 30
        self.assertEqual(self.maxHeap.get_max(), 30)
        self.maxHeap.extract_max()  # Remove 30

        # After removal, the new max should be 25
        self.assertEqual(self.maxHeap.get_max(), 25)
        self.maxHeap.extract_max()  # Remove 25

        # After removal, the new max should be 20
        self.assertEqual(self.maxHeap.get_max(), 20)

        # The size of the heap should be 3 now
        self.assertEqual(self.maxHeap.size(), 3)