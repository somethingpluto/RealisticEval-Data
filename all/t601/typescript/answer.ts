function countWords(str: string): number {
    // Initialize a word count variable
    let wordCount = 0; // Use let for block scoping
    const words = str.trim().split(/\s+/); // Split the string by whitespace

    // Count the words
    for (const word of words) {
        if (word) { // Check if the word is not empty
            wordCount++; // Increment the count for each word found
        }
    }

    return wordCount; // Return the total word count
}