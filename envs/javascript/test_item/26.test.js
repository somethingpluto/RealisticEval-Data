/**
 * Converts input strings that contain multiple separators (for example, *, ;, /) to comma-separated formatted strings.
 *
 * @param {string} inputString - The input string containing various separators like *, ;, /, -, :
 * @returns {string} A comma-separated string where all specified separators have been replaced with commas.
 */
function convertToCommaSeparated(inputString) {
    // Define the separators to be replaced
    const separators = /[*,;/:-]/g;
    
    // Replace all occurrences of the separators with commas
    const commaSeparatedString = inputString.replace(separators, ',');
    
    return commaSeparatedString;
}
describe('TestConvertToCommaSeparated', () => {
    it('should convert basic separators correctly', () => {
        expect(convertToCommaSeparated("apple;banana*orange/mango")).toBe("apple,banana,orange,mango");
    });

    it('should convert mixed separators in a string correctly', () => {
        expect(convertToCommaSeparated("grapes;lemon/melon*kiwi;litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should convert mixed separators in a string correctly (second test)', () => {
        expect(convertToCommaSeparated("grapes/lemon/melon*kiwi*litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should handle strings with no separators correctly', () => {
        expect(convertToCommaSeparated("watermelon")).toBe("watermelon");
    });
});
