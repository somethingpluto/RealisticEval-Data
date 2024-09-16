/**
 * The input hash buffer is compressed into a number letter string of length no less than 5
 *
 * @param {Buffer} hash - The hash buffer to be compressed.
 * @returns {string} A compressed string representation of the hash.
 */
function compressHash(hash: Buffer): string {
    // Convert the hash buffer to a number in base 16 (hexadecimal)
    let num = parseInt(hash.toString("hex"), 16);

    // Define the base and alphabet for encoding
    const base = 62;
    const alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Initialize the model_result string
    let result = "";

    // Convert the number to the desired base (base 62) and construct the compressed string
    while (result.length < 5) {
        const remainder = num % base;
        result += alphabet.charAt(remainder);
        num = Math.floor(num / base);
    }

    return result;
}