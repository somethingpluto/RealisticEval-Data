package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testBasicCalculations() {
        // Test with a simple input where lines contain at least two digits
        List<String> document = new ArrayList<>();
        document.add("Reading 1234 calibration");
        document.add("Measure 5678 complete");
        document.add("End of data 91011");

        int expectedSum = 163;
        int actualSum = sumCalibrationValues(document);

        assertEquals(expectedSum, actualSum);
    }

    @Test
    public void testNoDigits() {
        // Test lines with no digits
        List<String> document = new ArrayList<>();
        document.add("No numbers here");
        document.add("Still no numbers");

        int expectedSum = 0;
        int actualSum = sumCalibrationValues(document);

        assertEquals(expectedSum, actualSum);
    }

    @Test
    public void testEmptyLines() {
        // Test with empty lines or lines with spaces
        List<String> document = new ArrayList<>();
        document.add("");
        document.add("   ");

        int expectedSum = 0;
        int actualSum = sumCalibrationValues(document);

        assertEquals(expectedSum, actualSum);
    }

    @Test
    public void testMixedContent() {
        // Test with a mixture of valid and invalid lines
        List<String> document = new ArrayList<>();
        document.add("Good line 1524 end");
        document.add("Bad line");
        document.add("Another good line 7681");

        int expectedSum = 85;
        int actualSum = sumCalibrationValues(document);

        assertEquals(expectedSum, actualSum);
    }
}