class Calculator {
    add(a, b) {
        /**
         * Returns the sum of a and b.
         */
        return a + b;
    }

    subtract(a, b) {
        /**
         * Returns the difference of a and b.
         */
        return a - b;
    }

    multiply(a, b) {
        /**
         * Returns the product of a and b.
         */
        return a * b;
    }

    divide(a, b) {
        /**
         * Returns the quotient of a and b.
         * Throws Error if b is zero.
         */
        if (b === 0) {
            throw new Error("Cannot divide by zero.");
        }
        return a / b;
    }
}