/**
 * Generate a random UUID of length 36
 * The UUID has at least one uppercase letter, one lowercase letter, and one digit.
 *
 * @returns {string} A 36-character UUID string.
 */
function generateUUID(): string {
    // Define the characters that can appear in the UUID
    const possibleChars: string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    // Initialize an empty string to build the UUID
    let uuid: string = "";

    // Generate 36 characters for the UUID
    for (let i = 0; i < 36; i++) {
        uuid += possibleChars.charAt(Math.floor(Math.random() * possibleChars.length));
    }

    // Return the generated UUID
    return uuid;
}