package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Divide a list into n parts as evenly as possible. Excess elements are distributed to earlier sublists.
     *
     * @param lst The list to be divided.
     * @param n The number of parts to divide the list into.
     * @return A list containing n sublists, where each sublist represents a part of the original list.
     */
    public static List<List<Integer>> divideList(List<Integer> lst, int n) {
        // Total number of elements in the list
        int L = lst.size();
        // Calculate the size of each part
        int baseSize = L / n;
        // Calculate the number of sections that will have an additional element
        int remainder = L % n;

        List<List<Integer>> result = new ArrayList<>();
        // Start index of the sublist
        int startIndex = 0;

        for (int i = 0; i < n; i++) {
            // Determine the size of the current part
            int partSize = baseSize + (i < remainder ? 1 : 0);
            // Append the sublist to the result list
            result.add(new ArrayList<>(lst.subList(startIndex, startIndex + partSize)));
            // Update the start index for the next part
            startIndex += partSize;
        }

        return result;
    }

    public static void main(String[] args) {
        List<Integer> lst = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        int n = 3;
        List<List<Integer>> dividedList = divideList(lst, n);
        System.out.println(dividedList);
    }
}