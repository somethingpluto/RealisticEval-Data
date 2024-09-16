class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node, result=None):
        """Recursive Preorder Traversal"""
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def inorder_traversal(self, node, result=None):
        """Recursive Inorder Traversal"""
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result=None):
        """Recursive Postorder Traversal"""
        if result is None:
            result = []
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result

    def iterative_preorder(self):
        """Iterative Preorder Traversal"""
        if not self.root:
            return []
        stack, result = [self.root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)
                stack.append(node.right)
                stack.append(node.left)
        return result

    def iterative_inorder(self):
        """Iterative Inorder Traversal"""
        stack, result = [], []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def iterative_postorder(self):
        """Iterative Postorder Traversal"""
        if not self.root:
            return []
        stack, result = [self.root], []
        while stack:
            node = stack.pop()
            result.insert(0, node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result
