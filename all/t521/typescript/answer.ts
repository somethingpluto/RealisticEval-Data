function wordFilterCounter(text: string, filterWords: string[]): { [key: string]: number } {
    // Convert filterWords to a Set for faster lookup, ensuring case insensitivity
    const filterWordsSet = new Set(filterWords.map(word => word.toLowerCase()));

    // Find all words in the text using a regex pattern
    const words = text.toLowerCase().match(/\b\w+(?:'\w+)?\b/g);

    // Count occurrences of filtered words
    const wordCounts: { [key: string]: number } = {};
    if (words) {
        words.forEach(word => {
            if (filterWordsSet.has(word)) {
                wordCounts[word] = (wordCounts[word] || 0) + 1;
            }
        });
    }

    // Create an ordered output based on the original order of filterWords
    const orderedOutput: { [key: string]: number } = {};
    filterWords.forEach(word => {
        orderedOutput[word] = wordCounts[word.toLowerCase()] || 0;
    });

    return orderedOutput;
}
