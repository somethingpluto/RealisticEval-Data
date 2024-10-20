package org.real.temp;

public class Answer {

    /**
     * Compute the squared Euclidean distance between two vectors.
     *
     * @param vec1 First vector as an array of doubles.
     * @param vec2 Second vector as an array of doubles.
     * @return The squared Euclidean distance between vec1 and vec2 as a double.
     * @throws IllegalArgumentException If the vectors are of different lengths.
     */
    public static double squaredEuclideanDistance(double[] vec1, double[] vec2) {
        if (vec1.length != vec2.length) {
            throw new IllegalArgumentException("Vectors must be of the same length");
        }

        double distanceSquared = 0.0;
        for (int i = 0; i < vec1.length; i++) {
            distanceSquared += Math.pow(vec1[i] - vec2[i], 2);
        }
        return distanceSquared;
    }

    // A simple check function to verify the correctness of the squaredEuclideanDistance method.
    public static void main(String[] args) {
        double[] vec1 = {1.0, 2.0, 3.0};
        double[] vec2 = {4.0, 5.0, 6.0};
        double result = squaredEuclideanDistance(vec1, vec2);
        System.out.println("Squared Euclidean Distance: " + result); // Expected output: 27.0
    }
}