package org.real.temp;

import java.util.regex.Pattern;

public class Answer {
    public static boolean isValidPassword(String password) {
        // Regular expression patterns for the required criteria
        Pattern hasNumber = Pattern.compile("[0-9]");                          // At least one number
        Pattern hasLowercase = Pattern.compile("[a-z]");                       // At least one lowercase letter
        Pattern hasUppercase = Pattern.compile("[A-Z]");                       // At least one uppercase letter
        Pattern hasPunctuation = Pattern.compile("[!@#$%^&*(),.?\":{}|<>]");   // At least one punctuation mark
        Pattern hasMinimumLength = Pattern.compile(".{8,}");                   // At least 8 characters

        // Check each condition
        boolean isValid = hasNumber.matcher(password).find() &&
                          hasLowercase.matcher(password).find() &&
                          hasUppercase.matcher(password).find() &&
                          hasPunctuation.matcher(password).find() &&
                          hasMinimumLength.matcher(password).find();

        return isValid;
    }
}