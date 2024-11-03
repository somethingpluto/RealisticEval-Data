/**
 * Generates a 16-byte random salt value, hashes the provided password with that salt
 * using the SHA-256 hash algorithm, and returns the combined salt and hashed password.
 *
 * @param {string} password - The password to be hashed.
 * @return {Promise<Uint8Array>} A byte array containing the salt followed by the hashed password.
 */
async function hashPasswordWithSalt(password) {
    // Generate a 16-byte random salt
    const salt = generateRandomSalt(16);
    
    // Hash the password with the salt using SHA-256
    const hashedPassword = await hashWithSHA256(password, salt);
    
    // Combine the salt and the hashed password
    const saltAndHashedPassword = new Uint8Array([...salt, ...hashedPassword]);
    return saltAndHashedPassword;
}

/**
 * Generates a random salt of specified length.
 *
 * @param {number} length - The length of the salt.
 * @return {Uint8Array} A byte array containing the random salt.
 */
function generateRandomSalt(length) {
    const salt = new Uint8Array(length);
    window.crypto.getRandomValues(salt);
    return salt;
}

/**
 * Hashes the password using SHA-256 with the provided salt.
 *
 * @param {string} password - The password to be hashed.
 * @param {Uint8Array} salt - The salt to be used in hashing.
 * @return {Promise<Uint8Array>} A byte array containing the hashed password.
 */
async function hashWithSHA256(password, salt) {
    const encoder = new TextEncoder();
    const data = encoder.encode(password);
    const saltedData = new Uint8Array([...data, ...salt]);
    const hashBuffer = await crypto.subtle.digest('SHA-256', saltedData);
    return new Uint8Array(hashBuffer);
}
