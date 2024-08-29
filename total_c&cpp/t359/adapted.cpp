#include <functional>

using namespace std;

/**
 * @brief Calculate the integral approximation of a given function on a given interval [a,b] using the trapezoidal rule of numerical integration
 *
 * This function calculates the integral approximation of a given mathematical function over
 * the interval [a, b] using the trapezoidal rule of numerical integration. The interval is divided
 * into a specified number of subintervals, and the area under the curve is approximated by trapezoids.
 *
 * @param func The function to integrate, represented as a std::function<double(double)>.
 * @param a The lower bound of the integration interval.
 * @param b The upper bound of the integration interval.
 * @param n The number of subintervals to use in the approximation (more intervals yield higher accuracy).
 * @return The approximate value of the integral over the interval [a, b].
 */
double trapezoidal_rule(const std::function<double(double)>& func, double a, double b, int n) {
    if (n <= 0) {
        throw std::invalid_argument("Number of subintervals must be greater than 0.");
    }

    double h = (b - a) / n; // Step size
    double integral = 0.5 * (func(a) + func(b)); // Initial trapezoid (half end heights)

    for (int i = 1; i < n; ++i) {
        integral += func(a + i * h);
    }

    integral *= h;
    return integral;
}