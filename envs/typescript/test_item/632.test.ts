// Start of the code context
import { Token, TokenType } from './token';

function parseExpression(expression: string): Token[] {
    const tokens: Token[] = [];
    let current = 0;

    while (current < expression.length) {
        const char = expression[current];

        if (/\d/.test(char)) {
            let value = '';
            while (/\d/.test(char)) {
                value += char;
                current++;
                if (current >= expression.length) break;
                char = expression[current];
            }
            tokens.push(new Token(TokenType.NUMBER, parseInt(value, 10)));
        } else if (/[\+\-\*\/\(\)]/.test(char)) {
            tokens.push(new Token(TokenType.OPERATOR, char));
            current++;
        } else {
            throw new Error(`Invalid character: ${char}`);
        }
    }

    return tokens;
}
// End of the code context
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
