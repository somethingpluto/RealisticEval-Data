package org.real.temp;

import java.util.ArrayList;
import java.util.List;

// Define the TreeNode class
public class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    // Constructor for TreeNode
    public TreeNode(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// Define the BinaryTree class
public class BinaryTree {
    TreeNode root;

    // Constructor for BinaryTree
    public BinaryTree(TreeNode root) {
        this.root = root;
    }

    // Method to perform preorder traversal
    public List<Integer> preorderTraversal(TreeNode node) {
        List<Integer> result = new ArrayList<>();
        preorderHelper(node, result);
        return result;
    }

    // Helper method for preorder traversal
    private void preorderHelper(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        result.add(node.value);
        preorderHelper(node.left, result);
        preorderHelper(node.right, result);
    }

    // Method to perform inorder traversal
    public List<Integer> inorderTraversal(TreeNode node) {
        List<Integer> result = new ArrayList<>();
        inorderHelper(node, result);
        return result;
    }

    // Helper method for inorder traversal
    private void inorderHelper(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        inorderHelper(node.left, result);
        result.add(node.value);
        inorderHelper(node.right, result);
    }

    // Method to perform postorder traversal
    public List<Integer> postorderTraversal(TreeNode node) {
        List<Integer> result = new ArrayList<>();
        postorderHelper(node, result);
        return result;
    }

    // Helper method for postorder traversal
    private void postorderHelper(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        postorderHelper(node.left, result);
        postorderHelper(node.right, result);
        result.add(node.value);
    }
}