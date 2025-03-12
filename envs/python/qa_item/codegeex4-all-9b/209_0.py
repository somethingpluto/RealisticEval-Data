class Node:
    def __init__(self, value):
        self.data = value  # Data held by the node
        self.next = None   # Pointer to the next node in the list

# LinkedList class definition
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the linked list

    # Method to add a node at the beginning of the list
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Method to add a node at the end of the list
    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to delete a node with a specific value
    def delete_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    # Method to search for a value in the list
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Method to print all elements in the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
# ll = LinkedList()
# ll.insert_at_head(3)
# ll.insert_at_head(2)
# ll.insert_at_head(1)
# ll.print_list()  # Output: 1 -> 2 -> 3 -> None
# ll.delete_value(2)
# ll.print_list()  # Output: 1 -> 3 -> None
# print(ll.search(3))  # Output: True
# print(ll.search(2))  # Output: False
import unittest


class Tester(unittest.TestCase):

    def test_insertion_at_head(self):
        list = LinkedList()
        list.insertAtHead(10)
        list.insertAtHead(20)
        list.insertAtHead(30)
        # Expected: 30 -> 20 -> 10 -> None
        self.assertTrue(list.search(10))
        self.assertTrue(list.search(20))
        self.assertTrue(list.search(30))
        self.assertFalse(list.search(40))

    def test_insertion_at_tail(self):
        list = LinkedList()
        list.insertAtTail(1)
        list.insertAtTail(2)
        list.insertAtTail(3)
        # Expected: 1 -> 2 -> 3 -> None
        self.assertTrue(list.search(1))
        self.assertTrue(list.search(2))
        self.assertTrue(list.search(3))
        self.assertFalse(list.search(4))

    def test_deletion_of_elements(self):
        list = LinkedList()
        list.insertAtHead(5)
        list.insertAtHead(10)
        list.insertAtHead(15)
        list.deleteValue(10)
        # Expected: 15 -> 5 -> None
        self.assertFalse(list.search(10))
        self.assertTrue(list.search(15))
        self.assertTrue(list.search(5))

        list.deleteValue(15)
        # Expected: 5 -> None
        self.assertFalse(list.search(15))
        self.assertTrue(list.search(5))

        list.deleteValue(5)
        # Expected: None
        self.assertFalse(list.search(5))

    def test_search_functionality(self):
        list = LinkedList()
        list.insertAtTail(100)
        list.insertAtTail(200)
        list.insertAtTail(300)
        self.assertTrue(list.search(100))
        self.assertTrue(list.search(200))
        self.assertTrue(list.search(300))
        self.assertFalse(list.search(400))

    def test_edge_case_empty_list(self):
        list = LinkedList()
        self.assertFalse(list.search(1))  # Searching in an empty list
        list.deleteValue(1)  # Deleting from an empty list should not crash
        # Expected: None (still empty)
        self.assertEqual(list.printList(), None)  # or whatever the printList function returns for empty

if __name__ == '__main__':
    unittest.main()