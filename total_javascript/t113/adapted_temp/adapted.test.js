// Import the necessary libraries
const { JSDOM } = require('jsdom');

describe('getCSSFromSheet function tests', () => {
    // Set up a DOM environment before each test
    let dom, window, document, sheet;
    beforeEach(() => {
        dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
        window = dom.window;
        document = window.document;

        // Create a CSSStyleSheet-like object with cssRules property
        sheet = {
            cssRules: [
                { cssText: 'body { background: #fff; }' },
                { cssText: 'p { color: #333; }' }
            ]
        };
    });

    test('returns concatenated CSS rules from a valid stylesheet', () => {
        expect(getCSSFromSheet(sheet)).toBe('body { background: #fff; }p { color: #333; }');
    });

    test('throws TypeError when input is not a CSSStyleSheet', () => {
        const invalidSheet = {};
        expect(() => getCSSFromSheet(invalidSheet)).toThrow(TypeError);
        expect(() => getCSSFromSheet(invalidSheet)).toThrow("The provided input is not a valid CSSStyleSheet object.");
    });

    test('handles empty stylesheet gracefully', () => {
        const emptySheet = { cssRules: [] };
        expect(getCSSFromSheet(emptySheet)).toBe('');
    });

    test('returns an empty string if cssRules are not accessible', () => {
        const inaccessibleSheet = {};
        Object.defineProperty(inaccessibleSheet, 'cssRules', {
            get: () => {
                throw new Error("Access is denied");
            }
        });

        expect(getCSSFromSheet(inaccessibleSheet)).toBe('');
    });

    test('concatenates rules correctly even with complex CSS', () => {
        const complexCSSRules = [
            { cssText: '@media screen and (max-width: 600px) { body { background: #000; } }' },
            { cssText: 'div::after { content: "hello"; color: red; }' }
        ];
        const complexSheet = { cssRules: complexCSSRules };

        expect(getCSSFromSheet(complexSheet)).toBe('@media screen and (max-width: 600px) { body { background: #000; } }div::after { content: "hello"; color: red; }');
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