package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for converting snake_case strings to CamelCase.
 */
public class Tester {

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

    @Test
    public void testBasicConversion() {
        // Test basic snake_case to CamelCase conversion
        assertEquals("HelloWorld", snakeToCamel("hello_world"));
    }

    @Test
    public void testMultipleWords() {
        // Test conversion of a snake_case string with multiple words
        assertEquals("ThisIsATest", snakeToCamel("this_is_a_test"));
    }

    @Test
    public void testWithNumbers() {
        // Test conversion with numbers in the string
        assertEquals("ConvertThis123String", snakeToCamel("convert_this_123_string"));
    }

    @Test
    public void testLeadingTrailingUnderscores() {
        // Test conversion with leading and trailing underscores
        assertEquals("LeadingAndTrailing", snakeToCamel("_leading_and_trailing_"));
        assertEquals("MultipleUnderscores", snakeToCamel("___multiple___underscores___"));
    }

    @Test
    public void testEmptyString() {
        // Test conversion of an empty string
        assertEquals("", snakeToCamel(""));
    }
}