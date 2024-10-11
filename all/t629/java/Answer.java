package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    // Method to find all prime numbers within a given range
    public static List<Integer> findPrimes(int lowerBound, int upperBound) {
        List<Integer> primeNumbers = new ArrayList<>();

        // Loop through the specified range
        for (int number = lowerBound; number <= upperBound; number++) {
            // Check if the number is prime
            if (isPrime(number)) {
                primeNumbers.add(number); // Add to the list if prime
            }
        }

        return primeNumbers; // Return the list of prime numbers
    }

    // Helper method to check if a number is prime
    private static boolean isPrime(int number) {
        if (number <= 1) {
            return false; // 0 and 1 are not prime numbers
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // Not prime if divisible by any number other than 1 and itself
            }
        }
        return true; // Number is prime
    }

    // Example usage
    public static void main(String[] args) {
        int lowerBound = 10;
        int upperBound = 50;
        List<Integer> primes = findPrimes(lowerBound, upperBound);
        System.out.println("Prime numbers between " + lowerBound + " and " + upperBound + ": " + primes);
    }
}