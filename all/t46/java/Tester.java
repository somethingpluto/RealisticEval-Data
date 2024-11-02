package org.real.temp;

import org.junit.Before;

import java.util.ArrayList;
import java.util.List;
import org.real.temp.Answer.TreeNode;
import org.real.temp.Answer.BinaryTree;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Test class for BinaryTree operations.
 */
public class Tester {

    private BinaryTree tree;
    private BinaryTree emptyTree;

    @Before
    public void setUp() {
        // Tree structure:
        //      1
        //     / \
        //    2   3
        //   / \
        //  4   5
        tree = new Answer.BinaryTree(new TreeNode(1));
        tree.root.left = new Answer.TreeNode(2, new TreeNode(4), new TreeNode(5));
        tree.root.right = new TreeNode(3);

        emptyTree = new BinaryTree();

    }

    @Test
    public void testPreorderTraversal() {
        // Test preorder traversal
        List<Integer> result = new ArrayList<>();
        result = tree.preorderTraversal(tree.root,result);
        assertEquals("[1, 2, 4, 5, 3]", result.toString());
    }

    @Test
    public void testInorderTraversal() {
        // Test inorder traversal
        List<Integer> result = new ArrayList<>();

        result = tree.inorderTraversal(tree.root,result);
        assertEquals("[4, 2, 5, 1, 3]", result.toString());
    }

    @Test
    public void testPostorderTraversal() {
        List<Integer> result = new ArrayList<>();
        result = tree.postorderTraversal(tree.root,result);
        assertEquals("[4, 5, 2, 3, 1]", result.toString());
    }

    @Test
    public void testEmptyTree() {
        // Test traversals on an empty tree
        List<Integer> result = new ArrayList<>();
        assertEquals("[]", emptyTree.preorderTraversal(emptyTree.root,result).toString());
        assertEquals("[]", emptyTree.inorderTraversal(emptyTree.root,result).toString());
        assertEquals("[]", emptyTree.postorderTraversal(emptyTree.root,result).toString());
    }

}