package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class Tester {

    @Test
    public void testCreate2x2MatrixFilledWithZeros() {
        Object[][] result = MatrixCreator.createMatrix(2, 2, 0);
        assertArrayEquals(new Object[][]{{0, 0}, {0, 0}}, result);
    }

    @Test
    public void testCreate3x3MatrixFilledWithOnes() {
        Object[][] result = MatrixCreator.createMatrix(3, 3, 1);
        assertArrayEquals(new Object[][]{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}}, result);
    }

    @Test
    public void testCreate4x5MatrixFilledWithString() {
        Object[][] result = MatrixCreator.createMatrix(4, 5, "test");
        assertArrayEquals(new Object[][]{
            {"test", "test", "test", "test", "test"},
            {"test", "test", "test", "test", "test"},
            {"test", "test", "test", "test", "test"},
            {"test", "test", "test", "test", "test"},
        }, result);
    }

    @Test
    public void testCreate0x0Matrix() {
        Object[][] result = MatrixCreator.createMatrix(0, 0, null);
        assertArrayEquals(new Object[0][0], result);
    }

    @Test
    public void testCreate1x1MatrixWithBoolean() {
        Object[][] result = MatrixCreator.createMatrix(1, 1, true);
        assertArrayEquals(new Object[][]{{true}}, result);
    }

    @Test
    public void testCreate5x5MatrixFilledWithNegativeNumbers() {
        Object[][] result = MatrixCreator.createMatrix(5, 5, -1);
        assertArrayEquals(new Object[][]{
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
        }, result);
    }
}