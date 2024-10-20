package org.real.temp;

public class Answer {

    /**
     * Extracts the second-level domain (SLD) and top-level domain (TLD) from a fully qualified domain name (FQDN).
     *
     * @param fqdn The fully qualified domain name.
     * @return A pair containing the second-level domain and top-level domain.
     * @throws IllegalArgumentException if the provided FQDN does not contain enough parts to extract SLD and TLD.
     */
    public static Pair<String, String> extractSldTld(String fqdn) {
        // Split the FQDN into parts
        String[] parts = fqdn.split("\\.");

        // Check if there are enough parts to extract SLD and TLD
        if (parts.length < 2) {
            throw new IllegalArgumentException("The provided FQDN does not contain enough parts to extract SLD and TLD.");
        }

        // Extract the SLD and TLD
        String sld = parts[parts.length - 2];  // Second to last item is the SLD
        String tld = parts[parts.length - 1];  // Last item is the TLD

        return new Pair<>(sld, tld);
    }

    // Utility class to hold a pair of values
    public static class Pair<T1, T2> {
        private T1 first;
        private T2 second;

        public Pair(T1 first, T2 second) {
            this.first = first;
            this.second = second;
        }

        public T1 getFirst() {
            return first;
        }

        public T2 getSecond() {
            return second;
        }
    }

    public static void main(String[] args) {
        // Example usage
        try {
            Pair<String, String> result = extractSldTld("example.com");
            System.out.println("SLD: " + result.getFirst());
            System.out.println("TLD: " + result.getSecond());
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}