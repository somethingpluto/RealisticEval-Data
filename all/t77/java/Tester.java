package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

import java.time.ZoneId;

import static org.real.temp.Answer.*;

public class Tester {

    private static final ZoneId LOCAL_TZ = ZoneId.of("Asia/Singapore"); // Assuming Asia/Singapore as the local timezone

    @Test
    public void testBasicFunctionality() {
        long timestamp = 1655364000L; // Corresponds to Thu Jun 16 12:00:00 PM UTC 2022
        String expectedDateStr = "Thu Jun 16 03:20:00 PM +0800 2022";
        assertEquals("Should correctly format the timestamp", expectedDateStr, formatTimestampToString(timestamp, null));
    }

    @Test
    public void testDefaultFormat() {
        long timestamp = 1655364000L;
        String expectedDateStr = "Thu Jun 16 03:20:00 PM +0800 2022";
        assertEquals("Default format should match the expected date string", expectedDateStr, formatTimestampToString(timestamp, null));
    }

    @Test
    public void testCustomFormat() {
        long timestamp = 1655364000L;
        String customFormat = "%Y-%m-%d %H:%M:%S";
        String expectedDateStr = "2022-06-16 15:20:00";
        assertEquals("Should correctly format the timestamp using the custom format", expectedDateStr, formatTimestampToString(timestamp, customFormat));
    }

    @Test
    public void testEdgeCaseBoundaryValue() {
        long timestamp = 0L; // Unix epoch start
        String expectedDateStr = "Thu Jan 01 08:00:00 AM +0800 1970";
        assertEquals("Should correctly format the Unix epoch start time", expectedDateStr, formatTimestampToString(timestamp, null));
    }
}
