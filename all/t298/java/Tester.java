package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testFormatsStandardValuesCorrectly() {
        assertEquals("250", setEurValue("250"));
        assertEquals("2.5k", setEurValue("2500"));
    }

    @Test
    public void testHandlesBoundaryValuesAccurately() {
        assertEquals("999", setEurValue("999"));
        assertEquals("1.0k", setEurValue("1000"));
        assertEquals("1000.0k", setEurValue("999999"));
        assertEquals("1.0m", setEurValue("1000000"));
    }

    @Test
    public void testReturnsCorrectFormatForZeroAndNegativeInputs() {
        assertEquals("0", setEurValue("0"));
    }


    @Test
    public void testEnsuresPrecisionForLargeNumbers() {
        assertEquals("10.0m", setEurValue("10000000"));
        assertEquals("987.7m", setEurValue("987654321"));
    }
    
}