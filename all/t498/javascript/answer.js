const crypto = require('crypto');

function computeMD5(inputString) {
    /**
     * Computes and returns the MD5 hash of the input string.
     *
     * @param {string} inputString - The string to be hashed
     * @return {string} The MD5 hash of the input string in hexadecimal format
     */
    // Create an MD5 hash object
    const md5Hash = crypto.createHash('md5');

    // Update the hash object with the bytes of the input string
    md5Hash.update(inputString, 'utf-8');

    // Return the hexadecimal representation of the hash
    return md5Hash.digest('hex');
}