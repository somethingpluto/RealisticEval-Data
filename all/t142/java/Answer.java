package org.real.temp;

public class Answer {
    public static String camelCaseToCapitalizedWithSpaces(String input) {
        // Use a regular expression to insert spaces before capital letters and numbers
        String spacedString = input.replaceAll("([A-Z0-9])", " $1");

        // Capitalize the first letter of each word
        String[] words = spacedString.split(" ");
        StringBuilder capitalizedString = new StringBuilder();

        for (String word : words) {
            if (word.length() > 0) {
                capitalizedString.append(Character.toUpperCase(word.charAt(0)))
                                 .append(word.substring(1))
                                 .append(" ");
            }
        }

        // Trim any leading spaces and return the result
        return capitalizedString.toString().trim();
    }

    public static void main(String[] args) {
        String input = "thisIsAnExample123";
        String result = camelCaseToCapitalizedWithSpaces(input);
        System.out.println(result); // Output: "This Is An Example 123"
    }
}