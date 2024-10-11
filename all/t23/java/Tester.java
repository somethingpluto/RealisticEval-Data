package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testIntersection() {
        double[] seg1Start = {1, 1};
        double[] seg1End = {4, 4};
        double[] seg2Start = {1, 4};
        double[] seg2End = {4, 1};
        double[] expected = {2.5, 2.5};

        double[] result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);

        assertArrayEquals(expected, result, "The intersection should be at (2.5, 2.5)");
    }

    @Test
    public void testNoIntersection() {
        double[] seg1Start = {1, 1};
        double[] seg1End = {2, 2};
        double[] seg2Start = {3, 3};
        double[] seg2End = {4, 4};

        double[] result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);

        assertNull(result, "There should be no intersection");
    }

    @Test
    public void testParallelSegments() {
        double[] seg1Start = {1, 1};
        double[] seg1End = {2, 2};
        double[] seg2Start = {1, 2};
        double[] seg2End = {2, 3};

        double[] result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);

        assertNull(result, "Parallel segments should not intersect");
    }

    @Test
    public void testNoIntersectionDueToOffset() {
        double[] seg1Start = {1, 1};
        double[] seg1End = {3, 3};
        double[] seg2Start = {3, 2};
        double[] seg2End = {4, 2};

        double[] result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);

        assertNull(result, "There should be no intersection due to offset between segments");
    }

    @Test
    public void testIntersectionWithLargeCoordinates() {
        double[] seg1Start = {1000, 1000};
        double[] seg1End = {2000, 2000};
        double[] seg2Start = {1000, 2000};
        double[] seg2End = {2000, 1000};
        double[] expected = {1500.0, 1500.0};

        double[] result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);

        assertArrayEquals(expected, result, "The intersection should be at (1500.0, 1500.0)");
    }

}
