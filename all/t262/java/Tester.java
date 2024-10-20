package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
/**
 * Test cases for the averageOfLevels method.
 */
public class Tester {

    private static final double DELTA = 0.01;


    @Test
    public void testEmptyTree() {
        TreeNode root = null;
        List<Double> expected = Arrays.asList();
        assertEquals(expected, averageOfLevels(root));
    }

    @Test
    public void testSingleNodeTree() {
        TreeNode root = new TreeNode(5);
        List<Double> expected = Arrays.asList(5.0);
        assertEquals(expected, averageOfLevels(root));
    }

    @Test
    public void testBalancedTreeTwoLevels() {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        List<Double> expected = Arrays.asList(3.0, 14.5);
        assertEquals(expected, averageOfLevels(root));
    }

    @Test
    public void testUnbalancedTree() {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.right = new TreeNode(3);
        List<Double> expected = Arrays.asList(1.0, 2.0, 3.0);
        assertEquals(expected, averageOfLevels(root));
    }

    @Test
    public void testTreeMultipleLevels() {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(8);
        List<Double> expected = Arrays.asList(1.0, 2.5, 5.67);
        List<Double> result = averageOfLevels(root);
        assertEquals(expected.subList(0, 2), result.subList(0, 2));
        assertTrue(Math.abs(result.get(2) - expected.get(2)) <= DELTA);
    }
}