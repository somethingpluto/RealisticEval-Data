/**
 * Generates a random string of length 25 containing both upper case (A-Z) and lower case (a-z) letters.
 *
 * @returns {string} A randomly generated string that includes both upper and lower case letters.
 */
function generateRandomString(): string {
    // Define the character pool with upper and lower case letters
    const characters: string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    
    let randomString: string = '';

    // Generate a random string of length 25
    for (let i = 0; i < 25; i++) {
        const randomIndex: number = Math.floor(Math.random() * characters.length);
        randomString += characters[randomIndex];
    }

    return randomString;
}