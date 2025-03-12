from typing import List

def are_siblings(tree: List[int], val1: int, val2: int):
    parent_val1 = None
    parent_val2 = None
    
    for i in range(len(tree)):
        if 2*i+1 < len(tree) and (tree[2*i+1] == val1 or tree[2*i+1] == val2):
            if parent_val1 is None:
                parent_val1 = tree[i]
            else:
                parent_val2 = tree[i]
        if 2*i+2 < len(tree) and (tree[2*i+2] == val1 or tree[2*i+2] == val2):
            if parent_val1 is None:
                parent_val1 = tree[i]
            else:
                parent_val2 = tree[i]
    
    return parent_val1 is not None and parent_val2 is not None and parent_val1 == parent_val2
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