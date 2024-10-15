package org.real.temp;
import java.util.regex.Pattern;

public class Answer {

    public static boolean isValidUsername(String username) {
        // Define the regular expression for a valid username
        String usernameRegex = "^[a-zA-Z0-9_]+$";
        
        // Compile the regex pattern
        Pattern pattern = Pattern.compile(usernameRegex);
        
        // Test the username against the regular expression
        return pattern.matcher(username).matches();
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(isValidUsername("valid_username123")); // true
        System.out.println(isValidUsername("invalid-username!")); // false
    }
}