package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testArrayLengthEqualToTargetLength() {
        int[] result = adjustArrayLength(5, new int[]{1, 2, 3, 4, 5});
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, result);
    }

    @Test
    public void testArrayLengthShorterThanTargetLength() {
        int[] result = adjustArrayLength(8, new int[]{1, 2, 3});
        assertArrayEquals(new int[]{1, 2, 3, 1, 2, 3, 1, 2}, result);
    }

    @Test
    public void testArrayLengthShorterThanTargetLengthMultiple() {
        int[] result = adjustArrayLength(6, new int[]{10, 20});
        assertArrayEquals(new int[]{10, 20, 10, 20, 10, 20}, result);
    }

    @Test
    public void testArrayLengthShorterThanTargetLengthNotMultiple() {
        int[] result = adjustArrayLength(7, new int[]{7, 14, 21});
        assertArrayEquals(new int[]{7, 14, 21, 7, 14, 21, 7}, result);
    }
}