package org.real.temp;

/**
 * Determines whether a given number is a compliant four-digit number.
 * A compliant number is defined as being between 1000 and 9999, inclusive.
 */
public class Answer {

    /**
     * Checks if the provided number is a compliant four-digit number.
     *
     * @param number The number to check.
     * @return true if the number is a compliant four-digit number, false otherwise.
     */
    public static boolean isCompliantFourDigit(int number) {
        // Ensures the function processes only integers within the specified range
        return number >= 1000 && number <= 9999;
    }

    // Example usage
    public static void main(String[] args) {
        System.out.println(isCompliantFourDigit(1234)); // true
        System.out.println(isCompliantFourDigit(999));  // false
        System.out.println(isCompliantFourDigit(10000));// false
    }
}