/**
 * Formats a number as currency according to the specified locale and currency code.
 *
 * @param {number} value - The numerical value to be formatted.
 * @param {string} currencyCode - The currency code (e.g., "USD", "EUR").
 * @param {string} [locale="en-US"] - The locale string (e.g., "en-US", "fr-FR").
 * @returns {string} The formatted currency string.
 */
function formatCurrency(value, currencyCode, locale = "en-US") {
    return new Intl.NumberFormat(locale, {
        style: 'currency',
        currency: currencyCode
    }).format(value);
}
describe('formatCurrency function tests', () => {
    test('should format currency in US dollars', () => {
        const value = 1234.56;
        const currencyCode = 'USD';
        const locale = 'en-US';
        const expectedOutput = '$1,234.56'; // Expected format for USD
        expect(formatCurrency(value, currencyCode, locale)).toBe(expectedOutput);
    });

    test('should format currency in Euro', () => {
        const value = 1234.56;
        const currencyCode = 'EUR';
        const locale = 'en-US';
        const expectedOutput = '€1,234.56'; // Expected format for EUR
        expect(formatCurrency(value, currencyCode, locale)).toBe(expectedOutput);
    });

    test('should format currency in British Pound', () => {
        const value = 1234.56;
        const currencyCode = 'GBP';
        const locale = 'en-GB';
        const expectedOutput = '£1,234.56'; // Expected format for GBP
        expect(formatCurrency(value, currencyCode, locale)).toBe(expectedOutput);
    });

    test('should format currency with a negative value', () => {
        const value = -1234.56;
        const currencyCode = 'USD';
        const locale = 'en-US';
        const expectedOutput = '-$1,234.56'; // Expected format for negative USD
        expect(formatCurrency(value, currencyCode, locale)).toBe(expectedOutput);
    });

    test('should handle zero value correctly', () => {
        const value = 0;
        const currencyCode = 'JPY';
        const locale = 'en-JP';
        const expectedOutput = '¥0'; // Expected format for JPY (no decimals)
        expect(formatCurrency(value, currencyCode, locale)).toBe(expectedOutput);
    });
});
