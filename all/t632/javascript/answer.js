function parseExpression(expression) {
    const tokens = [];
    // Regular expression to match numbers (including decimals) and operators
    const regex = /\d+\.?\d*|[+*/()\-]/g;
    // Use regex to find matches in the expression
    let match;
    while ((match = regex.exec(expression)) !== null) {
        // Add each found token to the array
        tokens.push(match[0]);
    }
    return tokens;
}