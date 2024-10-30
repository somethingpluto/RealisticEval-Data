package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testIntersection() {
        Point seg1Start = new Point(1, 1);
        Point seg1End = new Point(4, 4);
        Point seg2Start = new Point(1, 4);
        Point seg2End = new Point(4, 1);
        Point expected = new Point(2.5, 2.5);

        Point result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);
        assertTrue("The intersection should be at (2.5, 2.5)",(expected.x == result.x)&&(expected.y == result.y));
    }

    @Test
    public void testNoIntersection() {
        Point seg1Start = new Point(1, 1);
        Point seg1End = new Point(2, 2);
        Point seg2Start = new Point(3, 3);
        Point seg2End = new Point(4, 4);

        Point result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);
        assertNull("There should be no intersection", result);
    }

    @Test
    public void testParallelSegments() {
        Point seg1Start = new Point(1, 1);
        Point seg1End = new Point(2, 2);
        Point seg2Start = new Point(1, 2);
        Point seg2End = new Point(2, 3);

        Point result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);
        assertNull("Parallel segments should not intersect", result);
    }

    @Test
    public void testNoIntersectionDueToOffset() {
        Point seg1Start = new Point(1, 1);
        Point seg1End = new Point(3, 3);
        Point seg2Start = new Point(3, 2);
        Point seg2End = new Point(4, 2);

        Point result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);
        assertNull("There should be no intersection due to offset between segments", result);
    }

    @Test
    public void testIntersectionWithLargeCoordinates() {
        Point seg1Start = new Point(1000, 1000);
        Point seg1End = new Point(2000, 2000);
        Point seg2Start = new Point(1000, 2000);
        Point seg2End = new Point(2000, 1000);
        Point expected = new Point(1500.0, 1500.0);

        Point result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);
        assertTrue("The intersection should be at (1500.0, 1500.0)", (expected.x == result.x)&&(expected.y == result.y));
    }
}