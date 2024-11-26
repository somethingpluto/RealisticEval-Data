package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the getScale function.
 */
public class Tester {

    /**
     * Test for the identity matrix (no scaling).
     */
    @Test
    public void testIdentityMatrix() {
        double[] matrix = {1, 0, 0, 0, 1, 0, 0, 0, 1};
        double[] expectedScale = {1.0, 1.0};
        double[] actualScale = getScale(matrix);
        assertEquals(expectedScale[0], actualScale[0], 0.001);
        assertEquals(expectedScale[1], actualScale[1], 0.001);
    }

    /**
     * Test for a scaling matrix (2x in x and 3x in y).
     */
    @Test
    public void testScalingMatrix() {
        double[] matrix = {2, 0, 0, 0, 3, 0, 0, 0, 1};
        double[] expectedScale = {2.0, 3.0};
        double[] actualScale = getScale(matrix);
        assertEquals(expectedScale[0], actualScale[0], 0.001);
        assertEquals(expectedScale[1], actualScale[1], 0.001);
    }

    /**
     * Test case with uniform scaling.
     */
    @Test
    public void testUniformScaling() {
        double[] matrix = {2, 0, 0, 0, 2, 0, 0, 0, 1};
        double[] expectedScale = {2.0, 2.0};
        double[] actualScale = getScale(matrix);
        assertEquals(expectedScale[0], actualScale[0], 0.001);
        assertEquals(expectedScale[1], actualScale[1], 0.001);
    }

    /**
     * Test case with non-uniform scaling.
     */
    @Test
    public void testNonUniformScaling() {
        double[] matrix = {3, 0, 0, 0, 5, 0, 0, 0, 1};
        double[] expectedScale = {3.0, 5.0};
        double[] actualScale = getScale(matrix);
        assertEquals(expectedScale[0], actualScale[0], 0.001);
        assertEquals(expectedScale[1], actualScale[1], 0.001);
    }

    /**
     * Test case with reflection matrix.
     */
    @Test
    public void testReflectionMatrix() {
        double[] matrix = {-1, 0, 0, 0, 1, 0, 0, 0, 1};
        double[] expectedScale = {1.0, 1.0};
        double[] actualScale = getScale(matrix);
        assertEquals(expectedScale[0], actualScale[0], 0.001);
        assertEquals(expectedScale[1], actualScale[1], 0.001);
    }
}