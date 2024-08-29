#include <vector>
#include <stdexcept>

/**
 * @brief Finds all prime numbers less than or equal to the given limit using the Sieve of Eratosthenes algorithm.
 *
 * This function computes all prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
 * The algorithm iteratively marks the multiples of each prime number starting from 2.
 * The remaining unmarked numbers are prime.
 *
 * @param limit The upper bound (inclusive) for finding prime numbers.
 * @return A vector of integers containing all prime numbers less than or equal to the limit.
 * @throws std::invalid_argument if the limit is less than 2.
 */
std::vector<int> sieveOfEratosthenes(int limit) {
    if (limit < 2) {
        throw std::invalid_argument("Limit must be greater than or equal to 2.");
    }

    std::vector<bool> isPrime(limit + 1, true);
    isPrime[0] = isPrime[1] = false;  // 0 and 1 are not prime numbers

    for (int i = 2; i * i <= limit; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                isPrime[j] = false;
            }
        }
    }

    std::vector<int> primes;
    for (int i = 2; i <= limit; ++i) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }

    return primes;
}
