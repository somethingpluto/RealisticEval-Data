package org.real.temp;

public class Answer {

    /**
     * Convert a hexadecimal color code to an ANSI escape code.
     *
     * @param hexColor A string representing the hexadecimal color code, e.g., "#FF5733".
     * @return An ANSI escape code for the specified RGB color.
     * @throws IllegalArgumentException if the hex color format is invalid.
     */
    public static String hexToAnsi(String hexColor) {
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

    public static void main(String[] args) {
        // Example usage
        try {
            String hexColor = "#FF5733";
            String ansiCode = hexToAnsi(hexColor);
            System.out.println("ANSI Code: " + ansiCode);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}