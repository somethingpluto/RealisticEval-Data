from collections import deque

class UniqueDeque:

    def __init__(self):
        self._deque = deque()
        self._set = set()

    def add(self, item):
        """
        Add an item to the deque if it is not already present.

        Parameters:
        - item: The item to add.

        Returns:
        - bool: True if the item was added, False if it was already present.
        """
        if item not in self._set:
            self._deque.append(item)
            self._set.add(item)
            return True
        return False

    def delete(self, item):
        """
        Remove an item from the deque if it exists.

        Parameters:
        - item: The item to remove.

        Returns:
        - bool: True if the item was removed, False if it was not found.
        """
        if item in self._set:
            self._deque.remove(item)
            self._set.remove(item)
            return True
        return False

    def contains(self, item):
        """
        Check if an item is present in the deque.

        Parameters:
        - item: The item to check.

        Returns:
        - bool: True if the item is present, False otherwise.
        """
        return item in self._set

    def __len__(self):
        """
        Get the number of elements in the deque.

        Returns:
        - int: The number of unique elements in the deque.
        """
        return len(self._deque)

    def __iter__(self):
        """
        Create an iterator for the deque.

        Returns:
        - iterator: An iterator over the elements in the deque.
        """
        return iter(self._deque)
import unittest
from collections import deque

class TestUniqueDeque(unittest.TestCase):

    def test_add_unique_elements(self):
        ud = UniqueDeque()
        self.assertTrue(ud.add(1))
        self.assertTrue(ud.add(2))
        self.assertTrue(ud.add(3))
        self.assertEqual(len(ud), 3)
        self.assertEqual(list(ud), [1, 2, 3])

    def test_add_duplicate_elements(self):
        ud = UniqueDeque()
        self.assertTrue(ud.add(1))
        self.assertFalse(ud.add(1))  # Duplicate add should return False
        self.assertEqual(len(ud), 1)
        self.assertEqual(list(ud), [1])

    def test_delete_elements(self):
        ud = UniqueDeque()
        ud.add(1)
        ud.add(2)
        ud.add(3)
        self.assertTrue(ud.delete(2))
        self.assertFalse(ud.delete(2))  # Deleting non-existing element should return False
        self.assertEqual(len(ud), 2)
        self.assertEqual(list(ud), [1, 3])

    def test_contains(self):
        ud = UniqueDeque()
        ud.add(1)
        self.assertTrue(ud.contains(1))
        self.assertFalse(ud.contains(2))
        ud.delete(1)
        self.assertFalse(ud.contains(1))

    def test_iter_and_len(self):
        ud = UniqueDeque()
        ud.add(1)
        ud.add(2)
        self.assertEqual(len(ud), 2)
        items = list(iter(ud))
        self.assertEqual(items, [1, 2])
        ud.delete(1)
        self.assertEqual(len(ud), 1)
        self.assertEqual(list(ud), [2])
if __name__ == '__main__':
    unittest.main()