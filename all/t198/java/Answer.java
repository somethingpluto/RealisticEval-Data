package org.real.temp;

import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

/**
 * @brief Finds the maximum difference between elements in the array
 * such that the smaller element appears before the larger one.
 */
public class Answer {

    /**
     * Finds the maximum difference between elements in the list.
     *
     * @param l A list of integers containing the elements.
     * @return The maximum difference.
     */
    public static int findMaxDifference(List<Integer> l) {
        int minVal = l.get(0);
        int maxDiff = Integer.MIN_VALUE;

        for (int i = 1; i < l.size(); ++i) {
            maxDiff = Math.max(maxDiff, l.get(i) - minVal);
            minVal = Math.min(minVal, l.get(i));
        }

        return maxDiff;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> l = new ArrayList<>(n);
        
        for (int i = 0; i < n; ++i) {
            l.add(scanner.nextInt());
        }

        int maxDiff = findMaxDifference(l);
        System.out.println(maxDiff);
        
        scanner.close();
    }
}