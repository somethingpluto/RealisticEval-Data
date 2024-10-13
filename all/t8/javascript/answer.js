function performPolynomialDecryption(degree, modulus, key, encryptedData) {
    /**
     * Implement decryption based on polynomials and keys
     * @param {number} degree - The highest degree of a polynomial plus one
     * @param {number} modulus - Modulus used during encryption
     * @param {Array<number>} key - An array of encrypted keys
     * @param {Array<number>} encryptedData - An array of encrypted data
     * @returns {Array<number>} Decrypted data
     */

    // Decrypts the polynomial-based encryption by reversing the encryption steps
    const decryptedData = [];

    for (let index = 0; index < degree; index++) {
        // Calculate the decrypted value considering the positive modulus range
        let decryptedValue = (encryptedData[index] - key[index]) % modulus;

        // Adjust for JavaScript's behavior with negative numbers
        if (decryptedValue < 0) {
            decryptedValue += modulus;
        }

        decryptedData.push(decryptedValue);
    }

    return decryptedData;
}