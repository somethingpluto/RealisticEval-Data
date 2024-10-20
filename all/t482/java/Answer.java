package org.real.temp;

public class Answer {

    /**
     * Extracts the contents of the outermost brackets from the input string.
     *
     * @param s The input string containing brackets.
     * @return The contents within the outermost brackets, or an empty string if no brackets are found.
     */
    public static String extractOutermostBrackets(String s) {
        Stack<Character> stack = new Stack<>();
        int startIndex = -1;
        String openingBrackets = "({[";
        String closingBrackets = ")}]";
        Map<Character, Character> matchingBracket = new HashMap<>();
        matchingBracket.put(')', '(');
        matchingBracket.put('}', '{');
        matchingBracket.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (openingBrackets.indexOf(ch) != -1) {  // Check for any opening bracket
                if (stack.isEmpty()) {  // If the stack is empty, we have found the outermost opening bracket
                    startIndex = i;  // Remember the position of the first opening bracket
                }
                stack.push(ch);
            } else if (closingBrackets.indexOf(ch) != -1) {  // Check for any closing bracket
                if (!stack.isEmpty() && stack.peek() == matchingBracket.get(ch)) {  // Match with the latest opening bracket
                    stack.pop();
                    if (stack.isEmpty()) {  // When stack is empty, we found the outermost closing bracket
                        return s.substring(startIndex + 1, i);  // Extract contents between the brackets
                    }
                }
            }
        }

        return "";  // Return an empty string if no outermost brackets were found
    }

}