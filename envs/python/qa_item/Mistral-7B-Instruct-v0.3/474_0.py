from typing import List
from collections import defaultdict

def are_siblings(tree: List[int], val1: int, val2: int) -> bool:
    if not tree:
        return False

    parents = defaultdict(lambda: None)
    for i, node in enumerate(tree):
        if node not in parents:
            parents[node] = i / 2
            if i % 2 == 0:
                left_child = 2 * i + 1
                right_child = 2 * i + 2
                if left_child < len(tree) and right_child < len(tree):
                    parents[tree[left_child]] = i
                    parents[tree[right_child]] = i

    return parents[val1] == parents[val2] and parents[val1] is not None
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