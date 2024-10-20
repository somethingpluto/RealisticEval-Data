package org.real.temp;

import org.junit.Before;
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
    private BinaryTree singleNodeTree;

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

        singleNodeTree = new BinaryTree(new TreeNode(10));
    }

    @Test
    public void testPreorderTraversal() {
        // Test preorder traversal
        List<Integer> result = tree.preorderTraversal(tree.root);
        assertEquals("[1, 2, 4, 5, 3]", result.toString());
    }

    @Test
    public void testInorderTraversal() {
        // Test inorder traversal
        List<Integer> result = tree.inorderTraversal(tree.root);
        assertEquals("[4, 2, 5, 1, 3]", result.toString());
    }

    @Test
    public void testPostorderTraversal() {
        // Test postorder traversal
        List<Integer> result = tree.postorderTraversal(tree.root);
        assertEquals("[4, 5, 2, 3, 1]", result.toString());
    }

    @Test
    public void testEmptyTree() {
        // Test traversals on an empty tree
        assertEquals("[]", emptyTree.preorderTraversal(emptyTree.root).toString());
        assertEquals("[]", emptyTree.inorderTraversal(emptyTree.root).toString());
        assertEquals("[]", emptyTree.postorderTraversal(emptyTree.root).toString());
    }

    @Test
    public void testSingleNodeTree() {
        // Test all traversals on a tree with only one node
        assertEquals("[10]", singleNodeTree.preorderTraversal(singleNodeTree.root).toString());
        assertEquals("[10]", singleNodeTree.inorderTraversal(singleNodeTree.root).toString());
        assertEquals("[10]", singleNodeTree.postorderTraversal(singleNodeTree.root).toString());
    }
}