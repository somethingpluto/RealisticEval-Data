class Node:
    def __init__(self, value):
        self.data = value  # Data held by the node
        self.next = None   # Pointer to the next node in the list

# LinkedList class definition
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the list
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Method to add a node at the end of the list
    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to delete a node with a specific value
    def delete_value(self, value):
        current_node = self.head
        if current_node and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != value:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    # Method to search for a value in the list
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    # Method to print all elements in the list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')
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