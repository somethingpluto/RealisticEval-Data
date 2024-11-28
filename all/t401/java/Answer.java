package org.real.temp;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Find and return a list of all placeholders in the format {{ placeholder }} from the input text.
     *
     * @param text The input string containing potential placeholders.
     * @return A list of matching placeholders.
     */
    public static List<String> findPlaceholders(String text) {
        // Use a regular expression to find placeholders in the specified format
        List<String> placeholders = new ArrayList<>();
        Pattern pattern = Pattern.compile("\\{\\{\\s*([\\w]+)\\s*}}");
        Matcher matcher = pattern.matcher(text);

        while (matcher.find()) {
            placeholders.add(matcher.group(1));
        }

        return placeholders;
    }

    // Example usage
    public static void main(String[] args) {
        String exampleText = "Hello, {{name}}! Welcome to {{place}}.";
        List<String> placeholders = findPlaceholders(exampleText);
        System.out.println(placeholders);
    }
}