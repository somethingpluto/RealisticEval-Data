package org.real.temp;

public class Answer {

    /**
     * Calculate the Euclidean distance between two points in a 2D space.
     *
     * @param point1 The first point as an array of coordinates [x1, y1].
     * @param point2 The second point as an array of coordinates [x2, y2].
     * @return The Euclidean distance between the two points.
     */
    public static double calculateEuclideanDistance(double[] point1, double[] point2) {
        return Math.sqrt(Math.pow(point2[0] - point1[0], 2) + Math.pow(point2[1] - point1[1], 2));
    }
}