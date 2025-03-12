class Node:
    def __init__(self, val):
        self.data = val  # Data value of the node
        self.next = None  # Pointer to the next node in the linked list

# Queue class
class Queue:
    def __init__(self):
        self.head = None  # Pointer to the front of the queue
        self.tail = None  # Pointer to the end of the queue

    # Destructor to clean up the queue
    def __del__(self):
        while not self.is_empty():
            self.dequeue()

    # Function to check if the queue is empty
    def is_empty(self):
        return self.head is None

    # Function to add an element to the end of the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Function to remove and return the front element of the queue
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            front_data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return front_data

    # Function to get the front element without removing it
    def front(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
import unittest


class Tester(unittest.TestCase):

    def test_queue_operations(self):
        queue = Queue()

        # Queue should be empty initially
        self.assertTrue(queue.isEmpty(), "Queue should be empty initially")

        # Enqueue elements
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertFalse(queue.isEmpty(), "Queue should not be empty after enqueuing elements")
        self.assertEqual(queue.front(), 10, "Front element should be 10")

        # Dequeue elements
        value = queue.dequeue()
        self.assertEqual(value, 10, "First dequeued element should be 10")
        self.assertEqual(queue.front(), 20, "Now front should be 20")

        # Dequeue from an empty queue
        queue.dequeue()  # Remove 20
        queue.dequeue()  # Remove 30
        value = queue.dequeue()
        self.assertEqual(value, -1, "Should indicate that the queue is empty")

        # Front element of an empty queue
        frontValue = queue.front()
        self.assertEqual(frontValue, -1, "Should indicate that the queue is empty")

        # Queue should become empty after dequeuing all elements
        queue.enqueue(10)
        queue.enqueue(20)
        queue.dequeue()  # Remove 10
        queue.dequeue()  # Remove 20
        self.assertTrue(queue.isEmpty(), "Queue should be empty after dequeuing all elements")
if __name__ == '__main__':
    unittest.main()