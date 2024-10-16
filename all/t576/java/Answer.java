package org.real.temp;
public class Answer {
    public static String hideBankAccount(String account) {
        // Validate that the account number is exactly 17 characters long
        if (account.length() != 17) {
            throw new IllegalArgumentException("Account number must be exactly 17 characters long.");
        }

        // Create the hidden representation with "****" prefix
        String hiddenPart = "****";

        // Extract the visible part of the account number (last 4 characters)
        String visiblePart = account.substring(13); // Get last 4 characters

        // Return the formatted string with hidden and visible parts
        return hiddenPart + visiblePart;
    }
}