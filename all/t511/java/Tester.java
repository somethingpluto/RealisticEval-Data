package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for verifying the correctness of the hexToAnsi method.
 */
public class Tester {

    /**
     * Tests valid hex color inputs.
     */
    @Test
    public void testValidColors() {
        assertEquals("\u001b[38;2;255;87;51m", hexToAnsi("#FF5733"));
        assertEquals("\u001b[38;2;0;255;0m", hexToAnsi("#00FF00"));
        assertEquals("\u001b[38;2;0;0;255m", hexToAnsi("#0000FF"));
    }

    /**
     * Tests edge cases with black and white colors.
     */
    @Test
    public void testBlackAndWhite() {
        assertEquals("\u001b[38;2;0;0;0m", hexToAnsi("#000000"));  // Black
        assertEquals("\u001b[38;2;255;255;255m", hexToAnsi("#FFFFFF"));  // White
    }

    /**
     * Converts a hexadecimal color code to an ANSI escape code.
     *
     * @param hexColor A string representing the hexadecimal color code, e.g., "#FF5733".
     * @return An ANSI escape code for the specified RGB color.
     * @throws IllegalArgumentException if the hex color format is invalid.
     */
    private String hexToAnsi(String hexColor) {
        // Check if the input is a valid hex color
        if (hexColor == null || hexColor.length() != 7 || !hexColor.startsWith("#")) {
            throw new IllegalArgumentException("Invalid hex color format. Use '#RRGGBB'.");
        }

        // Extract the red, green, and blue components from the hex string
        int r = Integer.parseInt(hexColor.substring(1, 3), 16);
        int g = Integer.parseInt(hexColor.substring(3, 5), 16);
        int b = Integer.parseInt(hexColor.substring(5, 7), 16);

        // Create the ANSI escape code
        String ansiCode = "\u001b[38;2;" + r + ";" + g + ";" + b + "m";

        return ansiCode;
    }
}