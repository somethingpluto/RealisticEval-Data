package org.real.temp;

public class Answer {

    /**
     * Align two lines of string to the left, supplementing with Spaces if the length is not enough
     *
     * @param str1 The first string.
     * @param str2 The second string.
     * @return An array containing the aligned strings.
     */
    public static String[] alignLinesLeft(String str1, String str2) {
        // Calculate the maximum length between str1 and str2
        int maxLength = Math.max(str1.length(), str2.length());

        // Create new strings with the same length as the maximum length
        StringBuilder sb1 = new StringBuilder(str1);
        StringBuilder sb2 = new StringBuilder(str2);

        // Append spaces to sb1 until it reaches the maximum length
        while(sb1.length() < maxLength){
            sb1.append(" ");
        }

        // Append spaces to sb2 until it reaches the maximum length
        while(sb2.length() < maxLength){
            sb2.append(" ");
        }

        // Return an array containing the aligned strings
        return new String[]{sb1.toString(), sb2.toString()};
    }
}