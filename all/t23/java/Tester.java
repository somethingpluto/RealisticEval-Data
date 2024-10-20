package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testIntersection() {
        Point seg1Start = new Point(1, 1);
        Point seg1End = new Point(4, 4);
        Point seg2Start = new Point(1, 4);
        Point seg2End = new Point(4, 1);
        Point expected = new Point(2.5, 2.5);

        Point result = getLineSegmentIntersection(seg1Start, seg1End, seg2Start, seg2End);
        assertEquals("The intersection should be at (2.5, 2.5)", expected, result);
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
        assertEquals("The intersection should be at (1500.0, 1500.0)", expected, result);
    }
    /**
     * Represents a point with x and y coordinates.
     */
    static class Point {
        double x, y;

        /**
         * Constructs a new Point with the specified coordinates.
         *
         * @param x The x-coordinate.
         * @param y The y-coordinate.
         */
        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        /**
         * Compares this Point with another Point for equality.
         *
         * @param obj The other Point to compare with.
         * @return true if the Points are equal, false otherwise.
         */
        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null || getClass() != obj.getClass()) {
                return false;
            }
            Point other = (Point) obj;
            return Double.compare(x, other.x) == 0 && Double.compare(y, other.y) == 0;
        }

        /**
         * Returns a string representation of the Point.
         *
         * @return A string in the format "(x, y)".
         */
        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }

        /**
         * Generates a hash code for the Point.
         *
         * @return The hash code.
         */
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}