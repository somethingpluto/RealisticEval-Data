package org.real.temp;

import java.util.Set;
import java.util.TreeSet;
import java.util.Arrays;

public class Answer {

    /**
     * Compares two sets of floats for equality within a relative and absolute tolerance.
     *
     * @param set1 The first set of floats.
     * @param set2 The second set of floats.
     * @param rtol The relative tolerance (default: 1e-5).
     * @param atol The absolute tolerance (default: 1e-6).
     * @return True if the sets are equal within the specified tolerances, False otherwise.
     */
    public static boolean areSetsEqual(Set<Double> set1, Set<Double> set2, double rtol, double atol) {
        // Convert sets to sorted lists for comparison
        TreeSet<Double> sortedSet1 = new TreeSet<>(set1);
        TreeSet<Double> sortedSet2 = new TreeSet<>(set2);

        // Check if the lengths of both sets are the same
        if (sortedSet1.size() != sortedSet2.size()) {
            return false;
        }

        // Compare each element in the two sorted sets
        Double[] list1 = sortedSet1.toArray(new Double[0]);
        Double[] list2 = sortedSet2.toArray(new Double[0]);

        for (int i = 0; i < list1.length; i++) {
            if (!isClose(list1[i], list2[i], rtol, atol)) {
                return false;
            }
        }

        return true;
    }

    private static boolean isClose(double a, double b, double rtol, double atol) {
        return Math.abs(a - b) <= Math.max(rtol * Math.max(Math.abs(a), Math.abs(b)), atol);
    }

    public static void main(String[] args) {
        Set<Double> set1 = new TreeSet<>(Arrays.asList(1.0, 2.0, 3.0));
        Set<Double> set2 = new TreeSet<>(Arrays.asList(1.0, 2.0, 3.0));

        System.out.println(areSetsEqual(set1, set2, 1e-5, 1e-6)); // Should print true
    }
}