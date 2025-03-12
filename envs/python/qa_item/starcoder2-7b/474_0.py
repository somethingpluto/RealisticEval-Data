from typing import List

def are_siblings(tree:List[int], val1:int, val2:int) -> bool:
    """
    Determines if two values are siblings in a binary tree represented as an array.

    Args:
        tree(List[int]): the binary tree level-order representation
        val1(int):
        val2(int):

    Returns:
        bool: True if val1 and val2 are siblings, False otherwise
    """
    # Find the index of val1 and val2 in the tree
    index1 = tree.index(val1) if val1 in tree else -1
    index2 = tree.index(val2) if val2 in tree else -1

    # If either val1 or val2 is not in the tree, they are not siblings
    if index1 == -1 or index2 == -1:
        return False

    # The parent of val1 and val2 is the same if they are siblings
    # The parent of a node in a binary tree is the node at index (i-1)//2
    parent1 = (index1 - 1) // 2
    parent2 = (index2 - 1) // 2

    return parent1 == parent2
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