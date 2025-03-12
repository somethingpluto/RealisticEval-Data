class TreeNode:
    """
    binary tree node
    """

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    binary tree
    """

    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node, result=None):
        if not node:
            return []
        if result is None:
            result = []
        result.append(node.value)
        self.preorder_traversal(node.left, result)
        self.preorder_traversal(node.right, result)
        return result

    def inorder_traversal(self, node, result=None):
        if not node:
            return []
        if result is None:
            result = []
        self.inorder_traversal(node.left, result)
        result.append(node.value)
        self.inorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result=None):
        if not node:
            return []
        if result is None:
            result = []
        self.postorder_traversal(node.left, result)
        self.postorder_traversal(node.right, result)
        result.append(node.value)
        return result
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

if __name__ == '__main__':
    unittest.main()