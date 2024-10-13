#include <iostream>
#include <cmath>

// Function to calculate the binomial coefficient (n choose k)
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

// Function to calculate the probability that x balls randomly drawn from a jar
// containing n red balls and m blue balls will all be red balls.
double probability_red_balls(int x, int n, int m) {
    if (x > n) {
        return 0; // Not enough red balls to draw x red balls
    }
    int total_balls = n + m;
    if (x > total_balls) {
        return 0; // Not enough balls to draw x balls of any color
    }

    // Number of ways to choose x red balls from n red balls
    long long ways_to_choose_red = binomial_coefficient(n, x);
    // Total number of ways to choose x balls from all balls
    long long total_ways_to_choose_balls = binomial_coefficient(total_balls, x);

    // Probability that all chosen balls are red
    double probability = static_cast<double>(ways_to_choose_red) / total_ways_to_choose_balls;

    return probability;
}

int main() {
    // Example usage
    std::cout << "Probability (x=2, n=5, m=7): " << probability_red_balls(2, 5, 7) << std::endl;
    std::cout << "Probability (x=3, n=4, m=6): " << probability_red_balls(3, 4, 6) << std::endl;

    return 0;
}