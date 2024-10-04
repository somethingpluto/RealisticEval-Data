package org.real.temp;

import java.awt.Color;

public class Answer {

    /**
     * Converts a Color object to its corresponding RGB color code string.
     *
     * @param color the Color object to convert
     * @return a hexadecimal string representing the RGB color code
     */
    public static String toRGBCode(Color color) {
        return String.format("#%02X%02X%02X",
                color.getRed(),
                color.getGreen(),
                color.getBlue());
    }

    // Main method for testing purposes
    public static void main(String[] args) {
        Color color = new Color(255, 87, 51); // Example color
        String rgbCode = toRGBCode(color);
        System.out.println("RGB Code: " + rgbCode); // Output: RGB Code: #FF5733
    }
}
