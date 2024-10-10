package org.real.temp;

public class Answer {

    /**
     * Determine whether a number is a compliant four-digit number
     *
     * @param number The number to check.
     * @return true if the number is a compliant four-digit number, false otherwise.
     */
    public static boolean isCompliantFourDigit(int number) {
        return number >= 1000 && number <= 9999;
    }
}