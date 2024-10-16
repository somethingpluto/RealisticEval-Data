package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    /**
     * Converts the array of Boolean values to a binary string representation,
     * which converts to the character '1' if the Boolean value is true.
     * Otherwise, it is converted to the character '0', and the final string is returned.
     *
     * @param boolArray An array of boolean values.
     * @return A binary string where '1' represents true and '0' represents false.
     */
    public static String boolArrayToBinaryString(boolean[] boolArray) {
        StringBuilder binaryString = new StringBuilder();
        for (boolean value : boolArray) {
            binaryString.append(value ? "1" : "0");
        }
        return binaryString.toString();
    }

    @Test
    public void testConvertsAllTrueValues() {
        boolean[] boolArray = {true, true, true};
        String expected = "111";
        assertEquals(expected, boolArrayToBinaryString(boolArray));
    }

    @Test
    public void testConvertsAllFalseValues() {
        boolean[] boolArray = {false, false, false};
        String expected = "000";
        assertEquals(expected, boolArrayToBinaryString(boolArray));
    }

    @Test
    public void testConvertsMixedValues() {
        boolean[] boolArray = {true, false, true, false};
        String expected = "1010";
        assertEquals(expected, boolArrayToBinaryString(boolArray));
    }

    @Test
    public void testHandlesEmptyArray() {
        boolean[] boolArray = {};
        String expected = "";
        assertEquals(expected, boolArrayToBinaryString(boolArray));
    }

    @Test
    public void testHandlesSingleBooleanValue() {
        boolean[] boolArray = {true};
        String expected = "1";
        assertEquals(expected, boolArrayToBinaryString(boolArray));
    }
}