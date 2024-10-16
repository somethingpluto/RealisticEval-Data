package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testFindOrder() {
        // Test Case 1: Minimum valid input with 2 players
        assertEquals(Arrays.asList(2, 1), Answer.findOrder(2));

        // Test Case 2: 3 players
        assertEquals(Arrays.asList(2, 3, 1), Answer.findOrder(3));

        // Test Case 3: 5 players
        assertEquals(Arrays.asList(2, 5, 3, 4, 1), Answer.findOrder(5));

        // Test Case 4: 7 players
        assertEquals(Arrays.asList(2, 5, 4, 1, 6, 7, 3), Answer.findOrder(7));

        // Test Case 5: 10 players
        assertEquals(Arrays.asList(2, 5, 10, 9, 7, 3, 4, 6, 8, 1), Answer.findOrder(10));
    }
}