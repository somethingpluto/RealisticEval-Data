    /**
     * Converts the given hex web value color to RGB color code. Code generated using ChatGPT.
     * @param color (Color): color as hex web value
     * @return Color: color as RGB code
     */
    private static String toRGBCode(Color color) {
        return String.format("#%02X%02X%02X",
                (int) (color.getRed() * 255),
                (int) (color.getGreen() * 255),
                (int) (color.getBlue() * 255));
    }
