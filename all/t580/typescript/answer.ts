import crypto from 'crypto';

/**
 * Hashes the input string using SHA-256 and ensures the result is always 64 characters long.
 * @param input - The string to be hashed.
 * @returns A 64-character hexadecimal string representing the SHA-256 hash of the input.
 */
function sha256Hash(input: string): string {
    // Create a SHA-256 hash object
    const hash = crypto.createHash('sha256');

    // Update the hash with the input string
    hash.update(input);

    // Generate the hash as a hexadecimal string
    const digest = hash.digest('hex');

    // Ensure the length is 64 characters, padding with zeros if necessary
    if (digest.length < 64) {
        const padding = '0'.repeat(64 - digest.length);
        return padding + digest;
    }

    // If the length is already 64, return the digest as is
    return digest;
}