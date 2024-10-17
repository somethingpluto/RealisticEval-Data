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