/**
 * Shuffles the characters in a given string randomly.
 *
 * @param {string} inputString - The string to shuffle.
 * @returns {string} A new string with the characters shuffled.
 */
function shuffleString(inputString: string): string {
    // Convert the string into an array of characters
    const charArray: string[] = inputString.split('');
    const length: number = charArray.length;

    // Shuffle the array using the Fisher-Yates algorithm
    for (let i = length - 1; i > 0; i--) {
        // Generate a random index between 0 and i (inclusive)
        const randomIndex: number = Math.floor(Math.random() * (i + 1));

        // Swap the current character with the character at the random index
        [charArray[i], charArray[randomIndex]] = [charArray[randomIndex], charArray[i]];
    }

    // Join the shuffled array back into a string and return it
    return charArray.join('');
}