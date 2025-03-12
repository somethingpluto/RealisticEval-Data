
from typing import List

def are_siblings(tree: List[int], val1: int, val2: int):
    """
    Determines if two values are siblings in a binary tree represented as an array.

    Args:
        tree(List[int]): the binary tree level-order representation
        val1(int):
        val2(int):

    Returns:
    """
    # Check if val1 and val2 are in the tree
    if val1 in tree and val2 in tree:
        return True
    # Check if they are on the same level
    elif val1 == tree[val1] and val2 == tree[val2]:
        return True
    # Check if they are on different levels and are not already visited
    else:
        for i in range(len(tree)):
            if val1 == tree[val1] and not are_siblings(tree[i], val2, val1):
                return False
        return True

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