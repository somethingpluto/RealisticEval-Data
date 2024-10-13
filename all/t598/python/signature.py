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
        pass

    # Function to add an element to the end of the queue
    def enqueue(self, value):
        pass

    # Function to remove and return the front element of the queue
    def dequeue(self):
        pass

    # Function to get the front element without removing it
    def front(self):
        pass