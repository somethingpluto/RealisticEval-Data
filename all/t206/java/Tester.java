package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    private static final double TOLERANCE = 1e-5;

    @Test
    public void testNoOverlapCirclesFarApart() {
        assertEquals(0.0, Answer.circleIntersectionArea(0.0, 0.0, 3.0, 10.0, 10.0, 3.0), TOLERANCE);
    }

    @Test
    public void testNoOverlapCirclesJustTouching() {
        assertEquals(0.0, Answer.circleIntersectionArea(0.0, 0.0, 3.0, 6.0, 0.0, 3.0), TOLERANCE);
    }

    @Test
    public void testOneCircleInsideTheOther() {
        double area = Answer.circleIntersectionArea(0.0, 0.0, 5.0, 2.0, 0.0, 3.0);
        assertEquals(28.2743, area, TOLERANCE); // Area of smaller circle
    }

    @Test
    public void testIdenticalCirclesFullOverlap() {
        double area = Answer.circleIntersectionArea(0.0, 0.0, 3.0, 0.0, 0.0, 3.0);
        assertEquals(28.2743, area, TOLERANCE); // Area of one circle
    }
}