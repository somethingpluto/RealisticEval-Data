package org.real.temp;

public class Answer {

    /**
     * Check whether point C is on a line formed by two points A and B.
     *
     * @param A The coordinates of point A [x, y].
     * @param B The coordinates of point B [x, y].
     * @param C The coordinates of point C [x, y].
     * @return true if point C lies on the line formed by points A and B, false otherwise.
     */
    public static boolean isPointOnLine(int[] A, int[] B, int[] C) {
        // Calculate the area of the triangle ABC using the determinant method
        double area = 0.5 * Math.abs(
                A[0] * (B[1] - C[1]) +
                        B[0] * (C[1] - A[1]) +
                        C[0] * (A[1] - B[1])
        );

        // If the area is zero, then points A, B, and C are collinear
        return area == 0;
    }

    public static void main(String[] args) {
        // Example usage
        int[] A = {0, 0};
        int[] B = {4, 4};
        int[] C = {2, 2};

        boolean result = isPointOnLine(A, B, C);
        System.out.println("Is point C on line AB? " + result);
    }
}