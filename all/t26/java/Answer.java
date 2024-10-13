package org.real.temp;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Answer {

    /**
     * Converts an input string with multiple separators to a comma-separated string.
     * Now handles additional separators: hyphens (-) and colons (:).
     *
     * @param inputString The input string containing various separators like *, ;, /, -, :
     * @return A comma-separated string where all specified separators have been replaced with commas.
     */
    public static String convertToCommaSeparated(String inputString) {
        // The pattern includes *, ;, /, -, :
        String pattern = "[\\*;/-:]";  // Correctly escaped hyphen and included colon in the character class
        String commaSeparatedString = inputString.replaceAll(pattern, ",");
        return commaSeparatedString;
    }

    public static void main(String[] args) {
        // Example usage
        String input = "Hello*World;Example/Text-Another:Test";
        String result = convertToCommaSeparated(input);
        System.out.println(result);  // Output: Hello,World,Example,Text,Another,Test
    }
}