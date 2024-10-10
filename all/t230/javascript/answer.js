function moveEmojisToEnd(text) {
    // Regular expression for matching emojis
    const emojiRegex = /[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu;

    // Find all emojis in the string
    let emojis = text.match(emojiRegex);

    if (!emojis || !emojis.length) {
        return text;
    }

    // Remove emojis from the original text
    let newText = text.replace(emojiRegex, '');

    // Append emojis to the end of the new text
    return newText + emojis.join('');
}