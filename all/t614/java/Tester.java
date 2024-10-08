package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.List;

public class Tester {

    @Test
    public void testCalculateAverageDifference_PositiveIntegers() {
        List<Integer> numbers = List.of(10, 20, 30, 40);
        double result = Answer.calculateAverageDifference(numbers);
        double expected = 10.0;
        assertEquals(expected, result, "The average difference should be 10.0");
    }

    @Test
    public void testCalculateAverageDifference_MixedPositiveAndNegative() {
        List<Integer> numbers = List.of(-10, 0, 10, 20);
        double result = Answer.calculateAverageDifference(numbers);
        double expected = 10.0;
        assertEquals(expected, result, "The average difference should be 10.0");
    }

    @Test
    public void testCalculateAverageDifference_SameValues() {
        List<Integer> numbers = List.of(5, 5, 5, 5);
        double result = Answer.calculateAverageDifference(numbers);
        double expected = 0.0;
        assertEquals(expected, result, "The average difference should be 0.0 as all values are the same");
    }

    @Test
    public void testCalculateAverageDifference_SingleElement() {
        List<Integer> numbers = List.of(100);
        double result = Answer.calculateAverageDifference(numbers);
        double expected = 0.0;  // Not enough data to calculate differences
        assertEquals(expected, result, "The average difference should be 0.0 for a single element list");
    }

    @Test
    public void testCalculateAverageDifference_EmptyList() {
        List<Integer> numbers = List.of();
        double result = Answer.calculateAverageDifference(numbers);
        double expected = 0.0;  // Not enough data to calculate differences
        assertEquals(expected, result, "The average difference should be 0.0 for an empty list");
    }

    @Test
    public void testCalculateAverageDifference_NegativeIntegers() {
        List<Integer> numbers = List.of(-5, -10, -15, -20);
        double result = Answer.calculateAverageDifference(numbers);
        double expected = -5.0;
        assertEquals(expected, result, "The average difference should be -5.0 for negative integers");
    }

}