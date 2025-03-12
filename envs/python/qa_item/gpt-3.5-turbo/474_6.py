from typing import List

def are_siblings(tree:List[int], val1:int, val2:int):
    """
    Determines if two values are siblings in a binary tree represented as an array.

    Args:
        tree(List[int]): the binary tree level-order representation
        val1(int):
        val2(int):

    Returns:
        bool: True if val1 and val2 are siblings, False otherwise
    """
    
    # Helper function to find the index of a given value in the tree list
    def find_index(val):
        for i in range(len(tree)):
            if tree[i] == val:
                return i
        return -1
    
    # Check if val1 and val2 are siblings
    index1 = find_index(val1)
    index2 = find_index(val2)
    
    # Siblings in a binary tree should have the same parent
    parent_index1 = (index1 - 1) // 2
    parent_index2 = (index2 - 1) // 2
    
    return parent_index1 == parent_index2
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