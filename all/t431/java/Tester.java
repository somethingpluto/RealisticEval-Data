package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;

/**
 * Test class for checking horizontal intersection of rectangles.
 */
public class Tester {

    /**
     * Determines if two rectangles intersect horizontally.
     *
     * Each rectangle is defined by an array [x1, y1, x2, y2], where:
     * - [x1, y1] are the coordinates of the bottom-left corner.
     * - [x2, y2] are the coordinates of the top-right corner.
     *
     * @param rect1 The first rectangle defined by [x1, y1, x2, y2].
     * @param rect2 The second rectangle defined by [x1, y1, x2, y2].
     * @return true if the rectangles intersect horizontally, false otherwise.
     */
    private static boolean intersectHorizontally(int[] rect1, int[] rect2) {
        return !(rect1[2] < rect2[0] || rect2[2] < rect1[0]);
    }

    @Test
    public void testCase1() {
        int[] rect1 = {0, 0, 2, 2};
        int[] rect2 = {1, 1, 3, 3};
        assertTrue("Test with overlapping rectangles", intersectHorizontally(rect1, rect2));
    }

    @Test
    public void testCase2() {
        int[] rect1 = {0, 0, 1, 1};
        int[] rect2 = {1, 1, 2, 2};
        assertTrue("Test with rectangles touching at a point (not overlapping)", intersectHorizontally(rect1, rect2));
    }

    @Test
    public void testCase3() {
        int[] rect1 = {0, 0, 2, 2};
        int[] rect2 = {2, 0, 3, 3};
        assertTrue("Test with adjacent rectangles (no overlap)", intersectHorizontally(rect1, rect2));
    }

    @Test
    public void testCase4() {
        int[] rect1 = {1, 1, 4, 4};
        int[] rect2 = {2, 2, 3, 3};
        assertTrue("Test with one rectangle fully inside another", intersectHorizontally(rect1, rect2));
    }

    @Test
    public void testCase5() {
        int[] rect1 = {-1, -1, 1, 1};
        int[] rect2 = {0, 0, 2, 2};
        assertTrue("Test with overlapping rectangles", intersectHorizontally(rect1, rect2));
    }
}