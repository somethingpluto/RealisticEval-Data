/**
 * Implement decryption based on polynomials and keys.
 * @param {number} degree - The highest degree of a polynomial plus one.
 * @param {number} modulus - Modulus used during encryption.
 * @param {Array<number>} key - An array of encrypted keys.
 * @param {Array<number>} encryptedData - An array of encrypted data.
 * @returns {Array<number>} Decrypted data.
 */
function performPolynomialDecryption(degree, modulus, key, encryptedData) {
    // Initialize the decrypted data array
    const decryptedData = [];

    // Iterate over each encrypted data point
    for (let i = 0; i < encryptedData.length; i++) {
        let decryptedValue = 0;

        // Evaluate the polynomial at the current index
        for (let j = 0; j < degree; j++) {
            decryptedValue += key[j] * Math.pow(i + 1, j);
        }

        // Apply the modulus to the decrypted value
        decryptedValue = (decryptedValue % modulus + modulus) % modulus;

        // Subtract the decrypted value from the encrypted data to get the original data
        decryptedData.push((encryptedData[i] - decryptedValue + modulus) % modulus);
    }

    return decryptedData;
}
describe('TestDecryptFunction', () => {
    it('test basic functionality', () => {
        expect(performPolynomialDecryption(4, 5, [1, 2, 3, 4], [5, 6, 7, 8])).toEqual([4, 4, 4, 4]);
    });

    it('test zero secret key', () => {
        expect(performPolynomialDecryption(3, 7, [0, 0, 0], [6, 13, 20])).toEqual([6, 6, 6]);
    });

    it('test zero ciphertext', () => {
        expect(performPolynomialDecryption(3, 9, [1, 2, 3], [0, 0, 0])).toEqual([8, 7, 6]);
    });

    it('test large values', () => {
        expect(performPolynomialDecryption(2, 1000, [500, 500], [1000, 1000])).toEqual([500, 500]);
    });
});
