package org.real.temp;

import java.util.regex.Pattern;

public class Answer {

    /**
     * Convert a CamelCase string to snake_case.
     *
     * @param camelStr The CamelCase string to convert.
     * @return The converted snake_case string.
     */
    public static String camelToSnake(String camelStr) {
        // Use regular expression to insert underscores before each uppercase letter,
        // and then convert the whole string to lowercase
        String snakeCaseStr = Pattern.compile("(?<!^)(?=[A-Z])").matcher(camelStr).replaceAll("_").toLowerCase();
        return snakeCaseStr;
    }

    // Example usage
    public static void main(String[] args) {
        String exampleCamel = "ExampleCamelCaseString";
        System.out.println("Converted to snake_case: " + camelToSnake(exampleCamel));
    }
}