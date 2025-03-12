from collections import deque

class UniqueDeque:

    def __init__(self):
        self.deque = deque()
        self.unique_set = set()

    def add(self, item):
        if item not in self.unique_set:
            self.deque.append(item)
            self.unique_set.add(item)
            return True
        return False

    def delete(self, item):
        if item in self.unique_set:
            self.deque.remove(item)
            self.unique_set.remove(item)
            return True
        return False

    def contains(self, item):
        return item in self.unique_set

    def __len__(self):
        return len(self.unique_set)

    def __iter__(self):
        return iter(self.deque)
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