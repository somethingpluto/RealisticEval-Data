from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def average_of_levels(root: TreeNode) -> List[float]:
    result = []
    if not root:
        return result
        
    queue = [root]
    
    while queue:
        level_sum = 0
        level_count = 0
        next_level = []
        
        for node in queue:
            level_sum += node.val
            level_count += 1
            
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        result.append(level_sum / level_count)
        queue = next_level
    
    return result
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestAverageOfLevels(unittest.TestCase):

    def test_empty_tree(self):
        root = None
        expected = []
        self.assertEqual(average_of_levels(root), expected)

    def test_single_node_tree(self):
        root = TreeNode(5)
        expected = [5.0]
        self.assertEqual(average_of_levels(root), expected)

    def test_balanced_tree_two_levels(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        expected = [3.0, 14.5]  # Level 0: 3; Level 1: (9+20)/2 = 14.5
        self.assertEqual(average_of_levels(root), expected)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [1.0, 2.0, 3.0]  # Level 0: 1; Level 1: 2; Level 2: 3
        self.assertEqual(average_of_levels(root), expected)

    def test_tree_multiple_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(8)
        expected = [1.0, 2.5, 5.67]  # Level 0: 1; Level 1: (2+3)/2 = 2.5; Level 2: (4+5+8)/3 ≈ 5.67
        self.assertAlmostEqual(average_of_levels(root)[2], expected[2], places=2)
        self.assertEqual(average_of_levels(root)[:2], expected[:2])
if __name__ == '__main__':
    unittest.main()