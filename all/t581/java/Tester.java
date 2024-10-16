package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testAbbreviateNumber_LessThan1000() {
        assertEquals("999", NumberAbbreviator.abbreviateNumber(999));
    }

    @Test
    public void testAbbreviateNumber_Exactly1000() {
        String result = NumberAbbreviator.abbreviateNumber(1000);
        assertTrue(result.equals("1k") || result.equals("1.0k"));
    }

    @Test
    public void testAbbreviateNumber_1500() {
        assertEquals("1.5k", NumberAbbreviator.abbreviateNumber(1500));
    }

    @Test
    public void testAbbreviateNumber_OneMillion() {
        String result = NumberAbbreviator.abbreviateNumber(1000000);
        assertTrue(result.equals("1M") || result.equals("1.0M"));
    }

    @Test
    public void testAbbreviateNumber_TwentyFiveMillion() {
        assertEquals("25M", NumberAbbreviator.abbreviateNumber(25000000));
    }

    @Test
    public void testAbbreviateNumber_OneBillion() {
        String result = NumberAbbreviator.abbreviateNumber(1000000000);
        assertTrue(result.equals("1B") || result.equals("1.0B"));
    }

    @Test
    public void testAbbreviateNumber_OnePointTwoTrillion() {
        assertEquals("1.2T", NumberAbbreviator.abbreviateNumber(1234567890123));
    }
}