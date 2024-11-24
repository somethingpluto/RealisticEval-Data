#include <iostream>
#include <vector>
#include <cmath> // For std::tgamma

// Function to calculate factorial
long long factorial(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

// Function to calculate binomial coefficient (n choose k)
long long binomialCoefficient(int n, int k) {
    return factorial(n) / (factorial(k) * factorial(n - k));
}

// Function to generate the ith row of Pascal's Triangle
std::vector<long long> pascal_triangle_row(int i) {
    std::vector<long long> row(i + 1, 0); // Initialize vector with zeros
    for (int k = 0; k <= i; ++k) {
        row[k] = binomialCoefficient(i, k);
    }
    return row;
}
