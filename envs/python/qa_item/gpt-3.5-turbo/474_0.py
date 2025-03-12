from typing import List

def are_siblings(tree:List[int], val1:int, val2:int):
    if not tree:
        return False
    
    def find_parent(node, val):
        if node is None:
            return None
        
        if (node.left == val) or (node.right == val):
            return node
        
        left_parent = find_parent(node.left, val)
        if left_parent:
            return left_parent
        
        return find_parent(node.right, val)
    
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    
    root = Node(tree[0])
    nodes = {tree[0]: root}
    
    for i in range(1, len(tree), 2):
        parent = nodes[tree[i]]
        parent.left = Node(tree[i+1])
        nodes[tree[i+1]] = parent.left
        
        if i+2 < len(tree):
            parent.right = Node(tree[i+2])
            nodes[tree[i+2]] = parent.right
    
    parent1 = find_parent(root, val1)
    parent2 = find_parent(root, val2)
    
    if parent1 == parent2:
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