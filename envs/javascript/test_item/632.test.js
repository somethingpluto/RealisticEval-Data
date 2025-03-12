/**
 * Parses a mathematical expression string into an array of tokens.
 * This function identifies both operands (numbers) and operators (+, -, *, /, etc.)
 * in the provided expression and returns them in an array format.
 *
 * @param {string} expression - The mathematical expression to be parsed.
 * @returns {string[]} An array containing the tokens identified in the expression.
 *                     The array will include both operands and operators in the order they appear.
 */
function parseExpression(expression) {
    const tokens = [];
    let currentToken = '';

    for (let i = 0; i < expression.length; i++) {
        const char = expression[i];

        if (isDigit(char) || char === '.') {
            // If the character is a digit or a decimal point, continue building the number
            currentToken += char;
        } else {
            // If we have a current token (number), push it to the tokens array
            if (currentToken !== '') {
                tokens.push(currentToken);
                currentToken = '';
            }

            // Handle operators and parentheses
            if (isOperator(char) || isParenthesis(char)) {
                tokens.push(char);
            }
        }
    }

    // Push the last token if it's a number
    if (currentToken !== '') {
        tokens.push(currentToken);
    }

    return tokens;
}

function isDigit(char) {
    return char >= '0' && char <= '9';
}

function isOperator(char) {
    return ['+', '-', '*', '/', '^', '%'].includes(char);
}

function isParenthesis(char) {
    return ['(', ')'].includes(char);
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
