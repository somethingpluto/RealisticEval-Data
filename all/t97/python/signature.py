class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, element):
        """Adds an element to the end of the queue.

        Args:
            element: The element to be added to the queue.
        """

    def dequeue(self):
        """Removes and returns the element from the front of the queue.

        Returns:
            The removed element from the front of the queue, or "Underflow" if the queue is empty.
        """

    def front(self):
        """Returns the front element of the queue without removing it.

        Returns:
            The front element of the queue, or "No elements in Queue" if the queue is empty.
        """

    def is_empty(self):
        """Checks if the queue is empty.

        Returns:
            True if the queue is empty, otherwise False.
        """
        return len(self.items) == 0

    def print_queue(self):
        """Returns a string representation of all the elements in the queue.

        Returns:
            A string containing all elements in the queue, separated by spaces.
        """