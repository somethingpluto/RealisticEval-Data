package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    private String timestampToReadableDate(long unixTimestamp) {
        long millis = unixTimestamp * 1000;
        Calendar calendar = new GregorianCalendar();
        calendar.setTimeInMillis(millis);
        
        String[] monthNames = {
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        };
        
        String month = monthNames[calendar.get(Calendar.MONTH)];
        int day = calendar.get(Calendar.DAY_OF_MONTH);
        int hours = calendar.get(Calendar.HOUR_OF_DAY);
        String minutes = String.format("%02d", calendar.get(Calendar.MINUTE));
        
        return String.format("%s %d, %d:%s", month, day, hours, minutes);
    }

    @Test
    public void testConvertUnixTimestampToReadableFormat() {
        long timestamp = 1696516800;
        assertEquals("Oct 5, 22:40", timestampToReadableDate(timestamp));
    }

    @Test
    public void testHandleTimestampAtStartOfYear() {
        long timestamp = 1672531200;
        assertEquals("Jan 1, 8:00", timestampToReadableDate(timestamp));
    }

    @Test
    public void testHandleTimestampAtEndOfYear() {
        long timestamp = 1672531199;
        assertEquals("Jan 1, 7:59", timestampToReadableDate(timestamp));
    }

    @Test
    public void testHandleTimestampsInLeapYear() {
        long timestamp = 1583020800;
        assertEquals("Mar 1, 8:00", timestampToReadableDate(timestamp));
    }

    @Test
    public void testConvertTimestampToReadableFormatWithSingleDigitDay() {
        long timestamp = 1675190400;
        assertEquals("Feb 1, 2:40", timestampToReadableDate(timestamp));
    }

    @Test
    public void testHandleZeroUnixTimestamp() {
        long timestamp = 0;
        assertEquals("Jan 1, 8:00", timestampToReadableDate(timestamp));
    }
}