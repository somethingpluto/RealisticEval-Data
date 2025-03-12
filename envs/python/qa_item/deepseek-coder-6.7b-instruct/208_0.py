class PriorityQueue:
    """Implement a priority queue"""

    # Constructor
    def __init__(self):
        self.queue = []

    # Function to insert a new element into the priority queue
    def insert(self, value):
        self.queue.append(value)
        self.queue.sort()

    # Function to get and remove the minimum element from the priority queue
    def extract_min(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    # Function to peek at the minimum element without removing it
    def peek_min(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    # Function to check if the priority queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Function to get the size of the priority queue
    def size(self):
        return len(self.queue)

    # Function to print the contents of the priority queue
    def print(self):
        print(self.queue)
import unittest


class Tester(unittest.TestCase):

    # Test Case 1: Test insertion and extraction of the minimum element
    def test_insertion_and_extraction_of_minimum_element(self):
        pq = PriorityQueue()

        # Inserting elements into the priority queue
        pq.insert(5)
        pq.insert(2)
        pq.insert(8)
        pq.insert(1)
        pq.insert(3)

        self.assertEqual(pq.size(), 5)
        self.assertEqual(pq.peekMin(), 1)

        # Extracting the minimum element
        self.assertEqual(pq.extractMin(), 1)
        self.assertEqual(pq.extractMin(), 2)
        self.assertEqual(pq.extractMin(), 3)
        self.assertEqual(pq.extractMin(), 5)
        self.assertEqual(pq.extractMin(), 8)
        self.assertTrue(pq.isEmpty())

    # Test Case 2: Test peekMin operation
    def test_peek_minimum_element(self):
        pq = PriorityQueue()

        # Peeking at the minimum element without extraction
        pq.insert(10)
        pq.insert(4)
        pq.insert(15)

        self.assertEqual(pq.peekMin(), 4)
        self.assertEqual(pq.size(), 3)  # Size should remain the same
        self.assertEqual(pq.peekMin(), 4)  # Peek should not remove the element

    # Test Case 3: Test edge case of extracting from an empty queue
    def test_extract_from_empty_queue(self):
        pq = PriorityQueue()

        # Attempting to extract from an empty queue should throw an exception
        with self.assertRaises(RuntimeError):
            pq.extractMin()

    # Test Case 4: Test isEmpty function
    def test_check_if_priority_queue_is_empty(self):
        pq = PriorityQueue()

        # Newly created queue should be empty
        self.assertTrue(pq.isEmpty())

        # Queue should not be empty after insertion
        pq.insert(7)
        self.assertFalse(pq.isEmpty())

        # Queue should be empty after extracting all elements
        pq.extractMin()
        self.assertTrue(pq.isEmpty())

    # Test Case 5: Test multiple insertions and order of extraction
    def test_multiple_insertions_and_extraction_order(self):
        pq = PriorityQueue()

        # Inserting multiple elements and checking extraction order
        pq.insert(9)
        pq.insert(4)
        pq.insert(6)
        pq.insert(1)
        pq.insert(8)

        extracted_elements = []
        while not pq.isEmpty():
            extracted_elements.append(pq.extractMin())

        expected_order = [1, 4, 6, 8, 9]
        self.assertEqual(extracted_elements, expected_order)

if __name__ == '__main__':
    unittest.main()