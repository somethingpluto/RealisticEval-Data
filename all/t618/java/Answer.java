package org.real.temp;

public class Answer {

    public static double[][] calculateRotationMatrix(Vec3 originalVector, Vec3 targetVector) {
        // Step 1: Normalize the input vectors
        Vec3 original = originalVector.normalize();
        Vec3 target = targetVector.normalize();

        // Step 2: Calculate the Axis of Rotation using the cross product
        Vec3 axis = original.cross(target).normalize();

        // Step 3: Calculate the Angle of Rotation
        double angle = Math.acos(original.dot(target));

        // Step 4: Construct the Rotation Matrix
        return calculateRotationMatrix(axis, angle);
    }

    private static double[][] calculateRotationMatrix(Vec3 axis, double angle) {
        double cosTheta = Math.cos(angle);
        double sinTheta = Math.sin(angle);
        double oneMinusCos = 1 - cosTheta;

        double x = axis.getX();
        double y = axis.getY();
        double z = axis.getZ();

        // Creating the rotation matrix using Rodrigues' rotation formula
        return new double[][]{
            {cosTheta + x * x * oneMinusCos, x * y * oneMinusCos - z * sinTheta, x * z * oneMinusCos + y * sinTheta},
            {y * x * oneMinusCos + z * sinTheta, cosTheta + y * y * oneMinusCos, y * z * oneMinusCos - x * sinTheta},
            {z * x * oneMinusCos - y * sinTheta, z * y * oneMinusCos + x * sinTheta, cosTheta + z * z * oneMinusCos}
        };
    }
}

class Vec3 {
    private double x, y, z;

    public Vec3(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getZ() {
        return z;
    }

    public Vec3 normalize() {
        double length = length();
        return new Vec3(x / length, y / length, z / length);
    }

    public double length() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public double dot(Vec3 other) {
        return this.x * other.x + this.y * other.y + this.z * other.z;
    }

    public Vec3 cross(Vec3 other) {
        return new Vec3(
            this.y * other.z - this.z * other.y,
            this.z * other.x - this.x * other.z,
            this.x * other.y - this.y * other.x
        );
    }
}