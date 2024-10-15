package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Date;

public class Tester {

    @Test
    public void testGetTimestampOneSecondAgo() {
        Date oneSecondAgo = new Date(System.currentTimeMillis() - 1000); // 1 second ago
        assertEquals("1 second ago", TimestampUtil.getTimestamp(oneSecondAgo));
    }

    @Test
    public void testGetTimestampFiveMinutesAgo() {
        Date fiveMinutesAgo = new Date(System.currentTimeMillis() - 5 * 60 * 1000); // 5 minutes ago
        assertEquals("5 minutes ago", TimestampUtil.getTimestamp(fiveMinutesAgo));
    }

    @Test
    public void testGetTimestampTwoHoursAgo() {
        Date twoHoursAgo = new Date(System.currentTimeMillis() - 2 * 60 * 60 * 1000); // 2 hours ago
        assertEquals("2 hours ago", TimestampUtil.getTimestamp(twoHoursAgo));
    }

    @Test
    public void testGetTimestampThreeDaysAgo() {
        Date threeDaysAgo = new Date(System.currentTimeMillis() - 3 * 24 * 60 * 60 * 1000); // 3 days ago
        assertEquals("3 days ago", TimestampUtil.getTimestamp(threeDaysAgo));
    }
}