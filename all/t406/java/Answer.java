package org.real.temp;

public final class Answer {

    private static final String RESET = "\033[0m";
    private static final String RED = "\033[91m";
    private static final String GREEN = "\033[92m";
    private static final String BLUE = "\033[94m";
    private static final String YELLOW = "\033[93m";
    private static final String MAGENTA = "\033[95m";
    private static final String CYAN = "\033[96m";

    private Answer() {
        // Private constructor to prevent instantiation
    }

    public static String red(String text) {
        return RED + text + RESET;
    }

    public static String green(String text) {
        return GREEN + text + RESET;
    }

    public static String blue(String text) {
        return BLUE + text + RESET;
    }

    public static String yellow(String text) {
        return YELLOW + text + RESET;
    }

    public static String magenta(String text) {
        return MAGENTA + text + RESET;
    }

    public static String cyan(String text) {
        return CYAN + text + RESET;
    }
}