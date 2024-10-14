package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testAreSiblings() {
        // Test data for a binary tree represented as an array
        int[] tree = {1, 2, 3, 4, 5, 6, 7};

        // Test cases
        assertTrue(areSiblings(tree, 4, 5)); // 4 and 5 are siblings
        assertFalse(areSiblings(tree, 2, 3)); // 2 and 3 are not siblings
        assertFalse(areSiblings(tree, 4, 7)); // 4 and 7 are not siblings
        assertFalse(areSiblings(tree, 8, 9)); // 8 and 9 do not exist in the tree
    }

    private boolean areSiblings(int[] tree, int val1, int val2) {
        int n = tree.length;

        // Find parent of val1
        int i = 0;
        while (i < n && tree[i] != val1) {
            i++;
        }
        int parentVal1 = -1;
        if (i < n) {
            parentVal1 = tree[(i - 1) / 2];
        }

        // Find parent of val2
        i = 0;
        while (i < n && tree[i] != val2) {
            i++;
        }
        int parentVal2 = -1;
        if (i < n) {
            parentVal2 = tree[(i - 1) / 2];
        }

        // Check if both nodes have the same parent
        return parentVal1 == parentVal2 && parentVal1 != -1;
    }
}
