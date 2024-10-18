package org.real.temp;

/**
 * Extracts the username and mailbox suffix from an email address.
 */
public class Answer {

    /**
     * Extracts the username and domain from an email address.
     *
     * @param email the email address to extract details from
     * @return a String array containing the username and domain
     * @throws IllegalArgumentException if the email does not contain an '@' character
     */
    public static String[] extractEmailDetails(String email) {
        // Check if '@' is in the email
        if (!email.contains("@")) {
            throw new IllegalArgumentException("Invalid email address. Email must contain an '@' character.");
        }

        // Split the email at the '@' and assign parts to username and domain
        String[] parts = email.split("@", 2);
        String username = parts[0];
        String domain = parts[1];

        return new String[]{username, domain};
    }

    // A simple check function to verify the correctness of the extractEmailDetails method
    public static void main(String[] args) {
        try {
            String[] result = extractEmailDetails("xxx@gmail.com");
            System.out.println("Username: " + result[0] + ", Domain: " + result[1]);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}