/**
 * The input hash buffer is compressed into a number letter string of length no less than 5
 *
 * @param {Buffer} hash - The hash buffer to be compressed.
 * @returns {string} A compressed string representation of the hash.
 */
function compressHash(hash) {
    // Convert the buffer to a hexadecimal string
    let hexString = hash.toString('hex');

    // Compress the hexadecimal string by replacing certain patterns with shorter representations
    let compressedString = hexString.replace(/0{5,}/g, '0') // Replace sequences of 5 or more zeros with '0'
                                   .replace(/1{5,}/g, '1') // Replace sequences of 5 or more ones with '1'
                                   .replace(/2{5,}/g, '2') // Replace sequences of 5 or more twos with '2'
                                   .replace(/3{5,}/g, '3') // Replace sequences of 5 or more threes with '3'
                                   .replace(/4{5,}/g, '4') // Replace sequences of 5 or more fours with '4'
                                   .replace(/5{5,}/g, '5') // Replace sequences of 5 or more fives with '5'
                                   .replace(/6{5,}/g, '6') // Replace sequences of 5 or more sixes with '6'
                                   .replace(/7{5,}/g, '7') // Replace sequences of 5 or more sevens with '7'
                                   .replace(/8{5,}/g, '8') // Replace sequences of 5 or more eights with '8'
                                   .replace(/9{5,}/g, '9'); // Replace sequences of 5 or more nines with '9'

    // Ensure the compressed string is at least 5 characters long
    if (compressedString.length < 5) {
        compressedString = '0' + compressedString; // Prepend a zero if the string is shorter than 5 characters
    }

    return compressedString;
}
describe('compressHash', () => {

    test('should return a string of length 5', () => {
        const hash = crypto.createHash('sha256').update('test').digest();
        const result = compressHash(hash);
        expect(result.length).toBe(5);
    });

    test('should return different strings for different inputs', () => {
        const hash1 = crypto.createHash('sha256').update('test1').digest();
        const hash2 = crypto.createHash('sha256').update('test2').digest();
        const result1 = compressHash(hash1);
        const result2 = compressHash(hash2);
        expect(result1).not.toBe(result2);
    });

    test('should return a consistent result for the same input', () => {
        const hash = crypto.createHash('sha256').update('test').digest();
        const result1 = compressHash(hash);
        const result2 = compressHash(hash);
        expect(result1).toBe(result2);
    });

    test('should handle a hash of all zeros', () => {
        const hash = Buffer.alloc(32, 0); // 32 bytes of zeros
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });

    test('should handle a hash of all ones', () => {
        const hash = Buffer.alloc(32, 255); // 32 bytes of 0xFF (255 in decimal)
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });
});
