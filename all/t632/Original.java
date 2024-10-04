//Code generated using ChatGPT
private ArrayList<Token> tokenizeExpression(String expression) {
    ArrayList<Token> tokens = new ArrayList<Token>();

   // Split the expression into individual tokens
   String[] expressionTokens = expression.split("(?<=[+\\-*/()])|(?=[+\\-*/()])");

    for (String tokenValue : expressionTokens) {
        Token token = new Token();

        // Check if the token is an operator
        if (isOperator(tokenValue)) {
            token.setOperator(true);
            token.setPrecedence(getOperatorPrecedence(tokenValue));
        } else {
            token.setOperator(false);
            token.setPrecedence((byte) 0); // Assuming non-operators have precedence 0
        }

        // Set the value of the token
        tokenValue = tokenValue.trim();

        if (!tokenValue.equals("")){
            token.setValue(tokenValue);

            // Add the token to the list
            tokens.add(token);
        }

    }

    return tokens;
}