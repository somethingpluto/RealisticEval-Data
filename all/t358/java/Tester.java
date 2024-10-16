package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class Tester {

    @Test
    public void testSortNames() {
        // Test Case 2: Same numbers, different names
        String[] arr2 = {"Alice10", "Charlie10", "Bob10"};
        String[] expected2 = {"Alice10", "Bob10", "Charlie10"};
        assertArrayEquals(expected2, Answer.sortNames(arr2));

        // Test Case 3: Mixed case with different names and numbers
        String[] arr3 = {"Alice3", "Bob2", "Charlie3", "Bob1"};
        String[] expected3 = {"Bob1", "Bob2", "Alice3", "Charlie3"};
        assertArrayEquals(expected3, Answer.sortNames(arr3));

        // Test Case 4: Single element
        String[] arr4 = {"Alice5"};
        String[] expected4 = {"Alice5"};
        assertArrayEquals(expected4, Answer.sortNames(arr4));

        // Test Case 5: Empty array
        String[] arr5 = {};
        String[] expected5 = {};
        assertArrayEquals(expected5, Answer.sortNames(arr5));
    }
}