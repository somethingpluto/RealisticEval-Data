#include <iostream>
#include <cmath>
#include <cassert>

// Function to calculate the binomial coefficient
long long binomial_coefficient(int n, int k) {
    if (k > n - k) {
        k = n - k;
    }
    long long result = 1;
    for (int i = 0; i < k; ++i) {
        result *= (n - i);
        result /= (i + 1);
    }
    return result;
}

// Function to calculate the probability of drawing n red balls
double probability_of_red_balls(int n, int x, int y) {
    const int N = 15;  // Total number of draws
    double p = static_cast<double>(x) / (x + y);  // Probability of drawing a red ball

    // Calculate the probability using the binomial formula
    double probability = binomial_coefficient(N, n) * std::pow(p, n) * std::pow(1 - p, N - n);
    return probability;
}

// Function to check the correctness of the probability_of_red_balls function
void check_probability_of_red_balls() {
    assert(std::abs(probability_of_red_balls(3, 7, 8) - 0.224669) < 1e-6);
    assert(std::abs(probability_of_red_balls(5, 10, 5) - 0.246094) < 1e-6);
    assert(std::abs(probability_of_red_balls(0, 2, 13) - 0.000016) < 1e-6);
    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    check_probability_of_red_balls();
    return 0;
}