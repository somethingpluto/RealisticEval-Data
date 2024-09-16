/**
 * Convert the chat logs to Markdown format and generate a Blob object containing them
 *
 * @param {string[]} chat - The chat conversation as an array of strings.
 * @param {string} [title="ChatGPT Conversation"] - The optional title for the conversation.
 * @returns {Blob} A Blob containing the Markdown formatted string of the conversation.
 */
function convertChatToMarkdown(chat, title = "ChatGPT Conversation") {
    let markdown = `# ${title}\n\n`;  // Initialize with the title and two newlines

    // Iterate over the chat conversation array
    chat.forEach((message, index) => {
        const speaker = index % 2 === 0 ? "Human" : "Assistant"; // Alternate speaker
        markdown += `**${speaker}:**\n${message}\n\n***\n\n`;  // Add message to the markdown
    });

    // Get the current date and time
    const date = getDate();
    const time = getTime();

    // Append the timestamp
    markdown += `Exported on ${date} ${time}.`;

    // Encode the string as a Blob and return it
    return encodeStringAsBlob(markdown);
}

/**
 * Encodes a string as a Blob object.
 *
 * @param {string} string - The string to encode.
 * @returns {Blob} The encoded Blob.
 */
function encodeStringAsBlob(string) {
    return new Blob([string], { type: 'text/markdown' });
}

/**
 * Gets the current date in YYYY-MM-DD format.
 *
 * @returns {string} The current date.
 */
function getDate() {
    const date = new Date();
    return date.toISOString().split('T')[0];
}

/**
 * Gets the current time in HH:MM:SS format.
 *
 * @returns {string} The current time.
 */
function getTime() {
    const date = new Date();
    return date.toTimeString().split(' ')[0];
}