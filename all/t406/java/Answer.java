package org.real.temp;

public class Answer {
    
    public static String red(String text) {
        // Implement method to return text in red color
        return "\033[31m" + text + "\033[0m";
    }

    public static String green(String text) {
        // Implement method to return text in green color
        return "\033[32m" + text + "\033[0m";
    }

    public static String blue(String text) {
        // Implement method to return text in blue color
        return "\033[34m" + text + "\033[0m";
    }

    public static String yellow(String text) {
        // Implement method to return text in yellow color
        return "\033[33m" + text + "\033[0m";
    }

    public static String magenta(String text) {
        // Implement method to return text in magenta color
        return "\033[35m" + text + "\033[0m";
    }

    public static String cyan(String text) {
        // Implement method to return text in cyan color
        return "\033[36m" + text + "\033[0m";
    }
}