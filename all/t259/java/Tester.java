package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testIsCompliantFourDigit() {
        // Test cases to verify the functionality of isCompliantFourDigit method

        // Case 1: Valid four-digit number
        assertTrue(isCompliantFourDigit(1234));

        // Case 2: Four-digit number with leading zero (should be false)
        assertFalse(isCompliantFourDigit(0123));

        // Case 3: Less than four digits
        assertFalse(isCompliantFourDigit(123));

        // Case 4: More than four digits
        assertFalse(isCompliantFourDigit(12345));

        // Case 5: Negative number
        assertFalse(isCompliantFourDigit(-1234));
    }

    /**
     * Determine whether a number is a compliant four-digit number
     *
     * @param number The number to check.
     * @return True if the number is a compliant four-digit number, False otherwise.
     */
    public boolean isCompliantFourDigit(int number) {
        String numStr = String.valueOf(Math.abs(number));
        return numStr.length() == 4;
    }
}