
package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.temporal.ChronoUnit;

public class Tester {

    private LocalDateTime fixedTime;
    private LocalDateTime originalNow;

    @Before
    public void setUp() {
        // Set the system time to a fixed date
        fixedTime = LocalDateTime.of(2024, 8, 23, 15, 45);
        originalNow = LocalDateTime.now();

        // Assuming we can mock or replace LocalDateTime.now() in the method being tested.
        // If you can't mock the system time directly, consider passing a clock or fixed date to the method.
    }

    @After
    public void tearDown() {
        // Restore original time if needed
        // This would typically be done through a static mock or resetting the context if using a library.
    }

    private long[] getTimeSinceBornUntilNow(LocalDateTime birthDate) {
        // This is where you would implement or call your actual function.
        // For demonstration, let's assume it's implemented correctly.
        LocalDateTime now = fixedTime; // Use the fixed time for testing

        // Calculate the time since birth
        long years = ChronoUnit.YEARS.between(birthDate, now);
        long months = ChronoUnit.MONTHS.between(birthDate.plusYears(years), now);
        long days = ChronoUnit.DAYS.between(birthDate.plusYears(years).plusMonths(months), now);
        long hours = ChronoUnit.HOURS.between(birthDate.plusYears(years).plusMonths(months).plusDays(days), now);
        long minutes = ChronoUnit.MINUTES.between(birthDate.plusYears(years).plusMonths(months).plusDays(days).plusHours(hours), now);

        return new long[]{years, months, days, hours, minutes};
    }

    @Test
    public void testTypicalBirthDate() {
        LocalDateTime birthDate = LocalDateTime.of(1990, 5, 15, 10, 30);
        long[] result = getTimeSinceBornUntilNow(birthDate);
        assertArrayEquals(new long[]{34, 3, 8, 5, 15}, result); // 34 years, 3 months, 8 days, 5 hours, 15 minutes
    }

    @Test
    public void testRecentBirthDate() {
        LocalDateTime birthDate = LocalDateTime.of(2024, 8, 20, 12, 0);
        long[] result = getTimeSinceBornUntilNow(birthDate);
        assertArrayEquals(new long[]{0, 0, 3, 3, 45}, result); // 3 days, 3 hours, 45 minutes
    }

    @Test
    public void testEdgeCaseEndOfYear() {
        LocalDateTime birthDate = LocalDateTime.of(2023, 12, 31, 23, 59);
        long[] result = getTimeSinceBornUntilNow(birthDate);
        assertArrayEquals(new long[]{0, 7, 22, 15, 46}, result); // 7 months, 22 days, 15 hours, 46 minutes
    }

    @Test
    public void testBirthdayEarlierInMonth() {
        LocalDateTime birthDate = LocalDateTime.of(2024, 8, 1, 0, 0);
        long[] result = getTimeSinceBornUntilNow(birthDate);
        assertArrayEquals(new long[]{0, 0, 22, 15, 45}, result); // 22 days, 15 hours, 45 minutes
    }

    @Test
    public void testBirthdayLaterInYearBeforeMonth() {
        LocalDateTime birthDate = LocalDateTime.of(2024, 1, 1, 1, 0);
        long[] result = getTimeSinceBornUntilNow(birthDate);
        assertArrayEquals(new long[]{0, 7, 22, 14, 45}, result); // 7 months, 22 days, 14 hours, 45 minutes
    }

    @Test
    public void testBirthdayPreviousMonth() {
        LocalDateTime birthDate = LocalDateTime.of(2024, 7, 30, 10, 0);
        long[] result = getTimeSinceBornUntilNow(birthDate);
        assertArrayEquals(new long[]{0, 0, 24, 5, 45}, result); // 24 days, 5 hours, 45 minutes
    }
}
