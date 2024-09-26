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
