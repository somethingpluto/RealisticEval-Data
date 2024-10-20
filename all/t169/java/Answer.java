package org.real.temp;
/**
 * Converts an Arabic numeral to its Roman numeral equivalent.
 *
 * @param num The number to convert.
 * @return The Roman numeral representation of the input number.
 * @throws IllegalArgumentException Will throw an error if the input is not a positive integer.
 */
public class Answer {
    public static String convertToRoman(int num) {
        if (num <= 0) {
            throw new IllegalArgumentException("Input must be a positive integer");
        }

        String[] romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] romanValues = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < romanNumerals.length; i++) {
            while (num >= romanValues[i]) {
                result.append(romanNumerals[i]);
                num -= romanValues[i];
            }
        }

        return result.toString();
    }
}