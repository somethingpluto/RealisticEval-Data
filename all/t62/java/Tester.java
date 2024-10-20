package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for BinaryTree operations.
 */
public class Tester {

    @Test
    public void testEmptyTree() {
        BinaryTree bt = new BinaryTree();
        assertArrayEquals(new int[]{}, bt.inorderTraversal());
        assertArrayEquals(new int[]{}, bt.preorderTraversal());
        assertArrayEquals(new int[]{}, bt.postorderTraversal());
    }

    @Test
    public void testSingleNodeTree() {
        BinaryTree bt = new BinaryTree();
        bt.insert(10);
        assertArrayEquals(new int[]{10}, bt.inorderTraversal());
        assertArrayEquals(new int[]{10}, bt.preorderTraversal());
        assertArrayEquals(new int[]{10}, bt.postorderTraversal());
    }

    @Test
    public void testBalancedTree() {
        BinaryTree bt = new BinaryTree();
        int[] elements = {8, 3, 10, 1, 6, 9, 14};
        for (int elem : elements) {
            bt.insert(elem);
        }
        assertArrayEquals(new int[]{1, 3, 6, 8, 9, 10, 14}, bt.inorderTraversal());
        assertArrayEquals(new int[]{8, 3, 1, 6, 10, 9, 14}, bt.preorderTraversal());
        assertArrayEquals(new int[]{1, 6, 3, 9, 14, 10, 8}, bt.postorderTraversal());
    }

    @Test
    public void testLeftHeavyTree() {
        BinaryTree bt = new BinaryTree();
        for (int i = 10; i > 0; i--) {
            bt.insert(i);
        }
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, bt.inorderTraversal());
        assertArrayEquals(new int[]{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}, bt.preorderTraversal());
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, bt.postorderTraversal());
    }

    @Test
    public void testRightHeavyTree() {
        BinaryTree bt = new BinaryTree();
        for (int i = 1; i <= 10; i++) {
            bt.insert(i);
        }
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, bt.inorderTraversal());
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, bt.preorderTraversal());
        assertArrayEquals(new int[]{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}, bt.postorderTraversal());
    }
}