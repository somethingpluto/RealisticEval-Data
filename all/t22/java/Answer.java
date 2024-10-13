package org.real.temp;

public class Answer {

    /**
     * Calculate the Euclidean distance between two points in a 2D space.
     *
     * @param point1 The first point as an array of coordinates [x1, y1].
     * @param point2 The second point as an array of coordinates [x2, y2].
     * @return The Euclidean distance between the two points.
     * @throws IllegalArgumentException If the inputs are not valid.
     */
    public static double calculateEuclideanDistance(double[] point1, double[] point2) throws IllegalArgumentException {
        // Validate input types
        if (point1 == null || point2 == null) {
            throw new IllegalArgumentException("Points cannot be null");
        }
        if (point1.length != 2 || point2.length != 2) {
            throw new IllegalArgumentException("Both points must have exactly two coordinates");
        }

        // Extract coordinates from the input arrays
        double x1 = point1[0];
        double y1 = point1[1];
        double x2 = point2[0];
        double y2 = point2[1];

        // Compute differences and Euclidean distance using the Pythagorean theorem
        double dx = x2 - x1;
        double dy = y2 - y1;

        return Math.sqrt(dx * dx + dy * dy);
    }

    public static void main(String[] args) {
        // Example usage
        double[] point1 = {1.0, 2.0};
        double[] point2 = {4.0, 6.0};

        try {
            double distance = calculateEuclideanDistance(point1, point2);
            System.out.println("The Euclidean distance is: " + distance);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}