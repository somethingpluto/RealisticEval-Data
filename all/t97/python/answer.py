class Queue:
    def __init__(self):
        """Initializes an empty queue."""
        self.items = []

    def enqueue(self, element):
        """
        Adds an element to the end of the queue.

        Args:
            element: The element to be added to the queue.
        """
        self.items.append(element)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
            The removed element from the front of the queue, or "Underflow" if the queue is empty.
        """
        if self.is_empty():
            return "Underflow"
        return self.items.pop(0)

    def front(self):
        """
        Returns the front element of the queue without removing it.

        Returns:
            The front element of the queue, or "No elements in Queue" if the queue is empty.
        """
        if self.is_empty():
            return "No elements in Queue"
        return self.items[0]

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, otherwise False.
        """
        return len(self.items) == 0

    def print_queue(self):
        """
        Returns a string representation of all the elements in the queue.

        Returns:
            A string containing all elements in the queue, separated by spaces.
        """
        return " ".join(map(str, self.items))
