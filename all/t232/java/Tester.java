package org.real.temp;
import static org.junit.Assert.*;
import org.junit.Test;

import java.util.Optional;

import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testBasicConversion() {
        assertEquals("Should convert 1h20min30s to 4830000 milliseconds", Optional.of(4830000).get(),convertHmsToMilliseconds("1h20min30s"));
    }

    @Test
    public void testNoHoursOrMinutes() {
        assertEquals("Should convert 30s to 30000 milliseconds",
                Optional.of(30000).get(),
                convertHmsToMilliseconds("30s"));
    }

    @Test
    public void testInvalidFormat() {
        assertNull("Should return null for invalid time format",
                convertHmsToMilliseconds("1hour20minutes"));
    }

    @Test
    public void testEdgeCaseMaxOneDay() {
        assertEquals("Should convert 23h59min59s to 86399000 milliseconds",
                Optional.of(86399000).get(),
                convertHmsToMilliseconds("23h59min59s"));
    }

    @Test
    public void testExceedingOneDay() {
        assertEquals("Should correctly convert 24h1min to 86460000 milliseconds",
                Optional.of(86460000).get(),
                convertHmsToMilliseconds("24h1min"));
    }
}
