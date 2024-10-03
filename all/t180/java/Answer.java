package org.real.temp;

public class Answer {
    /**
     * Performs a binary search to find the index of the target value in a sorted array.
     * If the target value is not found, it returns the index of the closest value.
     *
     * @param array  The sorted array in which to search.
     * @param target The target value to search for.
     * @return The index of the target or the index of the closest value if the target is not found.
     */
    public static int binarySearchClosest(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (array[mid] == target) {
                return mid;
            } else if (array[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // After the loop, left is the first index greater than the target
        // and right is the last index less than the target
        if (left >= array.length) {
            return array.length - 1; // closest is the last element
        }
        if (right < 0) {
            return 0; // closest is the first element
        }

        // Check which is closer: array[left] or array[right]
        if (Math.abs(array[left] - target) < Math.abs(array[right] - target)) {
            return left;
        } else {
            return right;
        }
    }

    /**
     * Main method for testing the binarySearchClosest function.
     */
    public static void main(String[] args) {
        int[] array = {1, 3, 5, 7, 9, 11};
        int target = 8;

        int result = binarySearchClosest(array, target);
        System.out.println("Closest index: " + result + " (Value: " + array[result] + ")");
    }
}
