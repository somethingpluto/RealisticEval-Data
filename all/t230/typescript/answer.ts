function moveEmojisToEnd(text: string): string {
    // Regular expression to match emojis
    const emojiRegex = /([\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}])/gu;

    // Split the text into non-emoji and emoji parts
    let nonEmojiParts: string[] = [];
    let emojiParts: string[] = [];

    for (let char of text) {
        if (emojiRegex.test(char)) {
            emojiParts.push(char);
        } else {
            nonEmojiParts.push(char);
        }
    }

    // Combine non-emoji parts followed by emoji parts
    return nonEmojiParts.join('') + emojiParts.join('');
}