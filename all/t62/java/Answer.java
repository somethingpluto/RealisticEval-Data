package org.real.temp;

public class Answer {
    // Inner class representing a tree node
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int key) {
            this.val = key;
            this.left = null;
            this.right = null;
        }
    }

    // Class representing the binary tree
    public static class BinaryTree {
        private TreeNode root;

        public BinaryTree() {
            this.root = null;
        }

        // Public method to insert a new key into the binary tree
        public void insert(int key) {
            if (this.root == null) {
                this.root = new TreeNode(key);
            } else {
                this._insert(this.root, key);
            }
        }

        // Private recursive method to insert a new key into the binary tree
        private void _insert(TreeNode node, int key) {
            if (key < node.val) {
                if (node.left == null) {
                    node.left = new TreeNode(key);
                } else {
                    this._insert(node.left, key);
                }
            } else if (key > node.val) {
                if (node.right == null) {
                    node.right = new TreeNode(key);
                } else {
                    this._insert(node.right, key);
                }
            }
        }

        // Public method to perform an inorder traversal of the binary tree
        public List<Integer> inorderTraversal() {
            List<Integer> result = new ArrayList<>();
            this._inorderTraversal(this.root, result);
            return result;
        }

        // Private recursive method to perform an inorder traversal of the binary tree
        private void _inorderTraversal(TreeNode node, List<Integer> result) {
            if (node != null) {
                this._inorderTraversal(node.left, result);
                result.add(node.val);
                this._inorderTraversal(node.right, result);
            }
        }

        // Public method to perform a preorder traversal of the binary tree
        public List<Integer> preorderTraversal() {
            List<Integer> result = new ArrayList<>();
            this._preorderTraversal(this.root, result);
            return result;
        }

        // Private recursive method to perform a preorder traversal of the binary tree
        private void _preorderTraversal(TreeNode node, List<Integer> result) {
            if (node != null) {
                result.add(node.val);
                this._preorderTraversal(node.left, result);
                this._preorderTraversal(node.right, result);
            }
        }

        // Public method to perform a postorder traversal of the binary tree
        public List<Integer> postorderTraversal() {
            List<Integer> result = new ArrayList<>();
            this._postorderTraversal(this.root, result);
            return result;
        }

        // Private recursive method to perform a postorder traversal of the binary tree
        private void _postorderTraversal(TreeNode node, List<Integer> result) {
            if (node != null) {
                this._postorderTraversal(node.left, result);
                this._postorderTraversal(node.right, result);
                result.add(node.val);
            }
        }
    }
}