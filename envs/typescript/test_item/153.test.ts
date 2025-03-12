import { createHash } from 'crypto';

/**
 * The input hash buffer is compressed into a number letter string of length no less than 5.
 *
 * @param {Buffer} hash - The hash buffer to be compressed.
 * @returns {string} A compressed string representation of the hash.
 */
// @ts-ignore
function compressHash(hash: Buffer): string {
    const hashAlgo = 'sha256';
    const hashObj = createHash(hashAlgo);
    hashObj.update(hash);
    const hashHex = hashObj.digest('hex');
    const hashBase58 = Buffer.from(hashHex, 'hex').toString('base58');
    return hashBase58;
}
// @ts-ignore
const crypto = require('crypto');

describe('compressHash', () => {

    test('should return a string of length 5', () => {
        // @ts-ignore
        const hash = crypto.createHash('sha256').update('test').digest();
        // @ts-ignore
        const result = compressHash(hash);
        expect(result.length).toBe(5);
    });

    test('should return different strings for different inputs', () => {
        // @ts-ignore
        const hash1 = crypto.createHash('sha256').update('test1').digest();
        // @ts-ignore
        const hash2 = crypto.createHash('sha256').update('test2').digest();
        // @ts-ignore
        const result1 = compressHash(hash1);
        // @ts-ignore
        const result2 = compressHash(hash2);
        expect(result1).not.toBe(result2);
    });

    test('should return a consistent model_answer_result for the same input', () => {
        // @ts-ignore
        const hash = crypto.createHash('sha256').update('test').digest();
        // @ts-ignore
        const result1 = compressHash(hash);
        // @ts-ignore
        const result2 = compressHash(hash);
        expect(result1).toBe(result2);
    });

    test('should handle a hash of all zeros', () => {
        const hash = Buffer.alloc(32, 0); // 32 bytes of zeros
        // @ts-ignore
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });

    test('should handle a hash of all ones', () => {
        const hash = Buffer.alloc(32, 255); // 32 bytes of 0xFF (255 in decimal)
        // @ts-ignore
        const result = compressHash(hash);
        expect(result).toMatch(/^[0-9a-zA-Z]{5}$/);
    });
});

