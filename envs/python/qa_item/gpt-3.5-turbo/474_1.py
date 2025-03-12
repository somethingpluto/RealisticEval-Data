from typing import List

def are_siblings(tree:List[int], val1:int, val2:int):
    if not tree:
        return False
    
    n = len(tree)
    for i in range(n):
        if tree[i] == val1:
            parent_idx = (i - 1) // 2
            if parent_idx < 0:
                return False
            sibling_idx = i - 1 if i % 2 == 0 else i + 1
            if sibling_idx < n and (tree[sibling_idx] == val2):
                return True
        elif tree[i] == val2:
            parent_idx = (i - 1) // 2
            if parent_idx < 0:
                return False
            sibling_idx = i - 1 if i % 2 == 0 else i + 1
            if sibling_idx < n and (tree[sibling_idx] == val1):
                return True

    return False
import unittest

class TestAreSiblings(unittest.TestCase):
    def setUp(self):
        # Setting up a binary tree used for all the test cases
        self.tree = [1, 2, 3, 4, 5, 6, 7]

    def test_basic_case(self):
        # Test with nodes 4 and 5, which are siblings
        result = are_siblings(self.tree, 4, 5)
        self.assertTrue(result)

    def test_non_sibling_case(self):
        # Test with nodes 4 and 6, which are not siblings
        result = are_siblings(self.tree, 4, 6)
        self.assertFalse(result)

    def test_root_node_case(self):
        # Test with node 1 (root) and any other node, should return False
        result = are_siblings(self.tree, 1, 2)
        self.assertFalse(result)

    def test_non_existent_values(self):
        # Test with non-existent values
        result = are_siblings(self.tree, 8, 9)
        self.assertFalse(result)

    def test_same_node_case(self):
        # Test with the same node for both values
        result = are_siblings(self.tree, 4, 4)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()