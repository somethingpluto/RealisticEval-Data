/**
 * Perform decryption based on polynomials and keys
 * @param {number} degree - The highest degree of a polynomial is added by one
 * @param {number} modulus - Modulus to use when encrypting/decrypting
 * @param {number[]} key - An array of encrypted keys
 * @param {number[]} encryptedData - An array of encrypted data
 * @returns {number[]} Decrypted data
 */
function performPolynomialDecryption(degree, modulus, key, encryptedData) {
    // Decrypts the polynomial based encryption by reversing the encryption steps
    const decryptedData = [];

    for (let index = 0; index < degree; index++) {
        // Calculate the decrypted value considering positive modulus range
        let decryptedValue = (encryptedData[index] - key[index]) % modulus;
        // Adjust for JavaScript's behavior with negative numbers
        if (decryptedValue < 0) {
            decryptedValue += modulus;
        }
        decryptedData.push(decryptedValue);
    }

    return decryptedData;
}