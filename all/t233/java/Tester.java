package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testRemoveComments() {
        String input = "Hello, world! # This is a comment";
        String expectedOutput = "Hello, world!";

        String actualOutput = removeComments(input);

        assertEquals(expectedOutput, actualOutput);
    }

    public String removeComments(String string) {
        // Implementation of the method goes here
        return string.replaceAll("#.*", "");
    }
}