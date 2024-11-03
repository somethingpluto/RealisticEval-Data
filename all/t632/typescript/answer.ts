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