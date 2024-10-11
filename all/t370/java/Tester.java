package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.Arrays;

public class Tester {

    @Test
    public void testDecompose() {
        // Test case 1
        int[] result = decompose(3, new int[]{2, 2});
        assertArrayEquals(new int[]{0, 1}, result);

        // Test case 2
        result = decompose(5, new int[]{2, 3});
        assertArrayEquals(new int[]{1, 2}, result);

        // Test case 3
        result = decompose(8, new int[]{2, 2, 2});
        assertArrayEquals(new int[]{1, 0, 0}, result);

        // Test case 4: Out of bounds
        try {
            decompose(9, new int[]{2, 2, 2});
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            assertEquals("Index out of bounds", e.getMessage());
        }
    }

    private int[] decompose(int n, int[] shape) {
        if (n < 0 || n >= Arrays.stream(shape).reduce(1, (a, b) -> a * b)) {
            throw new IllegalArgumentException("Index out of bounds");
        }

        int[] result = new int[shape.length];
        int size = 1;
        for (int i = shape.length - 1; i >= 0; i--) {
            result[i] = n / size % shape[i];
            size *= shape[i];
        }
        return result;
    }
}