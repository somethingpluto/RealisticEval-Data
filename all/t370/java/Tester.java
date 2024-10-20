package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Test edge case with a larger shape.
     */
    @Test
    public void testEdgeCaseWithLargerShape() {
        assertEquals("[3, 3, 0]", decompose(60, new int[]{4, 4, 4}).toString());
    }

    /**
     * Test the last valid index.
     */
    @Test
    public void testLastValidIndex() {
        assertEquals("[3, 3, 3]", decompose(63, new int[]{4, 4, 4}).toString());
    }

    /**
     * Test single dimension case.
     */
    @Test
    public void testSingleDimensionCase() {
        assertEquals("[2]", decompose(2, new int[]{5}).toString());
    }

    /**
     * Test invalid cases.
     */
    @Test
    public void testInvalidCases() {
        // Test case 5: Out of bounds case (negative index)
        assertThrows(IllegalArgumentException.class, () -> decompose(-1, new int[]{3, 4, 5}));

        // Test case 6: Out of bounds case (index too large)
        assertThrows(IllegalArgumentException.class, () -> decompose(100, new int[]{3, 4, 5}));
    }

}