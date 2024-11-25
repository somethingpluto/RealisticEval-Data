package org.real.temp;

public class Answer {

    /**
     * Determines if two values are siblings in a binary tree represented as an array.
     * 
     * @param tree the binary tree level-order representation
     * @param val1 the first value to check for sibling relationship
     * @param val2 the second value to check for sibling relationship
     * @return true if val1 and val2 are siblings, false otherwise
     */
    public static boolean areSiblings(int[] tree, int val1, int val2) {
        if (val1 == val2) {
            return false;  // A node cannot be a sibling to itself
        }

        int index1 = findIndex(tree, val1);
        int index2 = findIndex(tree, val2);

        // Check if one of the values is not in the tree
        if (index1 == -1 || index2 == -1) {
            return false;
        }

        // Check if they have the same parent
        return (index1 - 1) / 2 == (index2 - 1) / 2 && index1 != index2;
    }

    /**
     * Helper method to find the index of a value in the tree array.
     * 
     * @param tree the binary tree level-order representation
     * @param value the value to find
     * @return the index of the value, or -1 if not found
     */
    private static int findIndex(int[] tree, int value) {
        for (int i = 0; i < tree.length; i++) {
            if (tree[i] == value) {
                return i;
            }
        }
        return -1;  // Value not found
    }

    public static void main(String[] args) {
        int[] tree = {1, 2, 3, 4, 5, 6, 7};
        System.out.println(areSiblings(tree, 4, 5));  // Expected output: true
        System.out.println(areSiblings(tree, 2, 3));  // Expected output: true
        System.out.println(areSiblings(tree, 1, 2));  // Expected output: false
    }
}