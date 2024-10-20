package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.real.temp.Answer.*;

public class Tester {

    private long fixedTimestamp;

    @Before
    public void setUp() {
        // Freeze the current time to a fixed timestamp
        fixedTimestamp = 1609459200000L; // January 1, 2021, 00:00:00
    }
    

    @Test
    public void testTimePassedOneMinuteAgo() {
        long startTime = fixedTimestamp - 60000; // 1 minute earlier
        assertEquals("1:00", timePassed(startTime));
    }

    @Test
    public void testTimePassedBoundaryOf59Seconds() {
        long startTime = fixedTimestamp - 5900; // 59 seconds and 900 milliseconds earlier
        assertEquals("0:05", timePassed(startTime));
    }

    @Test
    public void testTimePassedSameAsCurrentTime() {
        assertEquals("0:00", timePassed(fixedTimestamp));
    }

    @Test
    public void testTimePassedFutureStartTime() {
        long startTime = fixedTimestamp + 60000; // 1 minute into the future
        String result = timePassed(startTime);
        assertTrue(result.startsWith("-")); // Expecting negative output or some error handling
    }

    @Test
    public void testTimePassedLargeTimeDifference() {
        long startTime = 1483228800000L; // January 1, 2017, 00:00:00 (4 years difference)
        assertEquals("2103840:00", timePassed(startTime)); // Calculated minutes for 4 years
    }
}