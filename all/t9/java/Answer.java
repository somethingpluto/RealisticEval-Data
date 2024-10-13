package org.real.temp;

public class Answer {

    /**
     * Check whether point C is on the line formed by points A and B.
     * 
     * @param A point A coordinates (x, y)
     * @param B point B coordinates (x, y)
     * @param C point C coordinates (x, y)
     * @return true if point C is on the line formed by A and B, false otherwise
     */
    public static boolean isPointOnLine(int[] A, int[] B, int[] C) {
        int xA = A[0];
        int yA = A[1];
        int xB = B[0];
        int yB = B[1];
        int xC = C[0];
        int yC = C[1];

        // Handle the vertical line case where the x-coordinates of points A and B are the same
        if (xA == xB) {
            return xC == xA;  // C must also have the same x-coordinate
        }

        // Calculate slopes using the formula (y2 - y1) / (x2 - x1)
        // Check if slopes of AC and BC are equal
        return (yC - yA) * (xB - xA) == (yB - yA) * (xC - xA);
    }

    public static void main(String[] args) {
        // Example usage
        int[] A = {1, 2};
        int[] B = {4, 6};
        int[] C = {2, 4};

        System.out.println(isPointOnLine(A, B, C));  // Output: true or false based on the points
    }
}