package org.real.temp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Answer {
    /**
     * Processes a list of strings, removing all occurrences of three consecutive backticks from each string.
     *
     * @param stringList The list of strings to process.
     * @return A new list with all instances of three consecutive backticks removed from each string.
     */
    public static List<String> removeTripleBackticks(List<String> stringList) {
        // Use a stream to process each string in the list by removing three consecutive backticks
        List<String> processedList = new ArrayList<>();
        for (String s : stringList) {
            processedList.add(s.replace("```", ""));
        }
        return processedList;
    }

    public static void main(String[] args) {
        // Example usage
        List<String> exampleList = Arrays.asList("```example```", "test```code```", "no```backticks");
        List<String> resultList = removeTripleBackticks(exampleList);
        System.out.println(resultList); // Output: [example, testcode, nobackticks]
    }
}