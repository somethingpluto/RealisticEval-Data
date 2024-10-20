package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {
    
    @Test
    public void testConvFlagsCase1() {
        assertEquals("FFFFFFE0", convFlags(0x0000001F));
    }

    @Test
    public void testConvFlagsCase2() {
        assertEquals("FFFFFFEA", convFlags(0x00000015));
    }

    @Test
    public void testConvFlagsCase3() {
        assertEquals("0", convFlags(0xFFFFFFFF));
    }

    @Test
    public void testConvFlagsCase4() {
        assertEquals("EDCBA987", convFlags(0x12345678));
    }

    @Test
    public void testConvFlagsCase5() {
        assertEquals("FFFFFFFE", convFlags(0x00000001));
    }

    @Test
    public void testConvFlagsCase6() {
        assertEquals("FFFFFFFC", convFlags(0x00000003));
    }

    @Test
    public void testConvFlagsCase7() {
        assertEquals("FFFFFFF7", convFlags(0x00000008));
    }

    @Test
    public void testConvFlagsCase8() {
        assertEquals("543210FE", convFlags(0xABCDEF01));
    }
}
