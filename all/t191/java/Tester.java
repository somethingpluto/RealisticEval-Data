package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testFloatToHexPositive() {
        float input = 123.456f;
        String expected = "42f6e979";
        assertEquals(expected, Answer.floatToHex(input));
    }

    @Test
    public void testFloatToHexNegative() {
        float input = -123.456f;
        String expected = "c2f6e979";
        assertEquals(expected, Answer.floatToHex(input));
    }

    @Test
    public void testFloatToHexZero() {
        float input = 0.0f;
        String expected = "00000000";
        assertEquals(expected, Answer.floatToHex(input));
    }

    @Test
    public void testFloatToHexSmallPositive() {
        float input = 0.0001f;
        String expected = "38d1b717";
        assertEquals(expected, Answer.floatToHex(input));
    }

    @Test
    public void testFloatToHexLarge() {
        float input = 1e30f;
        String expected = "7149f2ca";
        assertEquals(expected, Answer.floatToHex(input));
    }
}