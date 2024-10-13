function performPolynomialDecryption(degree: number, modulus: number, key: number[], encryptedData: number[]): number[] {
    /**
     * Implement decryption based on polynomials and keys.
     * 
     * @param degree - The highest degree of a polynomial plus one.
     * @param modulus - Modulus to use when encrypting the data.
     * @param key - An array of encrypted keys.
     * @param encryptedData - An array of encrypted data.
     * 
     * @returns The decrypted data.
     */
    const decryptedData: number[] = [];

    for (let index = 0; index < degree; index++) {
        // Calculate the decrypted value considering the positive modulus range
        let decryptedValue = (encryptedData[index] - key[index]) % modulus;

        // Adjust for TypeScript's behavior with negative numbers
        if (decryptedValue < 0) {
            decryptedValue += modulus;
        }

        decryptedData.push(decryptedValue);
    }

    return decryptedData;
}