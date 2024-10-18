package org.real.temp;

public class Answer {

    /**
     * Determine if two rectangles intersect vertically.
     *
     * Each rectangle is defined by an array [x1, y1, x2, y2], where:
     * - [x1, y1] are the coordinates of the bottom-left corner.
     * - [x2, y2] are the coordinates of the top-right corner.
     *
     * @param rect1 The first rectangle defined by [x1, y1, x2, y2].
     * @param rect2 The second rectangle defined by [x1, y1, x2, y2].
     * @return True if the rectangles intersect vertically, False otherwise.
     */
    public static boolean intersectVertically(int[] rect1, int[] rect2) {
        return !(rect1[3] < rect2[1] || rect2[3] < rect1[1]);
    }

    // Example usage
    public static void main(String[] args) {
        int[] rect1 = {1, 2, 3, 4};
        int[] rect2 = {0, 3, 5, 6};

        System.out.println(intersectVertically(rect1, rect2)); // Expected output: true
    }
}