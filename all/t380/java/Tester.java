package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {
    @Test
    public void testCompleteTime() {
        // Test with full values provided for days, hours, minutes, and seconds
        int[] time = {1, 2, 3, 4};  // 1 day, 2 hours, 3 minutes, 4 seconds
        int expected = 93784;
        int result = calculateTotalSeconds(time);
        assertEquals(expected, result);
    }

    @Test
    public void testPartialTime() {
        // Test with some values missing (assumed trailing zeros)
        int[] time = {0, 2, 3};  // 0 days, 2 hours, 3 minutes
        int expected = 7380;
        int result = calculateTotalSeconds(time);
        assertEquals(expected, result);
    }

    @Test
    public void testSecondsOnly() {
        // Test with only seconds provided
        int[] time = {0, 0, 0, 7200};  // 7200 seconds
        int expected = 7200;
        int result = calculateTotalSeconds(time);
        assertEquals(expected, result);
    }

    @Test
    public void testNoTime() {
        // Test with no time values provided
        int[] time = {};
        int expected = 0;
        int result = calculateTotalSeconds(time);
        assertEquals(expected, result);
    }
}