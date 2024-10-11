/**
 * Implement decryption based on polynomials and keys
 * @param degree - The highest degree of a polynomial is added by one
 * @param modulus - Modulus to use when encrypting question
 * @param key - An array of encrypted keys
 * @param encryptedData - An array of encrypted question
 * @returns - decrypted question
 */
function performPolynomialDecryption(degree: number, modulus: number, key: number[], encryptedData: number[]): number[] {

    // Decrypts the polynomial based encryption by reversing the encryption steps
    const decryptedData: number[] = [];

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