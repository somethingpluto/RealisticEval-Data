/**
 * @brief Calculate the integral approximation of a given function on a given interval [a,b] using the trapezoidal rule of numerical integration
 *
 * This function calculates the integral approximation of a given mathematical function over
 * the interval [a, b] using the trapezoidal rule of numerical integration. The interval is divided
 * into a specified number of subintervals, and the area under the curve is approximated by trapezoids.
 *
 * @param func The function to integrate, represented as a (x: number) => number.
 * @param a The lower bound of the integration interval.
 * @param b The upper bound of the integration interval.
 * @param n The number of subintervals to use in the approximation (more intervals yield higher accuracy).
 * @return The approximate value of the integral over the interval [a, b].
 */
function trapezoidalRule(func: (x: number) => number, a: number, b: number, n: number): number {
    if (n <= 0) {
        throw new Error("Number of subintervals must be greater than 0.");
    }

    const h = (b - a) / n; // Step size
    let integral = 0.5 * (func(a) + func(b)); // Initial trapezoid (half end heights)

    for (let i = 1; i < n; ++i) {
        integral += func(a + i * h);
    }

    integral *= h;
    return integral;
}