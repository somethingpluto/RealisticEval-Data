package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

public class Tester {

    private BinaryTree binaryTree;

    @Before
    public void setUp() {
        binaryTree = new BinaryTree();
    }

    @Test
    public void testInsert() {
        binaryTree.insert(10);
        binaryTree.insert(5);
        binaryTree.insert(15);

        assertEquals(Integer.valueOf(10), binaryTree.root.val);
        assertEquals(Integer.valueOf(5), binaryTree.root.left.val);
        assertEquals(Integer.valueOf(15), binaryTree.root.right.val);
    }

    @Test
    public void testInorderTraversal() {
        binaryTree.insert(10);
        binaryTree.insert(5);
        binaryTree.insert(15);
        binaryTree.insert(3);
        binaryTree.insert(7);
        binaryTree.insert(12);
        binaryTree.insert(18);

        List<Integer> expected = Arrays.asList(3, 5, 7, 10, 12, 15, 18);
        List<Integer> actual = binaryTree.inorderTraversal();

        assertEquals(expected, actual);
    }

    @Test
    public void testPreorderTraversal() {
        binaryTree.insert(10);
        binaryTree.insert(5);
        binaryTree.insert(15);
        binaryTree.insert(3);
        binaryTree.insert(7);
        binaryTree.insert(12);
        binaryTree.insert(18);

        List<Integer> expected = Arrays.asList(10, 5, 3, 7, 15, 12, 18);
        List<Integer> actual = binaryTree.preorderTraversal();

        assertEquals(expected, actual);
    }

    @Test
    public void testPostorderTraversal() {
        binaryTree.insert(10);
        binaryTree.insert(5);
        binaryTree.insert(15);
        binaryTree.insert(3);
        binaryTree.insert(7);
        binaryTree.insert(12);
        binaryTree.insert(18);

        List<Integer> expected = Arrays.asList(3, 7, 5, 12, 18, 15, 10);
        List<Integer> actual = binaryTree.postorderTraversal();

        assertEquals(expected, actual);
    }
}