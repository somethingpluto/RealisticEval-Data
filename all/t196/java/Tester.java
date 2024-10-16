package org.real.temp;

import org.junit.Test;
import org.junit.Rule;
import org.junit.rules.ExpectedException;

import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Tester {

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    @Test
    public void testGeneratePrimes_SmallLimit() {
        List<Integer> expected = Arrays.asList(2, 3, 5, 7);
        assertEquals(expected, Answer.generatePrimes(10));
    }

    @Test
    public void testGeneratePrimes_PrimeLimit() {
        List<Integer> expected = Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29);
        assertEquals(expected, Answer.generatePrimes(29));
    }

    @Test
    public void testGeneratePrimes_NonPrimeLimit() {
        List<Integer> expected = Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29);
        assertEquals(expected, Answer.generatePrimes(30));
    }

    @Test
    public void testGeneratePrimes_LimitOfTwo() {
        List<Integer> expected = Arrays.asList(2);
        assertEquals(expected, Answer.generatePrimes(2));
    }

    @Test
    public void testGeneratePrimes_InvalidLimit() {
        thrown.expect(IllegalArgumentException.class);
        thrown.expectMessage("Limit must be greater than or equal to 2.");
        Answer.generatePrimes(1);
    }
}