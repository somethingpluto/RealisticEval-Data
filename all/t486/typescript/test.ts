describe('Calculator', () => {
   let calculator: Calculator;

   beforeEach(() => {
       calculator = new Calculator();
   });

   it('should add two numbers correctly', () => {
       const result = calculator.add(10, 5);
       expect(result).toBe(15);
   });

   it('should subtract two numbers correctly', () => {
       const result = calculator.subtract(10, 5);
       expect(result).toBe(5);
   });

   it('should multiply two numbers correctly', () => {
       const result = calculator.multiply(10, 5);
       expect(result).toBe(50);
   });

   it('should divide two numbers correctly', () => {
       const result = calculator.divide(10, 5);
       expect(result).toBe(2.0);
   });

   it('should throw an error when dividing by zero', () => {
       expect(() => calculator.divide(10, 0)).toThrow('Cannot divide by zero.');
   });
});