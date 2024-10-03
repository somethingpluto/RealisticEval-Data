#include <stdexcept> // For std::invalid_argument

double function_to_integrate(double x) {
    return x * x;
}

/**
 * @brief Computes the approximate integral of a function using Simpson's Rule.
 *
 * Simpson's Rule is a method for numerical integration that approximates the integral of a function
 * over an interval by fitting parabolas. This function divides the interval [a, b] into n subintervals
 * and calculates the weighted sum of the function values at specific points.
 *
 * @param a The lower limit of integration.
 * @param b The upper limit of integration.
 * @param n The number of subintervals (must be even).
 * @return The approximate value of the integral.
 *
 * @throws std::invalid_argument If n is not positive or if it is not even.
 */
double simpsons_rule(double a, double b, int n) {
    // Check if n is a positive even integer
    if (n <= 0 || n % 2 != 0) {
        throw std::invalid_argument("n must be a positive even integer.");
    }

    // Calculate the width of each subinterval
    double h = (b - a) / n;
    double sum = 0.0;

    // Calculate the weighted sum of the function values
    for (int idx = 0; idx <= n; ++idx) {
        double x = a + idx * h; // Calculate the x value at the current index
        double fx = function_to_integrate(x); // Evaluate the function at x

        // Apply the Simpson's Rule weighting
        if (idx == 0 || idx == n) {
            // First and last terms (f(a) and f(b))
            sum += fx;
        } else if (idx % 2 == 1) {
            // Odd index terms (4 * f(a + b))
            sum += 4.0 * fx;
        } else {
            // Even index terms (2 * f(a + b))
            sum += 2.0 * fx;
        }
    }

    // Final calculation to obtain the integral value
    return (h / 3.0) * sum; // Simpson's Rule formula
}