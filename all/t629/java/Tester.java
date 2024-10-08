package org.real.temp;


import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Tester {

    @Test
    public void testFindPrimesBetween10And50() {
        List<Integer> primes = Answer.findPrimes(10, 50);
        List<Integer> expected = List.of(11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47);
        assertEquals(expected, primes);
    }

    @Test
    public void testFindPrimesInSingleNumberRange() {
        List<Integer> primes = Answer.findPrimes(5, 5);
        List<Integer> expected = List.of(5);
        assertEquals(expected, primes);
    }

    @Test
    public void testFindPrimesInEmptyRange() {
        List<Integer> primes = Answer.findPrimes(1, 1);
        List<Integer> expected = List.of();
        assertEquals(expected, primes);
    }

    @Test
    public void testFindPrimesInNegativeRange() {
        List<Integer> primes = Answer.findPrimes(-10, -1);
        List<Integer> expected = List.of();
        assertEquals(expected, primes);
    }

    @Test
    public void testFindPrimesFromZeroToTen() {
        List<Integer> primes = Answer.findPrimes(0, 10);
        List<Integer> expected = List.of(2, 3, 5, 7);
        assertEquals(expected, primes);
    }

    @Test
    public void testFindPrimesWhereLowerGreaterThanUpper() {
        List<Integer> primes = Answer.findPrimes(10, 5);
        List<Integer> expected = List.of();
        assertEquals(expected, primes);
    }

    @Test
    public void testFindPrimesInRangeStartingFromTwo() {
        List<Integer> primes = Answer.findPrimes(2, 10);
        List<Integer> expected = List.of(2, 3, 5, 7);
        assertEquals(expected, primes);
    }
}