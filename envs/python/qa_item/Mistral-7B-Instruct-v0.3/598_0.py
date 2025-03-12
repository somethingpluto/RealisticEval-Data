class Node:
    def __init__(self, val):
        self.data = val  # Data value of the node
        self.next = None  # Pointer to the next node in the linked list

class Queue:
    def __init__(self):
        self.head = None  # Pointer to the front of the queue
        self.tail = None  # Pointer to the end of the queue

    def is_empty(self):
        return self.head == None

    def enqueue(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.tail is None:  # If the queue is empty, both head and tail will point to the new node
            self.head = new_node
            self.tail = new_node
        else:  # If the queue is not empty, update the tail's next pointer to point to the new node, and update the tail to the new node
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty. Cannot dequeue.")
        front_value = self.head.data  # Save the front value
        self.head = self.head.next  # Update the head to point to the next node
        if self.head is None:  # If the dequeued node was the last node, update the tail to None
            self.tail = None
        return front_value  # Return the front value

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty. Cannot get front.")
        return self.head.data  # Return the data of the front node
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