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
    public void testFindPrimesNoPrimes() {
        List<Integer> expected = Arrays.asList();
        assertEquals(expected, Answer.findPrimes(0, 1), "Check range with no primes");
    }

    @Test
    public void testComputeSumOfPrimes() {
        List<Integer> primes = Arrays.asList(2, 3, 5, 7);
        int expectedSum = 17;
        assertEquals(expectedSum, Answer.computeSumOfPrimes(primes), "Sum of first four primes");
    }

    @Test
    public void testIsPrime() {
        assertTrue(Answer.isPrime(23), "Check if 23 is prime");
        assertFalse(Answer.isPrime(25), "Check if 25 is not prime");
    }

}
