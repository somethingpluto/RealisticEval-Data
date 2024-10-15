package org.real.temp;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class Tester {

    @Test
    public void testConvertCamelCaseToSentence() {
        // Test for a simple camelCase string
        String input1 = "thisIsTest";
        String expectedOutput1 = "This is test";
        assertEquals(expectedOutput1, StringFormatter.camelCaseToCapitalizedWithSpaces(input1));

        // Test for a single word starting with lowercase
        String input2 = "example";
        String expectedOutput2 = "Example";
        assertEquals(expectedOutput2, StringFormatter.camelCaseToCapitalizedWithSpaces(input2));

        // Test for a camelCase string with multiple uppercase letters
        String input3 = "thisIsAnExampleString";
        String expectedOutput3 = "This is an example string";
        assertEquals(expectedOutput3, StringFormatter.camelCaseToCapitalizedWithSpaces(input3));

        // Test for a single uppercase letter
        String input4 = "aSingleUppercaseLetterX";
        String expectedOutput4 = "A single uppercase letter x";
        assertEquals(expectedOutput4, StringFormatter.camelCaseToCapitalizedWithSpaces(input4));

        // Test for an already capitalized string
        String input5 = "AlreadyCapitalized";
        String expectedOutput5 = "Already capitalized";
        assertEquals(expectedOutput5, StringFormatter.camelCaseToCapitalizedWithSpaces(input5));
    }
}