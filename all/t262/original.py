from typing import List, Optional
from collections import deque

"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #code generated with chatgpt
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        averages = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = 0
            
            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                level_count += 1
                
                # Enqueue child nodes
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate the average value for the current level
            level_average = level_sum / level_count
            averages.append(level_average)
        
        return averages  
                

s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left= TreeNode(6)
root.right.right = TreeNode(9)        

print(s.averageOfLevels(root))