package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    public static List<Integer> findPrimes(int lowerBound, int upperBound) {
        List<Integer> primeNumbers = new ArrayList<>();

        for (int number = lowerBound; number <= upperBound; number++) {
            if (isPrime(number)) {
                primeNumbers.add(number);
            }
        }

        return primeNumbers;
    }

    /* method to compute the sum of primes given a list of prime numbers */
    public static int computeSumOfPrimes(List<Integer> primes) {
        int sum = 0;
        for (int prime : primes) {
            sum += prime;
        }
        return sum;
    }

    /* method to ask if a single number is prime */
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }

        if (num == 2 || num == 3) {
            return true;
        }

        if (num % 2 == 0 || num % 3 == 0) {
            return false;
        }

        for (int i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }

        return true;
    }

}
