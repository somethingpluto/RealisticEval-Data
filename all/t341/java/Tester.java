package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testConvertTypicalTimeString() {
        long result = TimeConverter.convertTimeHmsStringToMs("1h30m15s");
        assertEquals(5415000, result);  // 1 hour + 30 minutes + 15 seconds in ms
    }

    @Test
    public void testConvertZeroValues() {
        long result = TimeConverter.convertTimeHmsStringToMs("0h0m0s");
        assertEquals(0, result);  // 0 ms
    }

    @Test
    public void testConvertMaxSingleDigitValues() {
        long result = TimeConverter.convertTimeHmsStringToMs("9h59m59s");
        assertEquals(35999000, result); // 9 hours + 59 minutes + 59 seconds in ms
    }

    @Test
    public void testHandleLargeValues() {
        long result = TimeConverter.convertTimeHmsStringToMs("100h0m0s");
        assertEquals(360000000, result); // 100 hours in ms
    }

    @Test
    public void testConvertLeadingZeros() {
        long result = TimeConverter.convertTimeHmsStringToMs("01h01m01s");
        assertEquals(3661000, result); // 1 hour + 1 minute + 1 second in ms
    }
}