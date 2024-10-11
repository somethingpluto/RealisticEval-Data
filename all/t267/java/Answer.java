package org.real.temp;

public class Answer {

    /**
     * Extracts the second-level and top-level domain names from the fully qualified domain name FQDN and returns them.
     *
     * @param fqdn The fully qualified domain name.
     * @return A string array containing the second-level domain and top-level domain.
     */
    public static String[] extractSldTld(String fqdn) {
        // Split the FQDN using dots
        String[] parts = fqdn.split("\\.");

        // Initialize variables for SLD and TLD
        String sld = "";
        String tld = "";

        // Check if there are at least two parts in the FQDN
        if (parts.length >= 2) {
            // Set the last part as TLD
            tld = parts[parts.length - 1];

            // If there are more than two parts, set the second last part as SLD
            if (parts.length > 2) {
                sld = parts[parts.length - 2];
            } else {
                sld = parts[0];
            }
        }

        // Return the SLD and TLD as an array
        return new String[]{sld, tld};
    }

    public static void main(String[] args) {
        // Example usage of the extractSldTld method
        String[] result = extractSldTld("example.com");
        System.out.println("Second-Level Domain: " + result[0]);
        System.out.println("Top-Level Domain: " + result[1]);
    }
}