package org.real.temp;

public class Answer {
    public static double calculateSteeringAngle(double angularVelocity, double speed, double wheelbase) {
        // Check for valid speed
        if (speed <= 0) {
            throw new IllegalArgumentException("Speed must be greater than zero.");
        }

        // Calculate steering angle in radians
        double steeringAngle = Math.atan((angularVelocity * wheelbase) / speed);
        
        return steeringAngle; // Returns the steering angle in radians
    }
}