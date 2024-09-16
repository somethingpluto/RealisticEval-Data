from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root):
    """
    Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

    Args:
        root (TreeNode): The root of the binary tree.

    Returns:
        List[float]: A list containing the average values of each level.
    """
    if not root:
        return []

    result = []
    queue = deque([(root, 0)])  # (node, level)

    while queue:
        current_level = []
        level_size = len(queue)

        for _ in range(level_size):
            node, level = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Calculate the average for the current level
        level_average = sum(current_level) / len(current_level)
        result.append(level_average)

    return result