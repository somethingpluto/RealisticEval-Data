package org.real.temp;

public class Answer {

    // Method to perform insertion sort
    public static void insertionSort(double[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            // Current element to be inserted into sorted portion
            double key = arr[i];
            int j = i - 1;

            // Move elements of arr[0..i-1] that are greater than key
            // to one position ahead of their current position
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    // Method to display the array (optional for testing purposes)
    public static void show(double[] arr) {
        for (double element : arr) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    // Main method to test the insertionSort function
    public static void main(String[] args) {
        double[] arr = {12.4, 11.2, 13.5, 5.6, 6.7};

        System.out.println("Original array:");
        show(arr);

        // Perform insertion sort
        insertionSort(arr);

        System.out.println("Sorted array:");
        show(arr);
    }
}
