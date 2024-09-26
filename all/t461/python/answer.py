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

    averages = []  # List to store the average of each level
    queue = deque([root])  # Queue for level-order traversal

    while queue:
        level_sum = 0  # Sum of node values at the current level
        level_count = len(queue)  # Number of nodes at the current level

        # Process all nodes at the current level
        for _ in range(level_count):
            node = queue.popleft()  # Dequeue the front node
            level_sum += node.val  # Add the node's value to the level sum

            # Enqueue child nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Calculate the average value for the current level
        level_average = level_sum / level_count
        averages.append(level_average)  # Append average to the result list

    return averages
