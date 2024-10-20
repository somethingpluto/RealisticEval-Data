package org.real.temp;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Answer {

    /**
     * Move the emoji expressions in the string to the end of the text.
     *
     * @param text The input string containing text and possibly emojis.
     * @return The modified string with all emojis moved to the end.
     */
    public static String moveEmojisToEnd(String text) {
        // Regular expression pattern for capturing emojis
        Pattern emojiPattern = Pattern.compile(
            "[\\ud83c[\\udf00-\\udfff]|\\ud83d[\\udc00-\\ude4f\\ude80-\\udeff]|" +
            "[\\u2694-\\u2697\\u2699-\\u26cf\\u26d1-\\u26dd\\u26e9-\\u26ea\\u26ed\\u26ef-\\u26f3\\u26f8-\\u26fa\\u26fd-\\u26fe\\u2702-\\u2704\\u2706-\\u2708\\u270a-\\u270d\\u270f-\\u2712\\u2714\\u2716\\u2728\\u2733\\u2734\\u2744\\u27a1\\u2934-\\u2935\\u2b05-\\u2b07\\u2b1b-\\u2b1c\\u3030\\ud83c[\\udde6-\\uddff]{2}\\ud83c[\\uddfb-\\uddff]\\ud83d[\\ude00-\\ude4f]]+" 
        );

        // Find all emojis in the text
        Matcher matcher = emojiPattern.matcher(text);
        StringBuffer buffer = new StringBuffer();
        StringBuffer emojis = new StringBuffer();

        // Remove emojis from the text and collect them
        while (matcher.find()) {
            matcher.appendReplacement(buffer, "");
            emojis.append(matcher.group());
        }
        matcher.appendTail(buffer);

        // Concatenate non-emoji text with extracted emojis
        return buffer.toString() + emojis.toString();
    }

    public static void main(String[] args) {
        String text = "Hello, 😊 world! 🌍";
        System.out.println(moveEmojisToEnd(text));
    }
}