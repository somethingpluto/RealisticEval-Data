class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class PriorityQueue:
    """Implement a priority queue"""

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            if current.value > value:
                new_node.next = current
                self.head = new_node
            else:
                while current.next is not None and current.next.value <= value:
                    current = current.next
                new_node.next = current.next
                current.next = new_node
        self.length += 1

    def extract_min(self):
        if self.head is None:
            return None
        else:
            min_value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return min_value

    def peek_min(self):
        if self.head is None:
            return None
        return self.head.value

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
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