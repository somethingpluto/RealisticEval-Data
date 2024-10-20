package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testDirectDifferenceNoWrapping() {
        Point thisPoint = new Point(2, 3);
        Point otherPoint = new Point(5, 6);
        double width = 10;
        double height = 10;
        double[] result = toroidalDiff(thisPoint, otherPoint, width, height);
        assertArrayEquals(new double[]{-3, -3}, result, 0.0001);
    }

    @Test
    public void testWrappingAroundXDimension() {
        Point thisPoint = new Point(9, 5);
        Point otherPoint = new Point(1, 5);
        double width = 10;
        double height = 10;
        double[] result = toroidalDiff(thisPoint, otherPoint, width, height);
        assertArrayEquals(new double[]{-2, 0}, result, 0.0001); // dx wraps around the toroidal boundary
    }

    @Test
    public void testWrappingAroundYDimension() {
        Point thisPoint = new Point(4, 9);
        Point otherPoint = new Point(4, 1);
        double width = 10;
        double height = 10;
        double[] result = toroidalDiff(thisPoint, otherPoint, width, height);
        assertArrayEquals(new double[]{0, -2}, result, 0.0001); // dy wraps around the toroidal boundary
    }

    @Test
    public void testWrappingAroundBothDimensions() {
        Point thisPoint = new Point(9, 9);
        Point otherPoint = new Point(1, 1);
        double width = 10;
        double height = 10;
        double[] result = toroidalDiff(thisPoint, otherPoint, width, height);
        assertArrayEquals(new double[]{-2, -2}, result, 0.0001); // Both dx and dy wrap around
    }

    @Test
    public void testSamePosition() {
        Point thisPoint = new Point(5, 5);
        Point otherPoint = new Point(5, 5);
        double width = 10;
        double height = 10;
        double[] result = toroidalDiff(thisPoint, otherPoint, width, height);
        assertArrayEquals(new double[]{0, 0}, result, 0.0001); // No difference
    }
}