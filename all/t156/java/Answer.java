/**
 * Format the number into a more readable string representation, returning the original form if the number is less than 1,000.
 * If it is greater than or equal to a thousand and less than a million, it is formatted as "x.xK".
 * For a million or more, format it as "x.xM".
 *
 * @param num The number to be formatted.
 * @return The formatted number as a string.
 */
public class NumberFormatter {
    public static String formatNumber(double num) {
        if (num >= 1_000_000) {
            return String.format("%.1fM", num / 1_000_000);
        } else if (num >= 1_000) {
            return String.format("%.1fK", num / 1_000);
        } else {
            return String.valueOf(num);
        }
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(formatNumber(1500));      // Output: 1.5K
        System.out.println(formatNumber(2500000));   // Output: 2.5M
        System.out.println(formatNumber(500));        // Output: 500.0
    }
}