package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testCalculateWithValidInput() {
        List<Integer> values = Arrays.asList(1, 2, 3, 4, 5);
        int period = 3;
        double expected = 4.0; // (3 + 4 + 5) / 3
        assertEquals(expected, Answer.calculate(values, period));
    }

    @Test
    public void testCalculateWithAllSameValues() {
        List<Integer> values = Arrays.asList(5, 5, 5, 5, 5);
        int period = 5;
        double expected = 5.0; // (5 + 5 + 5 + 5 + 5) / 5
        assertEquals(expected, Answer.calculate(values, period));
    }

    @Test
    public void testCalculateWithSingleValue() {
        List<Integer> values = Arrays.asList(10);
        int period = 1;
        double expected = 10.0; // (10) / 1
        assertEquals(expected, Answer.calculate(values, period));
    }

    @Test
    public void testCalculateWithInsufficientValues() {
        List<Integer> values = Arrays.asList(1, 2);
        int period = 3;
        assertTrue(Double.isNaN(Answer.calculate(values, period))); // Expecting NaN
    }

    @Test
    public void testCalculateWithEmptyList() {
        List<Integer> values = Arrays.asList();
        int period = 1;
        assertTrue(Double.isNaN(Answer.calculate(values, period))); // Expecting NaN
    }

    @Test
    public void testCalculateWithNegativePeriod() {
        List<Integer> values = Arrays.asList(1, 2, 3, 4, 5);
        int period = -1;
        assertTrue(Double.isNaN(Answer.calculate(values, period))); // Expecting NaN
    }
}