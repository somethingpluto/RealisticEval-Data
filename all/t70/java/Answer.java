package org.real.temp;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Extracts all code block contents from a markdown string.
     *
     * @param markdownString The input markdown string.
     * @return A list of strings, each representing the content of a code block.
     *         Returns an empty list if no code blocks are found.
     */
    public static List<String> codeBlockRemover(String markdownString) {
        // Define a pattern that captures content within triple backticks, with optional language specifier
        String pattern = "```[a-zA-Z]*\n(.*?)```";

        // Compile the regular expression pattern
        Pattern compiledPattern = Pattern.compile(pattern, Pattern.DOTALL);

        // Find all occurrences of the pattern
        Matcher matcher = compiledPattern.matcher(markdownString);

        // List to store the extracted code blocks
        List<String> codeBlocks = new ArrayList<>();

        while (matcher.find()) {
            // Add the content of the code block to the list
            codeBlocks.add(matcher.group(1));
        }

        return codeBlocks;
    }

    public static void main(String[] args) {
        // Example usage
        String markdownString = "Some text\n```\npublic class Example {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}\n```\nMore text";
        List<String> codeBlocks = codeBlockRemover(markdownString);
        for (String codeBlock : codeBlocks) {
            System.out.println(codeBlock);
        }
    }
}