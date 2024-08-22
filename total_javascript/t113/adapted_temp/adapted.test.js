// Before your test definitions
global.CSSStyleSheet = class {
    constructor() {
        this.cssRules = [];
    }
};


describe('getCSSFromSheet', () => {
    let mockSheet;

    beforeEach(() => {
        // Create a mock CSSStyleSheet object with cssRules
        mockSheet = {
            cssRules: [
                {cssText: 'body { background-color: red; }'},
                {cssText: 'p { color: blue; }'}
            ]
        };
    });

    test('correctly concatenates cssText from all rules', () => {
        const expected = 'body { background-color: red; }p { color: blue; }';
        expect(getCSSFromSheet(mockSheet)).toBe(expected);
    });

    test('returns empty string for sheets with no cssRules', () => {
        const emptySheet = {cssRules: []};
        expect(getCSSFromSheet(emptySheet)).toBe('');
    });

    test('handles sheets where cssRules is undefined', () => {
        const undefinedRulesSheet = {};
        expect(getCSSFromSheet(undefinedRulesSheet)).toBe('');
    });

    test('throws TypeError if input is not a CSSStyleSheet', () => {
        const invalidInput = 'Not a StyleSheet';
        expect(() => getCSSFromSheet(invalidInput)).toThrow(TypeError);
    });

    test('handles exceptions from accessing cssRules (e.g., CORS issues)', () => {
        // Simulate a CORS issue where accessing cssRules throws an error
        const inaccessibleSheet = {
            get cssRules() {
                throw new Error('Security error: Access is denied.');
            }
        };
        expect(getCSSFromSheet(inaccessibleSheet)).toBe('');
    });
});

/**
 * Extracts and concatenates all CSS rules from a provided stylesheet.
 * @param {CSSStyleSheet} sheet - The stylesheet object from which CSS rules are extracted.
 * @returns {string} A string containing all CSS rules concatenated together.
 */
function getCSSFromSheet(sheet) {
    // Check if the sheet is a valid CSSStyleSheet object
    if (!(sheet instanceof CSSStyleSheet)) {
        throw new TypeError("The provided input is not a valid CSSStyleSheet object.");
    }

    try {
        // Safely attempt to access and map cssRules to their cssText
        const cssRulesList = sheet.cssRules || [];
        return Array.from(cssRulesList)
            .map(rule => rule.cssText)
            .join("");
    } catch (error) {
        // Log the error and return an indication of failure
        console.error("Failed to read CSS rules from the stylesheet:", error);
        return ""; // Return empty string or handle the error as needed
    }
}