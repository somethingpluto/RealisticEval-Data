package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testHexStringToUnsignedIntValidHexStrings() {
        assertEquals(6719, Answer.hexStringToUnsignedInt("1A3F")); // 1A3F in hex is 6719 in decimal
        assertEquals(65535, Answer.hexStringToUnsignedInt("FFFF")); // FFFF in hex is 65535 in decimal
        assertEquals(0, Answer.hexStringToUnsignedInt("0")); // 0 in hex is 0 in decimal
        assertEquals(127, Answer.hexStringToUnsignedInt("7F")); // 7F in hex is 127 in decimal
        assertEquals(11256099, Answer.hexStringToUnsignedInt("ABC123")); // ABC123 in hex is 11256099 in decimal
    }

    @Test
    public void testHexStringToUnsignedIntLowercaseHexString() {
        assertEquals(43981, Answer.hexStringToUnsignedInt("abcd")); // abcd in hex is 43981 in decimal
    }

    @Test
    public void testHexStringToUnsignedIntLeadingZeroes() {
        assertEquals(1, Answer.hexStringToUnsignedInt("0001")); // 0001 in hex is 1 in decimal
    }

    @Test
    public void testHexStringToUnsignedIntEmptyString() {
        assertEquals(0, Answer.hexStringToUnsignedInt("")); // Empty string should be treated as 0
    }

    @Test
    public void testHexStringToUnsignedIntMixedCase() {
        assertEquals(11259375, Answer.hexStringToUnsignedInt("AbCdEf")); // AbCdEf in hex is 11259375 in decimal
    }
}