package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testFormatThreadCountForOne() {
        assertEquals("01 Thread", formatThreadCount(1));
    }

    @Test
    public void testFormatThreadCountForFive() {
        assertEquals("05 Threads", formatThreadCount(5));
    }

    @Test
    public void testFormatThreadCountForTen() {
        assertEquals("10 Threads", formatThreadCount(10));
    }

    @Test
    public void testFormatThreadCountForNinetyNine() {
        assertEquals("99 Threads", formatThreadCount(99));
    }
}