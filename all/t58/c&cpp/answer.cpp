#include <iostream>
#include <cmath>

double factorial(int num) {
    if (num == 0)
        return 1;
    else
        return num * factorial(num - 1);
}

double combination(int n, int k) {
    return factorial(n) / (factorial(k) * factorial(n-k));
}

double probability_of_red_balls(int n, int x, int y) {
    double total = x + y;

    if (n > x || n > total)
        return 0;

    double numerator = combination(x, n) * combination(y, total-n);
    double denominator = combination(total, n);

    return numerator / denominator;
}