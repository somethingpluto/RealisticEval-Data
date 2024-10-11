import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testSumCalibrationValues() {
        // Test data
        String[] calibrationDocument = {"1abc2", "3def4ghi5"};
        
        // Call the method under test
        int result = sumCalibrationValues(calibrationDocument);
        
        // Assert the expected outcome
        assertEquals(100, result);  // Assuming that 12 + 45 should give 57
    }

    /**
     * Sums up calibration values extracted from the document.
     * Each calibration value is formed by combining the first and last digits of numbers found in each line
     * into a two-digit number.
     *
     * @param calibrationDocument An array of strings, each representing a line of text.
     * @return The total sum of all calibration values.
     */
    private int sumCalibrationValues(String[] calibrationDocument) {
        int sum = 0;
        for (String line : calibrationDocument) {
            int firstDigit = Character.getNumericValue(line.charAt(0));
            int lastDigit = Character.getNumericValue(line.charAt(line.length() - 1));
            sum += firstDigit * 10 + lastDigit;
        }
        return sum;
    }
}