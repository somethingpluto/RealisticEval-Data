package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Tester {

    private BinaryTree binaryTree;

    @BeforeEach
    public void setUp() {
        binaryTree = new BinaryTree();
    }

    @Test
    public void testPreorderTraversal() {
        // Create a sample binary tree for testing
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);

        root.left = node2;
        root.right = node3;
        node2.left = node4;
        node2.right = node5;

        // Expected result of preorder traversal: [1, 2, 4, 5, 3]
        List<Integer> expectedResult = Arrays.asList(1, 2, 4, 5, 3);
        List<Integer> actualResult = new ArrayList<>();
        binaryTree.preorderTraversal(root, actualResult);

        assertEquals(expectedResult, actualResult);
    }

    @Test
    public void testInorderTraversal() {
        // Create a sample binary tree for testing
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);

        root.left = node2;
        root.right = node3;
        node2.left = node4;
        node2.right = node5;

        // Expected result of inorder traversal: [4, 2, 5, 1, 3]
        List<Integer> expectedResult = Arrays.asList(4, 2, 5, 1, 3);
        List<Integer> actualResult = new ArrayList<>();
        binaryTree.inorderTraversal(root, actualResult);

        assertEquals(expectedResult, actualResult);
    }

    @Test
    public void testPostorderTraversal() {
        // Create a sample binary tree for testing
        TreeNode root = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);

        root.left = node2;
        root.right = node3;
        node2.left = node4;
        node2.right = node5;

        // Expected result of postorder traversal: [4, 5, 2, 3, 1]
        List<Integer> expectedResult = Arrays.asList(4, 5, 2, 3, 1);
        List<Integer> actualResult = new ArrayList<>();
        binaryTree.postorderTraversal(root, actualResult);

        assertEquals(expectedResult, actualResult);
    }
}

// TreeNode class
class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    TreeNode(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// BinaryTree class
class BinaryTree {
    TreeNode root;

    BinaryTree(TreeNode root) {
        this.root = root;
    }

    BinaryTree() {
        this(null);
    }

    void preorderTraversal(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        result.add(node.value);
        preorderTraversal(node.left, result);
        preorderTraversal(node.right, result);
    }

    void inorderTraversal(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        inorderTraversal(node.left, result);
        result.add(node.value);
        inorderTraversal(node.right, result);
    }

    void postorderTraversal(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        postorderTraversal(node.left, result);
        postorderTraversal(node.right, result);
        result.add(node.value);
    }
}