package org.real.temp;

public class Answer {
    
    static class TreeNode {
        TreeNode left;
        TreeNode right;
        int val;

        public TreeNode(int key) {
            this.left = null;
            this.right = null;
            this.val = key;
        }
    }

    private TreeNode root;

    public Answer() {
        this.root = null;
    }

    public void insert(int key) {
        if (this.root == null) {
            this.root = new TreeNode(key);
        } else {
            insertRecursive(this.root, key);
        }
    }

    private void insertRecursive(TreeNode node, int key) {
        if (key < node.val) {
            if (node.left == null) {
                node.left = new TreeNode(key);
            } else {
                insertRecursive(node.left, key);
            }
        } else {
            if (node.right == null) {
                node.right = new TreeNode(key);
            } else {
                insertRecursive(node.right, key);
            }
        }
    }

    public int[] inorderTraversal() {
        return inorderTraversalRecursive(this.root, new java.util.ArrayList<Integer>()).stream().mapToInt(i -> i).toArray();
    }

    private java.util.List<Integer> inorderTraversalRecursive(TreeNode node, java.util.List<Integer> result) {
        if (node != null) {
            inorderTraversalRecursive(node.left, result);
            result.add(node.val);
            inorderTraversalRecursive(node.right, result);
        }
        return result;
    }

    public int[] preorderTraversal() {
        return preorderTraversalRecursive(this.root, new java.util.ArrayList<Integer>()).stream().mapToInt(i -> i).toArray();
    }

    private java.util.List<Integer> preorderTraversalRecursive(TreeNode node, java.util.List<Integer> result) {
        if (node != null) {
            result.add(node.val);
            preorderTraversalRecursive(node.left, result);
            preorderTraversalRecursive(node.right, result);
        }
        return result;
    }

    public int[] postorderTraversal() {
        return postorderTraversalRecursive(this.root, new java.util.ArrayList<Integer>()).stream().mapToInt(i -> i).toArray();
    }

    private java.util.List<Integer> postorderTraversalRecursive(TreeNode node, java.util.List<Integer> result) {
        if (node != null) {
            postorderTraversalRecursive(node.left, result);
            postorderTraversalRecursive(node.right, result);
            result.add(node.val);
        }
        return result;
    }
}