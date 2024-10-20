package org.real.temp;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;
public class Tester {
    @Test
    public void testPointOnLine() {
        int[] A = {0, 0};
        int[] B = {10, 10};
        int[] C = {5, 5};
        assertTrue(isPointOnLine(A, B, C));
    }

    @Test
    public void testPointNotOnLine() {
        int[] A = {0, 0};
        int[] B = {10, 10};
        int[] C = {5, 6};
        assertFalse(isPointOnLine(A, B, C));
    }

    @Test
    public void testVerticalLine() {
        int[] A = {5, 0};
        int[] B = {5, 10};
        int[] C = {5, 5};
        assertTrue(isPointOnLine(A, B, C));
    }

    @Test
    public void testHorizontalLine() {
        int[] A = {0, 5};
        int[] B = {10, 5};
        int[] C = {5, 5};
        assertTrue(isPointOnLine(A, B, C));
    }

    @Test
    public void testPointNotOnVerticalLine() {
        int[] A = {5, 0};
        int[] B = {5, 10};
        int[] C = {6, 5};
        assertFalse(isPointOnLine(A, B, C));
    }
}