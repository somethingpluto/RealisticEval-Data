package org.real.temp;

public class Answer {

    /**
     * Convert an angle from radians to degrees.
     *
     * @param radians The angle in radians to convert.
     * @return The angle in degrees.
     */
    public static double radiansToDegrees(double radians) {
        double degrees = radians * (180 / Math.PI);
        return degrees;
    }

    // Example usage
    public static void main(String[] args) {
        double radians = Math.PI / 4; // 45 degrees in radians
        double degrees = radiansToDegrees(radians);
        System.out.println("Radians: " + radians + ", Degrees: " + degrees);
    }
}