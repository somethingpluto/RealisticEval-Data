package org.real.temp;

public class Answer {

    /**
     * Align two lines of string to the left, supplementing with spaces if the length is not enough.
     *
     * @param str1 the first string
     * @param str2 the second string
     * @return a pair of aligned strings (aligned str1, aligned str2)
     */
    public static String[] alignLinesLeft(String str1, String str2) {
        // Determine the maximum length of the two strings
        int maxLength = Math.max(str1.length(), str2.length());

        // Align both strings to the left by padding with spaces
        String alignedStr1 = String.format("%-" + maxLength + "s", str1);
        String alignedStr2 = String.format("%-" + maxLength + "s", str2);

        return new String[]{alignedStr1, alignedStr2};
    }

    public static void main(String[] args) {
        String[] result = alignLinesLeft("Hello", "World!");
        System.out.println(result[0]); // Prints: Hello    
        System.out.println(result[1]); // Prints: World!  
    }
}