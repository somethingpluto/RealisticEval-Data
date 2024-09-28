import { findShiftJISNotInGBK } from './path-to-your-function'; // Adjust import based on your file structure

describe('findShiftJISNotInGBK', () => {
    let shiftjisNotGBK: string[];

    beforeAll(() => {
        // Compute the result once before all tests
        shiftjisNotGBK = findShiftJISNotInGBK();
    });

    it('should not include known Shift-JIS only characters in GBK', () => {
        const knownShiftjisOnly = 'ヱ'; // Ensure this character is correct based on encoding
        expect(shiftjisNotGBK).toContain(knownShiftjisOnly);
    });

    it('should not include characters that are common in both encodings', () => {
        const commonCharacter = '水'; // Common in both, ensure accuracy
        expect(shiftjisNotGBK).not.toContain(commonCharacter);
    });

    it('should not include characters in neither encoding', () => {
        const neitherEncodingChar = '\u{1F4A9}'; // Emoji, not in basic Shift-JIS or GBK
        expect(shiftjisNotGBK).not.toContain(neitherEncodingChar);
    });

    it('should handle edge cases at the bounds of the BMP', () => {
        const edgeOfBMP = '\uFFFF'; // Last character in BMP
        expect(shiftjisNotGBK).not.toContain(edgeOfBMP);
    });

    it('should handle the list not being empty', () => {
        expect(shiftjisNotGBK.length).toBeGreaterThan(0);
    });
});