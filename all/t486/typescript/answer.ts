class Calculator {
    /**
     * Returns the sum of a and b.
     * @param a The first number.
     * @param b The second number.
     * @returns The sum of a and b.
     */
    add(a: number, b: number): number {
        return a + b;
    }

    /**
     * Returns the difference of a and b.
     * @param a The first number.
     * @param b The second number.
     * @returns The difference of a and b.
     */
    subtract(a: number, b: number): number {
        return a - b;
    }

    /**
     * Returns the product of a and b.
     * @param a The first number.
     * @param b The second number.
     * @returns The product of a and b.
     */
    multiply(a: number, b: number): number {
        return a * b;
    }

    /**
     * Returns the quotient of a and b.
     * Throws an error if b is zero.
     * @param a The first number.
     * @param b The second number.
     * @returns The quotient of a and b.
     */
    divide(a: number, b: number): number {
        if (b === 0) {
            throw new Error("Cannot divide by zero.");
        }
        return a / b;
    }
}