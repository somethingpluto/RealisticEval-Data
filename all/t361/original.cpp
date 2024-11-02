#include <iostream>
#include <cmath>
#include "sine.h"
#include "ex4.h"

double simpsons_rule(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.0;
    for (int i = 0; i <= n; i++) {
        double x = a + i * h;
        double fx = sine_function(x);
        if (i == 0 || i == n) {
            sum += fx;
        } else if (i % 2 == 1) {
            sum += 4.0 * fx;
        } else {
            sum += 2.0 * fx;
        }
    }
    return h * sum / 3.0;
}