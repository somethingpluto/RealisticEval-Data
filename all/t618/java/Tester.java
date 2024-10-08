package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    private static final double DELTA = 1e-6;

    @Test
    public void testRotation90DegreesXToY() {
        double[] from = {1, 0, 0};
        double[] to = {0, 1, 0};
        double[][] expected = {{0, -1, 0}, {1, 0, 0}, {0, 0, 1}};
        double[][] result = Answer.calculateRotationMatrix(from, to);
        assertMatrixEquals(expected, result, DELTA);
    }

    @Test
    public void testRotation180DegreesXToMinusX() {
        double[] from = {1, 0, 0};
        double[] to = {-1, 0, 0};
        double[][] expected = {{-1, 0, 0}, {0, -1, 0}, {0, 0, 1}};
        double[][] result = Answer.calculateRotationMatrix(from, to);
        assertMatrixEquals(expected, result, DELTA);
    }

    @Test
    public void testNoRotation() {
        double[] from = {1, 2, 3};
        double[] to = {1, 2, 3};
        double[][] expected = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        double[][] result = Answer.calculateRotationMatrix(from, to);
        assertMatrixEquals(expected, result, DELTA);
    }

    @Test
    public void testRotationNullVectors() {
        double[] from = null;
        double[] to = null;
        assertThrows(NullPointerException.class, () -> Answer.calculateRotationMatrix(from, to));
    }

    @Test
    public void testRotationWithZeroVector() {
        double[] from = {0, 0, 0};
        double[] to = {1, 0, 0};
        assertThrows(ArithmeticException.class, () -> Answer.calculateRotationMatrix(from, to));
    }

    @Test
    public void testRotationFromZToX() {
        double[] from = {0, 0, 1};
        double[] to = {1, 0, 0};
        double[][] expected = {{0, -1, 0}, {1, 0, 0}, {0, 0, 1}};
        double[][] result = Answer.calculateRotationMatrix(from, to);
        assertMatrixEquals(expected, result, DELTA);
    }

    @Test
    public void testArbitraryRotation() {
        double[] from = {1, 0, 0};
        double[] to = {0, 0, 1};
        double[][] expected = {{0, 0, 1}, {0, 1, 0}, {-1, 0, 0}};
        double[][] result = Answer.calculateRotationMatrix(from, to);
        assertMatrixEquals(expected, result, DELTA);
    }

    private void assertMatrixEquals(double[][] expected, double[][] actual, double delta) {
        for (int i = 0; i < expected.length; i++) {
            assertArrayEquals(expected[i], actual[i], delta, "Matrix rows do not match!");
        }
    }
}
