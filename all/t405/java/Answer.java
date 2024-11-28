package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Removes parts of each string in the given array.
     * Specifically, it removes all characters before the first uppercase letter,
     * then removes all characters before the first lowercase letter from the remaining string.
     *
     * @param strings An array of strings to process.
     * @return A list containing the processed strings.
     */
    public static List<String> removePartsOfStrings(String... strings) {
        List<String> results = new ArrayList<>();
        for (String string : strings) {
            try {
                // Remove all characters before the first uppercase letter
                int indexUpper = findFirstUppercaseIndex(string);
                String tempString = string.substring(indexUpper);

                // Remove all characters before the first lowercase letter
                int indexLower = findFirstLowercaseIndex(tempString);
                String resultString = tempString.substring(indexLower - 1);

                results.add(resultString);
            } catch (IndexOutOfBoundsException e) {
                // Handle cases where no uppercase or lowercase letters are found
                results.add(string);  // You may decide to append an empty string or an error message
            }
        }
        return results;
    }

    private static int findFirstUppercaseIndex(String str) {
        for (int i = 0; i < str.length(); i++) {
            if (Character.isUpperCase(str.charAt(i))) {
                return i;
            }
        }
        throw new IndexOutOfBoundsException("No uppercase letter found");
    }

    private static int findFirstLowercaseIndex(String str) {
        for (int i = 0; i < str.length(); i++) {
            if (Character.isLowerCase(str.charAt(i))) {
                return i;
            }
        }
        throw new IndexOutOfBoundsException("No lowercase letter found");
    }

    public static void main(String[] args) {
        List<String> results = removePartsOfStrings("HelloWorld", "JavaProgramming", "12345abcDEF");
        results.forEach(System.out::println);
    }
}