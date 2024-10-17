package org.real.temp;

public class Answer {

    /**
     * Converts the string representation of a score to its decimal value.
     *
     * @param scoreStr The score as a string, can be a decimal or a fraction (e.g., "2.5", "10/4")
     * @return The decimal value of the score as a double, or null if the input is invalid
     */
    public static Double convertScoreToDecimal(String scoreStr) {
        try {
            // Check if the score is a fraction
            if (scoreStr.contains("/")) {
                String[] parts = scoreStr.split("/");
                if (parts.length == 2) {
                    double numerator = Double.parseDouble(parts[0]);
                    double denominator = Double.parseDouble(parts[1]);
                    return numerator / denominator;
                } else {
                    throw new IllegalArgumentException("Invalid fraction format");
                }
            } else {
                // Otherwise, treat it as a decimal
                return Double.parseDouble(scoreStr);
            }

        } catch (NumberFormatException | ArithmeticException e) {
            System.out.println("Error converting '" + scoreStr + "' to decimal: " + e.getMessage());
            return null;
        }
    }

    public static void main(String[] args) {
        // Example usage
        String scoreStr = "10/4";
        Double result = convertScoreToDecimal(scoreStr);
        System.out.println("Converted score: " + result);

        scoreStr = "2.5";
        result = convertScoreToDecimal(scoreStr);
        System.out.println("Converted score: " + result);

        scoreStr = "invalid";
        result = convertScoreToDecimal(scoreStr);
        System.out.println("Converted score: " + result);
    }
}