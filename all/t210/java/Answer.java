package org.real.temp;

public class Answer {
    
    // Recursive method to compute the nth Fibonacci number
    public static int fibonacciRecursive(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }

    // Main method for testing
    public static void main(String[] args) {
        int n = 5; // Example input
        System.out.println("Fibonacci number at position " + n + " is: " + fibonacciRecursive(n));
    }
}