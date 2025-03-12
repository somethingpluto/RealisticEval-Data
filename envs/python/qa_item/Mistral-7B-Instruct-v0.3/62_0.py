class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.val)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node is not None:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.val)
import unittest


class TestBinaryTree(unittest.TestCase):

    def test_empty_tree(self):
        bt = BinaryTree()
        self.assertEqual(bt.inorder_traversal(), [])
        self.assertEqual(bt.preorder_traversal(), [])
        self.assertEqual(bt.postorder_traversal(), [])

    def test_single_node_tree(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.inorder_traversal(), [10])
        self.assertEqual(bt.preorder_traversal(), [10])
        self.assertEqual(bt.postorder_traversal(), [10])

    def test_balanced_tree(self):
        bt = BinaryTree()
        elements = [8, 3, 10, 1, 6, 9, 14]
        for elem in elements:
            bt.insert(elem)
        self.assertEqual(bt.inorder_traversal(), [1, 3, 6, 8, 9, 10, 14])
        self.assertEqual(bt.preorder_traversal(), [8, 3, 1, 6, 10, 9, 14])
        self.assertEqual(bt.postorder_traversal(), [1, 6, 3, 9, 14, 10, 8])

    def test_left_heavy_tree(self):
        bt = BinaryTree()
        for i in range(10, 0, -1):  # Inserts 10, 9, ..., 1
            bt.insert(i)
        self.assertEqual(bt.inorder_traversal(), [i for i in range(1, 11)])
        self.assertEqual(bt.preorder_traversal(), [10-i for i in range(10)])
        self.assertEqual(bt.postorder_traversal(), [i for i in range(1, 11)])

    def test_right_heavy_tree(self):
        bt = BinaryTree()
        for i in range(1, 11):  # Inserts 1, 2, ..., 10
            bt.insert(i)
        self.assertEqual(bt.inorder_traversal(), [i for i in range(1, 11)])
        self.assertEqual(bt.preorder_traversal(), [i for i in range(1, 11)])
        self.assertEqual(bt.postorder_traversal(), [i for i in range(10, 0, -1)])
if __name__ == '__main__':
    unittest.main()