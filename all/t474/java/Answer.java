package org.real.temp;

import java.util.List;

public class Answer {

    /**
     * Determines if two values are siblings in a binary tree represented as an array.
     *
     * @param tree the binary tree level-order representation
     * @param val1 the first value to check for sibling relationship
     * @param val2 the second value to check for sibling relationship
     * @return true if val1 and val2 are siblings, false otherwise
     */
    public static boolean areSiblings(List<Integer> tree, int val1, int val2) {
        // Find parent indices
        int idx1 = findParentIndex(tree, val1);
        int idx2 = findParentIndex(tree, val2);

        // If parents are same, they are siblings
        return (idx1 != -1 && idx2 != -1 && idx1 == idx2);
    }

    private static int findParentIndex(List<Integer> tree, int val) {
        for (int i = 0; i < tree.size(); i++) {
            if ((2 * i + 1 <= tree.size() - 1 && tree.get(2 * i + 1) == val) ||
                    (2 * i + 2 <= tree.size() - 1 && tree.get(2 * i + 2) == val)) {
                return i;
            }
        }
        return -1; // Value not found or it's root
    }
}
