package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    public List<String> parseExpression(String expression) {
        List<String> tokens = new ArrayList<>();

        // Regular expression to match numbers (including decimals) and operators
        String regex = "\\d+\\.?\\d*|[+\\-*/()]";

        // Use regex to find matches in the expression
        java.util.regex.Pattern pattern = java.util.regex.Pattern.compile(regex);
        java.util.regex.Matcher matcher = pattern.matcher(expression);

        while (matcher.find()) {
            // Add each found token to the list
            tokens.add(matcher.group());
        }

        return tokens;
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        String expression = "3 + 5 * (2 - 8)";

        List<String> result = answer.parseExpression(expression);

        // Print the result
        System.out.println(result);
    }
}
