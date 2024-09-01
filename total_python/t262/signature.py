from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: TreeNode) -> List[float]:
    """
    Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

    Args:
        root (TreeNode): The root of the binary tree.

    Returns:
        List[float]: A list containing the average values of each level.
    """
