package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Sums up calibration values extracted from the document.
     * Each calibration value is formed by combining the first and last digits of numbers found in each line
     * into a two-digit number.
     *
     * @param calibrationDocument An iterable of strings, each representing a line of text.
     * @return The total sum of all calibration values.
     */
    public static int sumCalibrationValues(List<String> calibrationDocument) {
        int totalSum = 0;

        for (String line : calibrationDocument) {
            // Filter out non-digit characters
            List<Character> digits = new ArrayList<>();
            for (char ch : line.toCharArray()) {
                if (Character.isDigit(ch)) {
                    digits.add(ch);
                }
            }

            // Extract the first and last digits
            if (!digits.isEmpty()) {
                char firstDigit = digits.get(0);
                char lastDigit = digits.get(digits.size() - 1);

                // Combine to form a two-digit number
                int calibrationValue = Character.getNumericValue(firstDigit) * 10 + Character.getNumericValue(lastDigit);

                // Add to the total sum
                totalSum += calibrationValue;
            }
        }

        return totalSum;
    }

    public static void main(String[] args) {
        // Example usage
        List<String> calibrationDocument = new ArrayList<>();
        calibrationDocument.add("abc123xyz");
        calibrationDocument.add("456def");
        calibrationDocument.add("ghi789");

        int result = sumCalibrationValues(calibrationDocument);
        System.out.println("Total Sum: " + result);
    }
}