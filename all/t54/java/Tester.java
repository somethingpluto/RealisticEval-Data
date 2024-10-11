package org.real.temp;

import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;
import org.junit.Test;

public class Tester {

    /**
     * Processes a list of strings, removing the three consecutive backticks from each string.
     *
     * @param stringList The list of strings to process.
     * @return A new list with all instances of three consecutive backticks removed from each string.
     */
    public List<String> removeTripleBackticks(List<String> stringList) {
        return stringList.stream()
                         .map(s -> s.replaceAll("```", ""))
                         .toList();
    }

    @Test
    public void testRemoveTripleBackticks() {
        // Test case 1
        List<String> input1 = Arrays.asList("This is a ```test``` string.");
        List<String> expectedOutput1 = Arrays.asList("This is a test string.");
        assertEquals(expectedOutput1, removeTripleBackticks(input1));

        // Test case 2
        List<String> input2 = Arrays.asList("No triple backticks here!");
        List<String> expectedOutput2 = Arrays.asList("No triple backticks here!");
        assertEquals(expectedOutput2, removeTripleBackticks(input2));

        // Test case 3
        List<String> input3 = Arrays.asList("````This is a test```string.", "Another ```test```");
        List<String> expectedOutput3 = Arrays.asList("`This is a teststring.", "Another `test`");
        assertEquals(expectedOutput3, removeTripleBackticks(input3));
    }
}