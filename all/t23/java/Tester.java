import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class Tester {

    private LineSegmentIntersection lineSegmentIntersection;

    @Before
    public void setUp() {
        lineSegmentIntersection = new LineSegmentIntersection();
    }

    @Test
    public void testGetLineSegmentIntersection() {
        // Define your test cases here
        double[][][] testCases = {
            {{{0, 0}, {1, 1}}, {{1, 0}, {0, 1}}, {0.5, 0.5}},
            {{{-1, -1}, {1, 1}}, {{1, -1}, {-1, 1}}, {0.0, 0.0}},
            {{{0, 0}, {0, 1}}, {{0, 1}, {1, 1}}, null},
            {{{0, 0}, {1, 0}}, {{1, 0}, {1, 1}}, null}
        };

        for (double[][] testCase : testCases) {
            double[][] seg1 = testCase[0];
            double[][] seg2 = testCase[1];
            Object expected = testCase[2];

            assertEquals(expected, lineSegmentIntersection.getLineSegmentIntersection(seg1, seg2));
        }
    }
}