class MaxHeap:
    def __init__(self):
        self.heap = []  # List to store heap elements

    def heapify_up(self, index):
        if index > len(self.heap) - 1:
            return
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        max_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[max_index]:
            max_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[max_index]:
            max_index = right_child_index

        if max_index!= index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self.heapify_down(max_index)

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self.heapify_down(0)
        return max_value

    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)
import unittest


class Tester(unittest.TestCase):

    def setUp(self):
        """Create a new instance of MaxHeap before each test."""
        self.maxHeap = MaxHeap()

    def test_initial_state_of_the_heap(self):
        """Test the initial state of the heap."""
        self.assertTrue(self.maxHeap.isEmpty())
        self.assertEqual(self.maxHeap.size(), 0)

    def test_insert_elements_into_the_heap(self):
        """Test inserting elements into the heap."""
        self.maxHeap.insert(10)
        self.maxHeap.insert(20)
        self.maxHeap.insert(5)
        self.assertFalse(self.maxHeap.isEmpty())
        self.assertEqual(self.maxHeap.size(), 3)
        self.assertEqual(self.maxHeap.getMax(), 20)  # The maximum should be 20

    def test_extract_maximum_element_from_the_heap(self):
        """Test extracting the maximum element from the heap."""
        self.maxHeap.insert(10)
        self.maxHeap.insert(30)
        self.maxHeap.insert(20)

        maxElement = self.maxHeap.extractMax()
        self.assertEqual(maxElement, 30)  # The maximum extracted should be 30
        self.assertEqual(self.maxHeap.getMax(), 20)  # The next maximum should be 20
        self.assertEqual(self.maxHeap.size(), 2)  # Size should be 2 after extraction

    def test_heap_property_after_multiple_operations(self):
        """Test that the heap maintains max heap property after multiple operations."""
        self.maxHeap.insert(15)
        self.maxHeap.insert(10)
        self.maxHeap.insert(30)
        self.maxHeap.insert(20)
        self.maxHeap.insert(25)

        # Current max should be 30
        self.assertEqual(self.maxHeap.getMax(), 30)
        self.maxHeap.extractMax()  # Remove 30

        # After removal, the new max should be 25
        self.assertEqual(self.maxHeap.getMax(), 25)
        self.maxHeap.extractMax()  # Remove 25

        # After removal, the new max should be 20
        self.assertEqual(self.maxHeap.getMax(), 20)

        # The size of the heap should be 3 now
        self.assertEqual(self.maxHeap.size(), 3)

if __name__ == '__main__':
    unittest.main()