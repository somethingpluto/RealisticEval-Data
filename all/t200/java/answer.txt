/**
 * @brief Extracts the string contained in the first pair of braces `{}` from the input string.
 *
 * @param input The input string from which the braces content will be extracted.
 * @return A substring enclosed within the first pair of braces, or an error message if braces are missing.
 */
public class Answer {
    
    public static String extractStringFromBraces(String input) {
        // Find the position of the first opening brace
        int openingBracePos = input.indexOf('{');

        // Check if an opening brace was found
        if (openingBracePos == -1) {
            return "No opening brace found.";
        }

        // Find the position of the first closing brace after the opening brace
        int closingBracePos = input.indexOf('}', openingBracePos);

        // Check if a closing brace was found
        if (closingBracePos == -1) {
            return "No closing brace found.";
        }

        // Extract the string between the braces (including the braces)
        return input.substring(openingBracePos, closingBracePos + 1);
    }
}