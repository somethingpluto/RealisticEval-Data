package org.real.temp;

public class Answer {

    /**
     * Determines if two rectangles intersect horizontally.
     * 
     * Each rectangle is defined by an array [x1, y1, x2, y2], where:
     * - [x1, y1] are the coordinates of the bottom-left corner.
     * - [x2, y2] are the coordinates of the top-right corner.
     * 
     * @param rect1 The first rectangle defined by [x1, y1, x2, y2].
     * @param rect2 The second rectangle defined by [x1, y1, x2, y2].
     * @return true if the rectangles intersect horizontally, false otherwise.
     */
    public static boolean intersectHorizontally(int[] rect1, int[] rect2) {
        return !(rect1[2] < rect2[0] || rect2[2] < rect1[0]);
    }

    // Example usage
    public static void main(String[] args) {
        int[] rect1 = {1, 1, 3, 3};
        int[] rect2 = {2, 2, 4, 4};
        
        System.out.println(intersectHorizontally(rect1, rect2)); // Expected output: true
    }
}