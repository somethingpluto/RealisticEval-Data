public class BitValidator {
    /**
     * Determines whether a given string (assumed to end with ".bit") is a valid 3-digit integer.
     *
     * @param bitName The string to validate.
     * @return True if the remaining part after removing ".bit" is a valid 3-digit integer, otherwise false.
     */
    public static boolean assert999(String bitName) {
        // Remove the ".bit" suffix from the string
        String numericString = bitName.replace(".bit", "");

        // Regular expression to ensure the string is a 1 to 3 digit number
        String regex = "^[0-9]{1,3}$";

        // Convert the remaining part to an integer
        try {
            int num = Integer.parseInt(numericString);
            // Check if the string matches the regex and if the number is within the valid range
            return numericString.matches(regex) && num >= 0 && num <= 999;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}