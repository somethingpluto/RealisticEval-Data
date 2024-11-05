function moveEmojisToEnd(text: string): string {
    const emojiRegex: RegExp = /[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu;
    let emojis = text.match(emojiRegex);
    if (!emojis || emojis.length === 0) {
        return text;
    }
    let newText = text.replace(emojiRegex, '');
    return newText + emojis.join('');
}
