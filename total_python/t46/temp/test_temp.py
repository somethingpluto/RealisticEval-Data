import unittest


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        """Setup basic tree structure for testing."""
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \
        #  4   5
        self.tree = BinaryTree(TreeNode(1))
        self.tree.root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        self.tree.root.right = TreeNode(3)

    def test_preorder_traversal(self):
        """Test preorder traversal."""
        result = self.tree.preorder_traversal(self.tree.root)
        self.assertEqual(result, [1, 2, 4, 5, 3])

    def test_inorder_traversal(self):
        """Test inorder traversal."""
        result = self.tree.inorder_traversal(self.tree.root)
        self.assertEqual(result, [4, 2, 5, 1, 3])

    def test_postorder_traversal(self):
        """Test postorder traversal."""
        result = self.tree.postorder_traversal(self.tree.root)
        self.assertEqual(result, [4, 5, 2, 3, 1])

    def test_empty_tree(self):
        """Test traversals on an empty tree."""
        empty_tree = BinaryTree()
        self.assertEqual(empty_tree.preorder_traversal(empty_tree.root), [])
        self.assertEqual(empty_tree.inorder_traversal(empty_tree.root), [])
        self.assertEqual(empty_tree.postorder_traversal(empty_tree.root), [])

    def test_single_node_tree(self):
        """Test all traversals on a tree with only one node."""
        single_node_tree = BinaryTree(TreeNode(10))
        self.assertEqual(single_node_tree.preorder_traversal(single_node_tree.root), [10])
        self.assertEqual(single_node_tree.inorder_traversal(single_node_tree.root), [10])
        self.assertEqual(single_node_tree.postorder_traversal(single_node_tree.root), [10])

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
