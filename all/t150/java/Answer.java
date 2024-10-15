public class ColorConverter {

    /**
     * Convert an RGB color object to a HEX color string.
     * @param rgb - An array containing the red, green, and blue components of the color.
     * @returns A string representing the HEX color code.
     */
    public static String rgbToHex(int[] rgb) {
        if (rgb.length != 3) {
            throw new IllegalArgumentException("Invalid RGB array");
        }

        return String.format("#%02x%02x%02x", rgb[0], rgb[1], rgb[2]);
    }

    /**
     * Convert a HEX color string to an RGB color object.
     * @param hex - A string representing the HEX color code.
     * @returns An array containing the red, green, and blue components of the color, or null if the HEX code is invalid.
     */
    public static int[] hexToRgb(String hex) {
        if (!isValidHex(hex)) {
            System.err.println("Invalid HEX color: " + hex);
            return null;
        }

        int r = Integer.parseInt(hex.substring(1, 3), 16);
        int g = Integer.parseInt(hex.substring(3, 5), 16);
        int b = Integer.parseInt(hex.substring(5, 7), 16);

        return new int[]{r, g, b};
    }

    private static boolean isValidHex(String hex) {
        String normalizedHex = hex.replaceFirst("^#", "");
        return normalizedHex.matches("[0-9a-fA-F]{6}");
    }
}