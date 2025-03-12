// Start of the TypeScript function
function applyOp(a: number, b: number, op: string): number {
    // ... (rest of the TypeScript function remains unchanged)
}

// End of the TypeScript function

// Python equivalent function
def apply_op(a: float, b: float, op: str) -> float:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    elif op == '^':
        return a ** b
    else:
        raise ValueError("Unsupported operation")
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
        expect(() => applyOp(5, 0, '/')).toThrow(Error);
    });

    test("Exponentiation", () => {
        expect(applyOp(2, 3, '^')).toBe(8);
        expect(applyOp(9, 0.5, '^')).toBe(3); // Square root of 9
    });
});
