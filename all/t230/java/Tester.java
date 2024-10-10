public class EmojiUtils {
    public static String moveEmojisToEnd(String text) {
        // Regex pattern to match emojis
        Pattern emojiPattern = Pattern.compile("[\uD83C-\uDBFF\uDC00-\uDFFF]");
        Matcher matcher = emojiPattern.matcher(text);

        StringBuilder nonEmojiPart = new StringBuilder();
        StringBuilder emojiPart = new StringBuilder();

        while (matcher.find()) {
            emojiPart.append(matcher.group());
        }

        matcher.reset();
        while (matcher.find()) {
            matcher.appendReplacement(nonEmojiPart, "");
        }
        matcher.appendTail(nonEmojiPart);

        return nonEmojiPart.toString() + emojiPart.toString();
    }
}