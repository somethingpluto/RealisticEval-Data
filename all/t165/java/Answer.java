import java.util.Base64;

public class Base64Converter {

    /**
     * Converts a standard Base64 encoded string into a URL-safe Base64 encoded string.
     *
     * @param base64 The standard Base64 encoded string to be converted.
     * @return The URL-safe Base64 encoded string.
     */
    public static String base64ToUrlSafe(String base64) {
        // Replace "+" with "-", "/" with "_", and remove trailing "=" characters
        String urlSafeBase64 = base64
                .replace("+", "-")  // Replace all occurrences of "+" with "-"
                .replace("/", "_")  // Replace all occurrences of "/" with "_"
                .replaceAll("=+$", "");  // Remove any trailing "=" characters

        return urlSafeBase64;
    }

    public static void main(String[] args) {
        String standardBase64 = "SGVsbG8gV29ybGQ="; // Example Base64 string
        String urlSafe = base64ToUrlSafe(standardBase64);
        System.out.println("URL-safe Base64: " + urlSafe);
    }
}