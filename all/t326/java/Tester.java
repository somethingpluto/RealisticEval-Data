package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testCalculateTimeDifferenceForPastDate() {
        long pastDateMillis = System.currentTimeMillis() - (3 * 24 * 60 * 60 * 1000 + 5 * 60 * 1000); // 3 days and 5 minutes ago
        TimeDifference result = TimeDifferenceCalculator.calculateTimeDifference(new Date(pastDateMillis));
        assertEquals(3, result.days);
        assertEquals(0, result.hours);
        assertEquals(5, result.minutes);
    }

    @Test
    public void testCalculateTimeDifferenceForNow() {
        Date now = new Date();
        TimeDifference result = TimeDifferenceCalculator.calculateTimeDifference(now);
        assertEquals(0, result.days);
        assertEquals(0, result.hours);
        assertEquals(0, result.minutes);
    }

    @Test
    public void testCalculateTimeDifferenceForJustSecondsAgo() {
        long justNowMillis = System.currentTimeMillis() - 45 * 1000; // 45 seconds ago
        TimeDifference result = TimeDifferenceCalculator.calculateTimeDifference(new Date(justNowMillis));
        assertEquals(0, result.days);
        assertEquals(0, result.hours);
        assertEquals(0, result.minutes);
    }

    @Test
    public void testCalculateTimeDifferenceForHoursDifference() {
        long hoursAgoMillis = System.currentTimeMillis() - 7 * 60 * 60 * 1000; // 7 hours ago
        TimeDifference result = TimeDifferenceCalculator.calculateTimeDifference(new Date(hoursAgoMillis));
        assertEquals(0, result.days);
        assertEquals(7, result.hours);
        assertEquals(0, result.minutes);
    }

    @Test
    public void testCalculateTimeDifferenceForHoursAndMinutesDifference() {
        long hoursAndMinutesAgoMillis = System.currentTimeMillis() - (1 * 24 * 60 * 60 * 1000 + 3 * 60 * 1000); // 1 day and 3 minutes ago
        TimeDifference result = TimeDifferenceCalculator.calculateTimeDifference(new Date(hoursAndMinutesAgoMillis));
        assertEquals(1, result.days);
        assertEquals(0, result.hours);
        assertEquals(3, result.minutes);
    }

    public static class TimeDifference {
        public long days;
        public long hours;
        public long minutes;

        public TimeDifference(long days, long hours, long minutes) {
            this.days = days;
            this.hours = hours;
            this.minutes = minutes;
        }
    }
}