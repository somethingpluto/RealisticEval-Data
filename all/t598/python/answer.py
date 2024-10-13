class Node:
    """Node structure for linked list."""
    def __init__(self, val):
        """Initialize the node with data and a pointer to the next node."""
        self.data = val  # Data value of the node
        self.next = None  # Pointer to the next node in the linked list


class Queue:
    """Queue class using a linked list."""
    def __init__(self):
        """Initialize the queue."""
        self.head = None  # Pointer to the front of the queue
        self.tail = None  # Pointer to the end of the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.head is None  # Queue is empty if head is None

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        new_node = Node(value)  # Create a new node
        if self.tail:
            self.tail.next = new_node  # Link the new node at the end
        else:
            self.head = new_node  # If the queue is empty, the new node is also the head
        self.tail = new_node  # Update the tail to the new node

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None  # Return None instead of -1 for invalid value
        temp = self.head  # Temporarily store the head node
        value = self.head.data  # Get the data from the head node
        self.head = self.head.next  # Move head to the next node
        if self.head is None:  # If the queue becomes empty
            self.tail = None  # Update the tail as well
        return value  # Return the dequeued value

    def front(self):
        """Get the front element without removing it."""
        if self.is_empty():
            print("Queue is empty. Cannot access front.")
            return None  # Return None instead of -1 for invalid value
        return self.head.data  # Return the front value