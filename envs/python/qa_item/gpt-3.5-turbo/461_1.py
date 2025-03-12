from typing import List, Optional
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    """
    Calculate the average value of nodes at each level of a binary tree.

    Args:
        root (Optional[TreeNode]): The root of the binary tree.

    Returns:
        List[float]: A list of averages for each level of the binary tree.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)

    return result
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

if __name__ == '__main__':
    unittest.main()