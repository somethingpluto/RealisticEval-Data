package org.real.temp;

public class Answer {

    /**
     * Generates the next sequence in the 'look-and-say' sequence by reading off the digits of the given number,
     * grouping by consecutive digits.
     *
     * @param number The current sequence as a string.
     * @return The next sequence in the 'look-and-say' series.
     */
    public static String lookAndSay(String number) {
        StringBuilder result = new StringBuilder();
        int count = 1;
        int length = number.length();

        // Iterate through the number, group by consecutive digits and count them
        for (int i = 1; i < length; i++) {
            if (number.charAt(i) == number.charAt(i - 1)) {
                count++;
            } else {
                result.append(count).append(number.charAt(i - 1));
                count = 1;
            }
        }

        // Append the last group of digits
        result.append(count).append(number.charAt(length - 1));

        return result.toString();
    }

}
