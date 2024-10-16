package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testConvFlags() {
        assertEquals("FFFFFFE0", new Answer().convFlags(0x0000001F));
        assertEquals("FFFFFFEA", new Answer().convFlags(0x00000015));
        assertEquals("0", new Answer().convFlags(0xFFFFFFFF));
        assertEquals("EDCBA987", new Answer().convFlags(0x12345678));
        assertEquals("FFFFFFFE", new Answer().convFlags(0x00000001));
        assertEquals("FFFFFFFC", new Answer().convFlags(0x00000003));
        assertEquals("FFFFFFF7", new Answer().convFlags(0x00000008));
        assertEquals("543210FE", new Answer().convFlags(0xABCDEF01));
    }
}