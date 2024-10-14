package org.real.temp;

public class Answer {

    /**
     * Convert an angle from degrees to radians.
     *
     * @param degrees The angle in degrees to convert.
     * @return The angle in radians.
     */
    public static double degreesToRadians(double degrees) {
        double radians = degrees * (Math.PI / 180);
        return radians;
    }

    // A simple check function to verify the correctness of the conversion
    public static void main(String[] args) {
        double degrees = 90; // Example angle in degrees
        double radians = degreesToRadians(degrees);
        System.out.println("Degrees: " + degrees + ", Radians: " + radians);
    }
}