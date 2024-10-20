package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Answer {

    /**
     * Transforms the input text by finding and modifying patterns that match the format '(...)'.
     * Specifically, it removes any asterisks inside the parentheses while preserving the outer format.
     * 
     * For example:
     * input: hello
     * output: hello
     *
     * @param text The input text containing patterns to be transformed.
     * @return The transformed text with asterisks inside '(*...*)' patterns removed.
     */
    public static String removeInnerAsterisks(String text) {
        // Regular expression to find patterns like (*...*)
        Pattern pattern = Pattern.compile("\\(\\*(.*?)\\*\\)");
        Matcher matcher = pattern.matcher(text);
        
        // Use StringBuffer to construct the new string
        StringBuffer result = new StringBuffer();

        while (matcher.find()) {
            // Get the content between the asterisks
            String content = matcher.group(1).replace("*", "");
            // Replace the matched pattern with the modified content
            matcher.appendReplacement(result, "(*" + content + "*)");
        }
        
        // Append the remaining part of the string
        matcher.appendTail(result);
        
        return result.toString();
    }

    // Example usage
    public static void main(String[] args) {
        String[] testCases = {
            "*he*l*lo*",                  // No parentheses, should return original
            "Hello (*w*o*r*l*d*)!",       // Removes inner asterisks: "Hello (*world*)!"
            "This is a test (*a*b*c*)",   // Removes inner asterisks: "This is a test (*abc*)"
            "No asterisks here",           // No patterns to replace, should return original
            "Multiple patterns (*x*y*z*) and (*a*b*)", // "Multiple patterns (*xyz*) and (*ab*)"
        };
        
        for (String text : testCases) {
            String result = removeInnerAsterisks(text);
            System.out.println("Original: '" + text + "' => Transformed: '" + result + "'");
        }
    }
}
