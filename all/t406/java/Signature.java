public final class Colors {

    // Private constructor to prevent instantiation of utility class
    private Colors() {
        throw new UnsupportedOperationException("Utility class");
    }

    /**
     * Returns the text in red color.
     *
     * @param text The text to be colored.
     * @return The text wrapped in ANSI escape codes for red color.
     */
    public static String red(String text) {
        return "\u001B[31m" + text + "\u001B[0m";
    }

    /**
     * Returns the text in green color.
     *
     * @param text The text to be colored.
     * @return The text wrapped in ANSI escape codes for green color.
     */
    public static String green(String text) {
        return "\u001B[32m" + text + "\u001B[0m";
    }

    /**
     * Returns the text in blue color.
     *
     * @param text The text to be colored.
     * @return The text wrapped in ANSI escape codes for blue color.
     */
    public static String blue(String text) {
        return "\u001B[34m" + text + "\u001B[0m";
    }

    /**
     * Returns the text in yellow color.
     *
     * @param text The text to be colored.
     * @return The text wrapped in ANSI escape codes for yellow color.
     */
    public static String yellow(String text) {
        return "\u001B[33m" + text + "\u001B[0m";
    }

    /**
     * Returns the text in magenta color.
     *
     * @param text The text to be colored.
     * @return The text wrapped in ANSI escape codes for magenta color.
     */
    public static String magenta(String text) {
        return "\u001B[35m" + text + "\u001B[0m";
    }

    /**
     * Returns the text in cyan color.
     *
     * @param text The text to be colored.
     * @return The text wrapped in ANSI escape codes for cyan color.
     */
    public static String cyan(String text) {
        return "\u001B[36m" + text + "\u001B[0m";
    }
}