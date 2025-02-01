/**
 * Hides the sensitive part of a bank account number with 17 numbers, only showing the last 4 characters.
 * For example:
 *      input: 12345678901234567
 *      output: ****4567
 * @param {string} account - The bank account number to hide.
 * @returns {string} - The bank account number with the first part hidden.
 * @throws {Error} - Throws an error if the account number is not exactly 17 characters long.
 */
function hideBankAccount(account) {
    if (account.length !== 17) {
        throw new Error('Account number must be exactly 17 characters long.');
    }
    return '****' + account.slice(-4);
}
describe('hideBankAccount', () => {
    test('should return "****4567" for an account number of "12345678901234567"', () => {
        expect(hideBankAccount('12345678901234567')).toBe('****4567');
    });

    test('should return "****6543" for an account number of "98765432109876543"', () => {
        expect(hideBankAccount('98765432109876543')).toBe('****6543');
    });

    test('should return "****1100" for an account number of "11111111111111100"', () => {
        expect(hideBankAccount('11111111111111100')).toBe('****1100');
    });

    test('should throw an error for an account number shorter than 17 characters', () => {
        expect(() => hideBankAccount('1234567890123456')).toThrow();
    });

    test('should throw an error for an account number longer than 17 characters', () => {
        expect(() => hideBankAccount('123456789012345678')).toThrow();
    });

    test('should throw an error for an account number with 0 characters', () => {
        expect(() => hideBankAccount('')).toThrow();
    });
});
