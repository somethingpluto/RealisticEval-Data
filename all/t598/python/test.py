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