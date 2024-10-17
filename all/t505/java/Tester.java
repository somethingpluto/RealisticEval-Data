package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Test class for verifying the correctness of the camelToSnake method.
 */
public class Tester {

    /**
     * Tests basic CamelCase to snake_case conversion.
     */
    @Test
    public void testBasicConversion() {
        assertEquals("hello_world", camelToSnake("HelloWorld"));
    }

    /**
     * Tests conversion of a CamelCase string with multiple words.
     */
    @Test
    public void testMultipleWords() {
        assertEquals("this_is_a_test", camelToSnake("ThisIsATest"));
    }

    /**
     * Tests conversion with numbers in the string.
     */
    @Test
    public void testWithNumbers() {
        assertEquals("convert_this123_string", camelToSnake("ConvertThis123String"));
    }

    /**
     * Tests conversion with leading uppercase letters.
     */
    @Test
    public void testLeadingUppercase() {
        assertEquals("python_function", camelToSnake("PythonFunction"));
    }

    /**
     * Tests conversion of an empty string.
     */
    @Test
    public void testEmptyString() {
        assertEquals("", camelToSnake(""));
    }

    // Method to be tested
    private String camelToSnake(String camelStr) {
        // Use regular expression to insert underscores before each uppercase letter,
        // and then convert the whole string to lowercase
        return camelStr.replaceAll("(?<!^)(?=[A-Z])", "_").toLowerCase();
    }
}