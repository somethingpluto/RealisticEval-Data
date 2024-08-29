package com.real.t351;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class TestClass {
    @Test
    void testBezierAtStart() {
        assertEquals(1.0, Adapted.bezier(0, 1, 3, 3, 1), "Bezier at t=0 should return the first control point p0");
    }

    @Test
    void testBezierAtEnd() {
        assertEquals(1.0, Adapted.bezier(1, 1, 3, 3, 1), "Bezier at t=1 should return the last control point p3");
    }

    @Test
    void testBezierAtMiddle() {
        double expected = 1.0 * 0.125 + 3 * 0.375 + 3 * 0.375 + 1 * 0.125; // Calculate manually for t=0.5
        assertEquals(expected, Adapted.bezier(0.5, 1, 3, 3, 1), 0.001, "Bezier at t=0.5 should return the correct middle value");
    }

    @Test
    void testBezierParameterOutOfRange() {
        assertThrows(IllegalArgumentException.class, () -> Adapted.bezier(-0.1, 1, 3, 3, 1),
                "Bezier should throw IllegalArgumentException for t out of range");
        assertThrows(IllegalArgumentException.class, () -> Adapted.bezier(1.1, 1, 3, 3, 1),
                "Bezier should throw IllegalArgumentException for t out of range");
    }

    @Test
    void testBezierWithIdenticalControlPoints() {
        assertEquals(2.0, Adapted.bezier(0.5, 2, 2, 2, 2), "Bezier with all control points the same should return that value");
    }
}
