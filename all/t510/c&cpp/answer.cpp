#include <iostream>
#include <utility>  // For std::pair
#include <stdexcept>  // For std::invalid_argument

// Function to find the powers of 2 and 3 that multiply to produce the given number
std::pair<int, int> find_powers(int num) {
    // Input validation
    if (num <= 0) {
        throw std::invalid_argument("Input must be a positive integer greater than zero.");
    }

    int n = 0;  // Counter for powers of 2
    int m = 0;  // Counter for powers of 3

    // Count the power of 2 in the factorization
    while (num % 2 == 0) {
        n++;
        num /= 2;
    }

    // Count the power of 3 in the factorization
    while (num % 3 == 0) {
        m++;
        num /= 3;
    }

    // If num is reduced to 1, only 2's and 3's were factors
    if (num == 1) {
        return std::make_pair(n, m);
    } else {
        return std::make_pair(-1, -1);  // Use (-1, -1) to indicate other prime factors
    }
}