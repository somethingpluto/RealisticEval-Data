package org.real.temp;

import java.util.List;
import java.util.ArrayList;

public class Answer {

    /**
     * Sorts the given list of integers using the Bubble Sort algorithm.
     *
     * @param arr A list of integers to be sorted.
     */
    public static void bubbleSort(List<Integer> arr) {
        boolean swapped;
        int n = arr.size();
        do {
            swapped = false;
            for (int i = 1; i < n; i++) {
                if (arr.get(i - 1) > arr.get(i)) {
                    // Swap arr[i - 1] and arr[i]
                    int temp = arr.get(i - 1);
                    arr.set(i - 1, arr.get(i));
                    arr.set(i, temp);
                    swapped = true;
                }
            }
            n--; // Reduce the range of comparison, as the last element is now sorted
        } while (swapped);
    }

    public static void main(String[] args) {
        // Example usage
        List<Integer> array = new ArrayList<>();
        array.add(64);
        array.add(34);
        array.add(25);
        array.add(12);
        array.add(22);
        array.add(11);
        array.add(90);

        System.out.println("Original array: " + array);
        bubbleSort(array);
        System.out.println("Sorted array: " + array);
    }
}