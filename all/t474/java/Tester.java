package org.real.temp;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.real.temp.Answer.*;
public class Tester {

    private int[] tree;

    @Before
    public void setUp() {
        // Setting up a binary tree used for all the test cases
        tree = new int[]{1, 2, 3, 4, 5, 6, 7};
    }

    @Test
    public void testBasicCase() {
        // Test with nodes 4 and 5, which are siblings
        boolean result = areSiblings(tree, 4, 5);
        assertTrue(result);
    }

    @Test
    public void testNonSiblingCase() {
        // Test with nodes 4 and 6, which are not siblings
        boolean result = areSiblings(tree, 4, 6);
        assertFalse(result);
    }


    @Test
    public void testNonExistentValues() {
        // Test with non-existent values
        boolean result = areSiblings(tree, 8, 9);
        assertFalse(result);
    }

    @Test
    public void testSameNodeCase() {
        // Test with the same node for both values
        boolean result = areSiblings(tree, 4, 4);
        assertFalse(result);
    }
}