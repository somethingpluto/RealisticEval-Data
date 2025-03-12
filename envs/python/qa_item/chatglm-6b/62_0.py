
class BinaryTree:
    """
    implement the tree in the question structure and implement its three traversal methods
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        self._insert(self.root, key)
        self.root = TreeNode(key)

    def _insert(self, node, key):
        if node is None:
            return
        left = node.left
        right = node.right
        if key < left.val:
            left.left = self._insert(node.left, key)
        if key > right.val:
            right.right = self._insert(node.right, key)
        node.val = key

    def inorder_traversal(self):
        result = []
        for node in self.root.left.left.right:
            result.append(node.val)
        return result

    def _inorder_traversal(self, node, result):
        if node is None:
            return
        result.append(node.val)

    def preorder_traversal(self):
        result = []
        for node in self.root:
            result.append(node.val)
            if node.left:
                result.append(node.left.val)
            if node.right:
                result.append(node.right.val)

    def _preorder_traversal(self, node, result):
        if node is None:
            return
        result.append(node.val)

    def postorder_traversal(self):
        result = []
        for node in self.root:
            if node is None:
                continue
            result.append(node.val)
            if node.left:
                result.append(node.left.val)
            if node.right:
                result.append(node.right.val)

    def _postorder_traversal(self, node, result):
        if node is None:
            return
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