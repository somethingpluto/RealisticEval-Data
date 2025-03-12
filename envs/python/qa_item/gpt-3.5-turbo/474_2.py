from typing import List

def are_siblings(tree:List[int], val1:int, val2:int):
    if not tree:
        return False
    
    tree_len = len(tree)
    
    # Find the indexes of the two values in the tree
    val1_index = -1
    val2_index = -1
    
    for i in range(tree_len):
        if tree[i] == val1:
            val1_index = i
        elif tree[i] == val2:
            val2_index = i
    
    # Check if the indexes are siblings
    if val1_index % 2 == 0:
        return val2_index == val1_index + 1
    elif val1_index % 2 == 1:
        return val2_index == val1_index - 1
    else:
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