package org.real.temp;
public class Answer {
    public static boolean isSnakeCase(String input) {
        // Regular expression to match SNAKE_CASE
        String snakeCaseRegex = "^[a-z]+(_[a-z]+)*$";
        return input != null && input.matches(snakeCaseRegex);
    }
}