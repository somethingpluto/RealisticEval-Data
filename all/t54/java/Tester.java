package org.real.temp;

import org.junit.Test; // JUnit 4 Test annotation
import static org.junit.Assert.assertEquals; // JUnit 4 assertion method
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testRemoveTripleBackticksBasic() {
        // Test basic functionality
        List<String> inputStrings = Arrays.asList("Here is ```code``` example", "Another ```example``` here", "No backticks here");
        List<String> expectedOutput = Arrays.asList("Here is code example", "Another example here", "No backticks here");
        assertEquals(expectedOutput, removeTripleBackticks(inputStrings));
    }

    @Test
    public void testStringsWithMultipleInstances() {
        // Test strings containing multiple instances of triple backticks
        List<String> inputStrings = Arrays.asList("Multiple ```backticks``` in ```one``` string");
        List<String> expectedOutput = Arrays.asList("Multiple backticks in one string");
        assertEquals(expectedOutput, removeTripleBackticks(inputStrings));
    }

    @Test
    public void testEmptyStrings() {
        // Test with empty strings
        List<String> inputStrings = Arrays.asList("");
        List<String> expectedOutput = Arrays.asList("");
        assertEquals(expectedOutput, removeTripleBackticks(inputStrings));
    }

    @Test
    public void testNoTripleBackticks() {
        // Test strings that do not contain triple backticks
        List<String> inputStrings = Arrays.asList("Just a normal string", "Another normal string");
        List<String> expectedOutput = Arrays.asList("Just a normal string", "Another normal string");
        assertEquals(expectedOutput, removeTripleBackticks(inputStrings));
    }

    @Test
    public void testEdgeCases() {
        // Test edge cases like strings made entirely of triple backticks
        List<String> inputStrings = Arrays.asList("```", "```more```", "text``````");
        List<String> expectedOutput = Arrays.asList("", "more", "text");
        assertEquals(expectedOutput, removeTripleBackticks(inputStrings));
    }
}
