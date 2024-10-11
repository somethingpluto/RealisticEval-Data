package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testIsPointOnLine() {
        // Test case 1: Point C lies on the line AB
        int[] A = {0, 0};
        int[] B = {4, 4};
        int[] C = {2, 2};
        boolean result = isPointOnLine(A, B, C);
        assertEquals(true, result);

        // Test case 2: Point C does not lie on the line AB
        A = new int[]{0, 0};
        B = new int[]{4, 4};
        C = new int[]{2, 3};
        result = isPointOnLine(A, B, C);
        assertEquals(false, result);

        // Test case 3: Point C is one of the endpoints of the line AB
        A = new int[]{0, 0};
        B = new int[]{4, 4};
        C = new int[]{0, 0};
        result = isPointOnLine(A, B, C);
        assertEquals(true, result);

        A = new int[]{0, 0};
        B = new int[]{4, 4};
        C = new int[]{4, 4};
        result = isPointOnLine(A, B, C);
        assertEquals(true, result);
    }
}