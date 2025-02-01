class Calculator {
    /**
     * Returns the sum of a and b.
     * @param {number} a - The first number.
     * @param {number} b - The second number.
     * @returns {number} The sum of a and b.
     */
    add(a, b) {
        return a + b;
    }

    /**
     * Returns the difference of a and b.
     * @param {number} a - The first number.
     * @param {number} b - The second number.
     * @returns {number} The difference of a and b.
     */
    subtract(a, b) {
        return a - b;
    }

    /**
     * Returns the product of a and b.
     * @param {number} a - The first number.
     * @param {number} b - The second number.
     * @returns {number} The product of a and b.
     */
    multiply(a, b) {
        return a * b;
    }

    /**
     * Returns the quotient of a and b.
     * Throws an error if b is zero.
     * @param {number} a - The numerator.
     * @param {number} b - The denominator.
     * @returns {number} The quotient of a and b.
     * @throws {Error} If b is zero.
     */
    divide(a, b) {
        if (b === 0) {
            throw new Error('Cannot divide by zero');
        }
        return a / b;
    }
}
describe('Calculator', () => {
    let calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    describe('add', () => {
        it('should add two numbers correctly', () => {
            const result = calculator.add(10, 5);
            expect(result).toBe(15);
        });
    });

    describe('subtract', () => {
        it('should subtract two numbers correctly', () => {
            const result = calculator.subtract(10, 5);
            expect(result).toBe(5);
        });
    });

    describe('multiply', () => {
        it('should multiply two numbers correctly', () => {
            const result = calculator.multiply(10, 5);
            expect(result).toBe(50);
        });
    });

    describe('divide', () => {
        it('should divide two numbers correctly', () => {
            const result = calculator.divide(10, 5);
            expect(result).toBe(2.0);
        });

        it('should throw an error when dividing by zero', () => {
            expect(() => calculator.divide(10, 0)).toThrow('Cannot divide by zero.');
        });
    });
});
