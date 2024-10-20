package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testConvertSimpleCamelCase() {
        // Test for a simple camelCase string
        String input = "thisIsTest";
        String expectedOutput = "This is test";
        assertEquals(expectedOutput, camelCaseToCapitalizedWithSpaces(input));
    }

    @Test
    public void testConvertSingleLowercaseWord() {
        // Test for a single word starting with lowercase
        String input = "example";
        String expectedOutput = "Example";
        assertEquals(expectedOutput, camelCaseToCapitalizedWithSpaces(input));
    }

    @Test
    public void testConvertCamelCaseWithMultipleUppercase() {
        // Test for a camelCase string with multiple uppercase letters
        String input = "thisIsAnExampleString";
        String expectedOutput = "This is an example string";
        assertEquals(expectedOutput, camelCaseToCapitalizedWithSpaces(input));
    }

    @Test
    public void testConvertSingleUppercaseLetter() {
        // Test for a single uppercase letter
        String input = "aSingleUppercaseLetterX";
        String expectedOutput = "A single uppercase letter x";
        assertEquals(expectedOutput, camelCaseToCapitalizedWithSpaces(input));
    }

    @Test
    public void testConvertAlreadyCapitalizedString() {
        // Test for an already capitalized string
        String input = "AlreadyCapitalized";
        String expectedOutput = "Already capitalized";
        assertEquals(expectedOutput, camelCaseToCapitalizedWithSpaces(input));
    }
}
