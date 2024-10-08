package org.real.temp;
import org.junit.jupiter.api.Test;

import org.real.temp.*;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class Tester {
    @Test
    public void testFindPrimesInRange() {
        List<Integer> expected = Arrays.asList(2, 3, 5, 7, 11);
        assertEquals(expected, Answer.findPrimes(1, 12), "Check primes between 1 and 12");
    }

    @Test
    public void testFindPrimesSinglePrime() {
        List<Integer> expected = Arrays.asList(29);
        assertEquals(expected, Answer.findPrimes(29, 29), "Check single prime number");
    }

    @Test
    public void testFindPrimesInBigRange() {
        List<Integer> expected = Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97);
        assertEquals(expected, Answer.findPrimes(1, 100), "Check primes between 1 and 100");
    }

    @Test
    public void testFindPrimesNoPrimes() {
        List<Integer> expected = Arrays.asList();
        assertEquals(expected, Answer.findPrimes(0, 1), "Check range with no primes");
    }

}
