#include <iostream>

// Recursive function to compute the nth Fibonacci number
int fibonacciRecursive(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}