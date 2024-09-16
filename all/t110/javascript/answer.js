/**
 * Generate a random UUID of length 36
 *
 * @returns {string} A 36-character UUID string.
 */
function generateUUID() {
    // Define the characters that can appear in the UUID
    const possibleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    // Initialize an empty string to build the UUID
    let uuid = "";

    // Generate 36 characters for the UUID
    for (let i = 0; i < 36; i++) {
        uuid += possibleChars.charAt(Math.floor(Math.random() * possibleChars.length));
    }

    // Return the generated UUID
    return uuid;
}