package org.real.temp;

public class Answer {

    /**
     * Move the emoji expressions in the string to the end of the text.
     *
     * @param text The input string containing text and possibly emojis.
     * @return The modified string with all emojis moved to the end.
     */
    public static String moveEmojisToEnd(String text) {
        // Regex pattern to match emojis
        String regex = "[\uD83C\uDF00-\uDBFF\uDC00-\uDFFF]+";
        
        // Find all emojis in the text
        java.util.regex.Pattern pattern = java.util.regex.Pattern.compile(regex);
        java.util.regex.Matcher matcher = pattern.matcher(text);
        
        // Collect non-emoji characters
        StringBuilder nonEmojiText = new StringBuilder();
        while (matcher.find()) {
            nonEmojiText.append(matcher.replaceAll(""));
        }
        
        // Append all emojis to the end
        StringBuilder emojiText = new StringBuilder();
        while (matcher.find()) {
            emojiText.append(matcher.group());
        }
        
        return nonEmojiText.toString() + emojiText.toString();
    }

    public static void main(String[] args) {
        // Test the method
        String input = "Hello, World! 😊";
        String result = moveEmojisToEnd(input);
        System.out.println(result);  // Output: Hello, World! 😊
    }
}