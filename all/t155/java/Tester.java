package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

import java.util.Date;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testGetTimestampOneSecondAgo() {
        Date oneSecondAgo = new Date(System.currentTimeMillis() - 1000); // 1 second ago
        assertEquals("1 second ago",getTimestamp(oneSecondAgo));
    }

    @Test
    public void testGetTimestampFiveMinutesAgo() {
        Date fiveMinutesAgo = new Date(System.currentTimeMillis() - 5 * 60 * 1000); // 5 minutes ago
        assertEquals("5 minutes ago",getTimestamp(fiveMinutesAgo));
    }

    @Test
    public void testGetTimestampTwoHoursAgo() {
        Date twoHoursAgo = new Date(System.currentTimeMillis() - 2 * 60 * 60 * 1000); // 2 hours ago
        assertEquals("2 hours ago",getTimestamp(twoHoursAgo));
    }

    @Test
    public void testGetTimestampThreeDaysAgo() {
        Date threeDaysAgo = new Date(System.currentTimeMillis() - 3 * 24 * 60 * 60 * 1000); // 3 days ago
        assertEquals("3 days ago",getTimestamp(threeDaysAgo));
    }
}