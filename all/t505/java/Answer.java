package org.real.temp;

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
        return camelStr.replaceAll("(?<!^)(?=[A-Z])", "_").toLowerCase();
    }

    // Example usage
    public static void main(String[] args) {
        String exampleCamel = "ExampleCamelCaseString";
        System.out.println("Converted to snake_case: " + camelToSnake(exampleCamel));
    }
}