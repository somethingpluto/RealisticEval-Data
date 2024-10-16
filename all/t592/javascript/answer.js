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
                throw new Error("Division by zero is not allowed.");
            }
            return a / b;
        case '^':
            return Math.pow(a, b);
        default:
            throw new Error("Invalid operator.");
    }
}