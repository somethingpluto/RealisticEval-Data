from typing import List


def are_siblings(tree: List[int], val1: int, val2: int):
    """
    Determines if two values are siblings in a binary tree represented as an array.

    :param tree: List[int], the binary tree level-order representation
    :param val1: int, first value to check for sibling relationship
    :param val2: int, second value to check for sibling relationship
    :return: bool, True if val1 and val2 are siblings, False otherwise
    """
    def get_parent_index(tree: List[int], node_index: int) -> int:
        return (node_index - 1) // 2

    def are_siblings_helper(tree: List[int], val1: int, val2: int):
        val1_index = tree.index(val1)
        val2_index = tree.index(val2)
        
        parent1_index = get_parent_index(tree, val1_index)
        parent2_index = get_parent_index(tree, val2_index)
        
        return parent1_index == parent2_index

    return are_siblings_helper(tree, val1, val2)
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