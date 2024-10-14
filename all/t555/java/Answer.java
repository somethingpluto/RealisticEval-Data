package org.real.temp;

public class Answer {

    /**
     * Converts a quaternion to a rotation angle in radians.
     *
     * @param quaternion An array containing the quaternion components (w, x, y, z)
     * @return The rotation angle in radians
     */
    public static double quaternionToAngle(double[] quaternion) {
        // Ensure the quaternion is a valid 4-element array
        if (quaternion == null || quaternion.length != 4) {
            throw new IllegalArgumentException("Quaternion must have 4 components (w, x, y, z)");
        }

        double w = quaternion[0];
        double x = quaternion[1];
        double y = quaternion[2];
        double z = quaternion[3];

        // Calculate the angle in radians
        double angle = 2 * Math.acos(w);

        return angle;
    }

    public static void main(String[] args) {
        // Example usage
        double[] quaternion = {0.707, 0.0, 0.0, 0.707};
        double angle = quaternionToAngle(quaternion);
        System.out.println("Rotation angle in radians: " + angle);
    }
}