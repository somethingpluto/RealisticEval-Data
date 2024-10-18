public class Tester {

    /**
     * Tests with overlapping rectangles.
     */
    @Test
    public void testCase1() {
        int[] rect1 = {0, 0, 2, 2};
        int[] rect2 = {1, 1, 3, 3};
        assertTrue("Rectangles should intersect vertically", intersectVertically(rect1, rect2));
    }

    /**
     * Tests with overlapping rectangles.
     */
    @Test
    public void testCase2() {
        int[] rect1 = {-1, -1, 1, 1};
        int[] rect2 = {0, 0, 2, 2};
        assertTrue("Rectangles should intersect vertically", intersectVertically(rect1, rect2));
    }

    /**
     * Test case where rectangles partially overlap vertically.
     */
    @Test
    public void testCase3() {
        int[] rect1 = {0, 1, 2, 4};
        int[] rect2 = {1, 0, 3, 2};
        assertTrue("Rectangles should intersect vertically", intersectVertically(rect1, rect2));
    }

    /**
     * Test case where rectangles are identical.
     */
    @Test
    public void testCase4() {
        int[] rect1 = {0, 0, 2, 2};
        int[] rect2 = {0, 0, 2, 2};
        assertTrue("Rectangles should intersect vertically", intersectVertically(rect1, rect2));
    }

    /**
     * Test case where one rectangle is completely inside the other.
     */
    @Test
    public void testCase5() {
        int[] rect1 = {0, 0, 4, 4};
        int[] rect2 = {1, 1, 2, 2};
        assertTrue("Rectangles should intersect vertically", intersectVertically(rect1, rect2));
    }
}