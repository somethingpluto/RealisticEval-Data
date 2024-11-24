package org.real.temp;

public class Answer {

    /**
     * Converts a snake_case string to CamelCase.
     *
     * @param snakeStr The snake_case string to convert.
     * @return The converted CamelCase string.
     */
    public static String snakeToCamel(String snakeStr) {
        // Split the snake_case string into words
        String[] words = snakeStr.split("_");

        // Capitalize the first letter of each word and join them
        StringBuilder camelCaseStr = new StringBuilder();
        for (String word : words) {
            if (!word.isEmpty()) {
                camelCaseStr.append(Character.toUpperCase(word.charAt(0)));
                camelCaseStr.append(word.substring(1));
            }
        }
        return camelCaseStr.toString();
    }

    // Example usage
    public static void main(String[] args) {
        String snakeStr = "example_snake_case_string";
        String camelCaseStr = snakeToCamel(snakeStr);
        System.out.println(camelCaseStr); // Output: ExampleSnakeCaseString
    }
}