import unittest


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestAverageOfLevels(unittest.TestCase):
    def test_empty_tree(self):
        """Test case for an empty tree."""
        self.assertEqual(average_of_levels(None), [])

    def test_single_node(self):
        """Test case for a tree with a single node."""
        root = TreeNode(5)
        self.assertEqual(average_of_levels(root), [5.0])

    def test_three_levels(self):
        """Test case for a tree with three levels."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        self.assertEqual(average_of_levels(root), [1.0, 2.5, 5.0])  # (1), (2, 3) -> [1.0, (2+3)/2], (4, 5, 6) -> [5.0]
