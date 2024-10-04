package org.real.temp;

public class Answer {

    /**
     * Performs binary search on a sorted array to find the index of a target value.
     *
     * @param array the sorted array to search
     * @param target the value to search for
     * @return the index of the target value if found, otherwise -1
     */
    public static int binarySearch(int[] array, int target) {
        int left = 0;                    // Starting index of the search range
        int right = array.length - 1;    // Ending index of the search range

        while (left <= right) {
            int mid = left + (right - left) / 2; // Calculate the mid index to avoid overflow

            // Check if the target is at mid
            if (array[mid] == target) {
                return mid;              // Target found, return index
            }
            // If target is greater, ignore left half
            else if (array[mid] < target) {
                left = mid + 1;          // Narrow search to the right half
            }
            // If target is smaller, ignore right half
            else {
                right = mid - 1;         // Narrow search to the left half
            }
        }

        return -1;                        // Target not found, return -1
    }
}