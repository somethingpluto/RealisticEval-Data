package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;

public class Tester {

    private static final double WHEELBASE = 2.5; // Setting wheelbase constant for all tests

    @Test
    public void testNormalCase() {
        double angularVelocity = 1.0; // radians/second
        double speed = 10.0;          // meters/second
        double expectedAngle = Math.atan((angularVelocity * WHEELBASE) / speed);
        assertEquals(expectedAngle, Answer.calculateSteeringAngle(angularVelocity, speed, WHEELBASE), 1e-9);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testZeroSpeed() {
        double angularVelocity = 1.0; // radians/second
        double speed = 0.0;           // meters/second
        Answer.calculateSteeringAngle(angularVelocity, speed, WHEELBASE);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNegativeSpeed() {
        double angularVelocity = 1.0; // radians/second
        double speed = -5.0;          // meters/second
        Answer.calculateSteeringAngle(angularVelocity, speed, WHEELBASE);
    }

    @Test
    public void testZeroAngularVelocity() {
        double angularVelocity = 0.0; // radians/second
        double speed = 10.0;          // meters/second
        double expectedAngle = 0.0;   // Steering angle should be zero
        assertEquals(expectedAngle, Answer.calculateSteeringAngle(angularVelocity, speed, WHEELBASE), 1e-9);
    }

    @Test
    public void testLargeValues() {
        double angularVelocity = 100.0; // radians/second
        double speed = 1000.0;          // meters/second
        double expectedAngle = Math.atan((angularVelocity * WHEELBASE) / speed);
        assertEquals(expectedAngle, Answer.calculateSteeringAngle(angularVelocity, speed, WHEELBASE), 1e-9);
    }

    @Test
    public void testHighAngularVelocity() {
        double angularVelocity = 10.0; // radians/second
        double speed = 1.0;             // meters/second
        double expectedAngle = Math.atan((angularVelocity * WHEELBASE) / speed);
        assertEquals(expectedAngle, Answer.calculateSteeringAngle(angularVelocity, speed, WHEELBASE), 1e-9);
    }
}