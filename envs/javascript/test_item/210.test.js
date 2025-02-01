/**
 * Implement the Fibonacci sequence
 *
 * @param {number} n - Which Fibonacci number to calculate.
 * @return {number}
 */
function fibonacciRecursive(n) {
  // Base cases: 0th Fibonacci number is 0, 1st Fibonacci number is 1
  if (n === 0) return 0;
  if (n === 1) return 1;

  // Recursive case: nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}
describe("Fibonacci sequence", () => {
    // Test Case 1: Fibonacci of 0
    test("Fibonacci(0) should be 0", () => {
        expect(fibonacciRecursive(0)).toBe(0);
    });

    // Test Case 2: Fibonacci of 1
    test("Fibonacci(1) should be 1", () => {
        expect(fibonacciRecursive(1)).toBe(1);
    });

    // Test Case 3: Fibonacci of 5
    test("Fibonacci(5) should be 5", () => {
        expect(fibonacciRecursive(5)).toBe(5);
    });

    // Test Case 4: Fibonacci of 10
    test("Fibonacci(10) should be 55", () => {
        expect(fibonacciRecursive(10)).toBe(55);
    });

    // Test Case 5: Fibonacci of 20
    test("Fibonacci(20) should be 6765", () => {
        expect(fibonacciRecursive(20)).toBe(6765);
    });
});
