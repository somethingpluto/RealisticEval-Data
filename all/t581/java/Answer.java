package org.real.temp;

/**
 * Abbreviates a number to a string with a suffix based on its magnitude.
 *
 * @param number - The number to abbreviate.
 * @return - The abbreviated string representation of the number.
 */
public class Answer {
    public static String abbreviateNumber(double number) {
        // If the number is less than 1000, return it as is.
        if (number < 1000) {
            return String.valueOf(number);
        }

        // Determine the tier of the number based on its magnitude.
        int tier = (int) Math.floor(Math.log10(number) / 3);

        // Define suffixes for each tier.
        String[] suffixes = {"", "k", "M", "B", "T"};

        // Calculate the base number by dividing by the corresponding power of ten.
        double baseNumber = number / Math.pow(10, tier * 3);

        // Round the base number to one decimal place.
        double roundedNumber = Math.round(baseNumber * 10) / 10.0;

        // Return the number with its corresponding suffix.
        return roundedNumber + suffixes[tier];
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(abbreviateNumber(123));          // Output: 123.0
        System.out.println(abbreviateNumber(1234));         // Output: 1.2k
        System.out.println(abbreviateNumber(1234567));      // Output: 1.2M
        System.out.println(abbreviateNumber(1234567890));   // Output: 1.2B
    }
}