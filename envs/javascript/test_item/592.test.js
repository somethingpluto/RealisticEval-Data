/**
 * Performs a mathematical operation on two operands.
 *
 * This function takes two numbers and an operator character, and performs
 * the specified arithmetic operation. Supported operations include addition,
 * subtraction, multiplication, division, and exponentiation.
 *
 * @param {number} a The first operand.
 * @param {number} b The second operand.
 * @param {string} op A character representing the operation to perform:
 *                    '+' for addition,
 *                    '-' for subtraction,
 *                    '*' for multiplication,
 *                    '/' for division,
 *                    '^' for exponentiation.
 *
 * @return {number} The result of the operation.
 *
 * @throws {Error} if the operator is not recognized or if
 *         there is an attempt to divide by zero.
 */
function applyOp(a, b, op) {
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            if (b === 0) {
                throw new Error('Division by zero is not allowed.');
            }
            return a / b;
        case '^':
            return Math.pow(a, b);
        default:
            throw new Error('Unsupported operator.');
    }
}
describe("applyOp function tests", () => {
    test("Addition", () => {
        expect(applyOp(3, 4, '+')).toBe(7);
        expect(applyOp(-1, -1, '+')).toBe(-2);
    });

    test("Subtraction", () => {
        expect(applyOp(10, 5, '-')).toBe(5);
        expect(applyOp(5, 10, '-')).toBe(-5);
    });

    test("Multiplication", () => {
        expect(applyOp(3, 4, '*')).toBe(12);
        expect(applyOp(-2, 5, '*')).toBe(-10);
    });

    test("Division", () => {
        expect(applyOp(8, 4, '/')).toBe(2);
        expect(applyOp(5, 2, '/')).toBe(2.5);
        expect(() => applyOp(5, 0, '/')).toThrow("Division by zero is not allowed.");
    });

    test("Exponentiation", () => {
        expect(applyOp(2, 3, '^')).toBe(8);
        expect(applyOp(9, 0.5, '^')).toBe(3); // Square root of 9
    });
});
