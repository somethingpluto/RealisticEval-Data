package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;

public class ArrayUtilsTest {

    @Test
    public void testFlattenArray() {
        // Test case 1: Empty list
        assertEquals(Arrays.asList(), ArrayUtils.flattenArray(Arrays.asList()));

        // Test case 2: Single element list
        assertEquals(Arrays.asList(1), ArrayUtils.flattenArray(Arrays.asList(1)));

        // Test case 3: Two-level nested list
        assertEquals(Arrays.asList(1, 2, 3, 4), ArrayUtils.flattenArray(Arrays.asList(
                Arrays.asList(1, 2),
                Arrays.asList(3, 4)
        )));

        // Test case 4: Multi-level nested list
        assertEquals(Arrays.asList(1, 2, 3, 4, 5, 6), ArrayUtils.flattenArray(Arrays.asList(
                Arrays.asList(1, 2),
                Arrays.asList(3, Arrays.asList(4, 5)),
                Arrays.asList(6)
        )));

        // Test case 5: Mixed types (should throw exception or handle appropriately)
        try {
            ArrayUtils.flattenArray(Arrays.asList(1, Arrays.asList("a", 2)));
        } catch (ClassCastException e) {
            // Expected exception
        }
    }
}