public class StringTruncator {
    public static String truncateStringWithReplacement(String str, int maxLength) {
        // Check if the string length is less than or equal to the specified length
        if (str.length() <= maxLength) {
            return str; // No need to truncate
        }

        // Replace the excess part with ellipsis
        return str.substring(0, maxLength) + "...";
    }

    public static void main(String[] args) {
        String original = "This is a long string that needs to be truncated.";
        int maxLength = 20;

        String truncated = truncateStringWithReplacement(original, maxLength);
        System.out.println(truncated); // Output: This is a long str...
    }
}