package org.real.temp;

import java.util.List;

public class Answer {

    // Method to perform Hill sort (Shell sort)
    public static void hillSort(List<Integer> arr) {
        int n = arr.size();

        // Start with a large gap, then reduce the gap
        for (int gap = n / 2; gap > 0; gap /= 2) {
            // Do a gapped insertion sort for this gap size
            for (int i = gap; i < n; i++) {
                // Save the value to be inserted
                int temp = arr.get(i);
                int j;
                // Shift earlier gap-sorted elements up until the correct location for arr[i] is found
                for (j = i; j >= gap && arr.get(j - gap) > temp; j -= gap) {
                    arr.set(j, arr.get(j - gap));
                }
                // Put temp (the original arr[i]) in its correct location
                arr.set(j, temp);
            }
        }
    }
}