package org.real.temp;
import java.util.regex.Pattern;

public class Answer {
    // Define the regular expression for a valid email
    private static final Pattern emailRegex = Pattern.compile("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$");

    public static boolean isValidEmail(String email) {
        // Test the email against the regular expression
        return emailRegex.matcher(email).matches();
    }

    public static void main(String[] args) {
        // Example usage
        String email = "example@example.com";
        System.out.println(isValidEmail(email)); // Output: true or false
    }
}