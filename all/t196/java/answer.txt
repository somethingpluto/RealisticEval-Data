package org.real.temp;

import java.util.ArrayList;
import java.util.List;

/**
 * @brief Find all prime numbers that are less than or equal to limit using the Eichler sieve algorithm
 *
 * @param limit The upper bound (inclusive) for finding prime numbers.
 * @return A list of integers containing all prime numbers less than or equal to the limit.
 * @throws IllegalArgumentException if the limit is less than 2.
 */
public class Answer {
    public static List<Integer> generatePrimes(int limit) {
        if (limit < 2) {
            throw new IllegalArgumentException("Limit must be greater than or equal to 2.");
        }

        boolean[] isPrime = new boolean[limit + 1];
        for (int i = 2; i <= limit; i++) {
            isPrime[i] = true; // Initialize all numbers as prime
        }
        isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime numbers

        for (int i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= limit; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        return primes;
    }
}