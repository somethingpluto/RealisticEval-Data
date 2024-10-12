class Queue:
    def __init__(self):
        """Initializes an empty queue."""
        self.items = []

    def enqueue(self, element):
        """Adds an element to the end of the queue."""
        self.items.append(element)

    def dequeue(self):
        """Removes and returns the element from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return "Underflow"

    def front(self):
        """Returns the front element of the queue without removing it."""
        if not self.is_empty():
            return self.items[0]
        return "No elements in Queue"

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def print_queue(self):
        """Returns a string representation of all the elements in the queue."""
        return ' '.join(map(str, self.items))


class TestQueue(unittest.TestCase):

    def setUp(self):
        """Initialize an empty queue before each test."""
        self.queue = Queue()

    def test_initialize_empty_queue(self):
        """Test if the queue is initialized empty."""
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_elements(self):
        """Test enqueueing elements into the queue."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.print_queue(), '1 2 3')
        self.assertFalse(self.queue.is_empty())

    def test_dequeue_elements(self):
        """Test dequeueing elements from the queue."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        dequeued_element = self.queue.dequeue()
        self.assertEqual(dequeued_element, 1)

    def test_front_element(self):
        """Test getting the front element without removing it."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        front_element = self.queue.front()
        self.assertEqual(front_element, 10)

    def test_check_empty_queue(self):
        """Test checking if the queue is empty."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(5)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())
