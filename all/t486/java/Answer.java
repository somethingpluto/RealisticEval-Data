package org.real.temp;

public class Answer {

    public static void main(String[] args) {
        // Example usage
        Calculator calculator = new Calculator();
        System.out.println(calculator.add(10.5, 2.5)); // Output: 13.0
        System.out.println(calculator.subtract(10.5, 2.5)); // Output: 8.0
        System.out.println(calculator.multiply(10.5, 2.5)); // Output: 26.25
        try {
            System.out.println(calculator.divide(10.5, 0)); // Throws IllegalArgumentException
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage()); // Output: Cannot divide by zero.
        }
    }

    public static class Calculator {
        /**
         * Returns the sum of a and b.
         */
        public double add(double a, double b) {
            return a + b;
        }

        /**
         * Returns the difference of a and b.
         */
        public double subtract(double a, double b) {
            return a - b;
        }

        /**
         * Returns the product of a and b.
         */
        public double multiply(double a, double b) {
            return a * b;
        }

        /**
         * Returns the quotient of a and b.
         * Throws IllegalArgumentException if b is zero.
         */
        public double divide(double a, double b) {
            if (b == 0) {
                throw new IllegalArgumentException("Cannot divide by zero.");
            }
            return a / b;
        }
    }
}