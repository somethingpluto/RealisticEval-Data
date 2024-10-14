package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class Tester {

    @Test
    public void testIsBreakTime_StartTime() {
        assertTrue(isBreakTime("09:00", "10:00", "09:00"));
    }

    @Test
    public void testIsBreakTime_WithinRange() {
        assertTrue(isBreakTime("09:00", "10:00", "09:30"));
    }

    @Test
    public void testIsBreakTime_ExceedEndTime() {
        assertFalse(isBreakTime("09:00", "10:00", "20:00"));
    }

    @Test
    public void testIsBreakTime_BeforeStart() {
        assertFalse(isBreakTime("09:00", "10:00", "08:59"));
    }

    @Test
    public void testIsBreakTime_AfterEnd() {
        assertFalse(isBreakTime("09:00", "10:00", "10:01"));
    }

    // Assuming the method isBreakTime is defined in this class or imported
    public static boolean isBreakTime(String startTime, String endTime, String currentTime) {
        // Implementation here
    }
}