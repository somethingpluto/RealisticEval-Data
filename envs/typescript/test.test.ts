function parseExpression(expression: string): string[] {
    const tokens: string[] = [];
    // Regular expression to match numbers (including decimals) and operators
    const regex = /\d+\.?\d*|[+*/()\-]/g;
    // Use regex to find matches in the expression
    const matches = expression.match(regex);
    if (matches) {
        // Add each found token to the list
        tokens.push(...matches);
    }
    return tokens;
}
describe('parseExpression', () => {
    test('simple addition', () => {
        const expression = "2 + 2";
        const result = parseExpression(expression);
        expect(result).toEqual(["2", "+", "2"]);
    });

    test('complex expression', () => {
        const expression = "3 + 5 * (2 - 8)";
        const result = parseExpression(expression);
        expect(result).toEqual(["3", "+", "5", "*", "(", "2", "-", "8", ")"]);
    });

    test('negative numbers', () => {
        const expression = "-1 + 4 - 5";
        const result = parseExpression(expression);
        expect(result).toEqual(["-", "1", "+", "4", "-", "5"]);
    });

    test('decimals', () => {
        const expression = "3.5 + 2.1";
        const result = parseExpression(expression);
        expect(result).toEqual(["3.5", "+", "2.1"]);
    });

    test('operators only', () => {
        const expression = "+ - * /";
        const result = parseExpression(expression);
        expect(result).toEqual(["+", "-", "*", "/"]);
    });

    test('empty expression', () => {
        const expression = "";
        const result = parseExpression(expression);
        expect(result.length).toBe(0);
    });

    test('single number', () => {
        const expression = "42";
        const result = parseExpression(expression);
        expect(result).toEqual(["42"]);
    });
});
