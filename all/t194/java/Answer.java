package org.real.temp;

public class Answer {
    /**
     * @brief Returns a copy of the specified string.
     * 
     * @param str The input string to be copied.
     * @return A new string that is a copy of the input string.
     * @throws IllegalArgumentException if the input string is null.
     */
    public String returnString(String str) {
        if (str == null) {
            throw new IllegalArgumentException("Input string cannot be null.");
        }

        // Return a new string that is a copy of the input string
        return new String(str);
    }
}