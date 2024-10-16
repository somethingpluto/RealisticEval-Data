package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testAddition() {
        assertEquals(7, Answer.applyOp(3, 4, '+'), 0);
        assertEquals(-2, Answer.applyOp(-1, -1, '+'), 0);
    }

    @Test
    public void testSubtraction() {
        assertEquals(5, Answer.applyOp(10, 5, '-'), 0);
        assertEquals(-5, Answer.applyOp(5, 10, '-'), 0);
    }

    @Test
    public void testMultiplication() {
        assertEquals(12, Answer.applyOp(3, 4, '*'), 0);
        assertEquals(-10, Answer.applyOp(-2, 5, '*'), 0);
    }

    @Test
    public void testDivision() {
        assertEquals(2, Answer.applyOp(8, 4, '/'), 0);
        assertEquals(2.5, Answer.applyOp(5, 2, '/'), 0);
        try {
            Answer.applyOp(5, 0, '/');
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            // Expected exception
        }
    }

    @Test
    public void testExponentiation() {
        assertEquals(8, Answer.applyOp(2, 3, '^'), 0);
        assertEquals(3, Answer.applyOp(9, 0.5, '^'), 0);
    }
}