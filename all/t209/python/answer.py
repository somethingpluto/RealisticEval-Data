class Node:
    def __init__(self, value):
        """Initialize a new node with given data."""
        self.data = value  # Data held by the node
        self.next = None   # Pointer to the next node in the list


class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # Pointer to the first node in the list

    def __del__(self):
        """Destructor to clean up memory."""
        current = self.head
        while current is not None:
            next_node = current.next
            del current  # Delete the current node
            current = next_node

    def insert_at_head(self, value):
        """Add a node at the beginning of the list."""
        new_node = Node(value)  # Create a new node
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node

    def insert_at_tail(self, value):
        """Add a node at the end of the list."""
        new_node = Node(value)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # New node becomes the head
        else:
            current = self.head
            while current.next is not None:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the last node to the new node

    def delete_value(self, value):
        """Delete a node with a specific value."""
        if self.head is None:
            return  # List is empty, nothing to delete

        # If the head needs to be deleted
        if self.head.data == value:
            temp = self.head
            self.head = self.head.next  # Update head to the next node
            del temp  # Delete the old head
            return

        # Traverse to find the node to delete
        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next

        # If the node was found, delete it
        if current.next is not None:
            temp = current.next
            current.next = current.next.next  # Unlink the node from the list
            del temp  # Delete the node

    def search(self, value):
        """Search for a value in the list."""
        current = self.head
        while current is not None:
            if current.data == value:
                return True  # Value found
            current = current.next
        return False  # Value not found

    def print_list(self):
        """Print all elements in the list."""
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list
