/**
 * @jest-environment jsdom
 */

describe('getCSSFromSheet', () => {
    let styleSheet;

    beforeEach(() => {
        // Create a style element with some CSS rules for testing
        const style = document.createElement('style');
        style.appendChild(document.createTextNode(`
            body { background-color: red; }
            p { color: blue; }
        `));
        document.head.appendChild(style);
        styleSheet = style.sheet;
    });

    afterEach(() => {
        // Clean up the document after each test
        document.head.innerHTML = '';
    });

    test('Valid Stylesheet: should return combined CSS rules', () => {
        const cssText = getCSSFromSheet(styleSheet);
        expect(cssText).toContain('body {background-color: red;}p {color: blue;}');
    });

    test('Empty Stylesheet: should return an empty string', () => {
        const emptyStyle = document.createElement('style');
        document.head.appendChild(emptyStyle);
        const emptyStyleSheet = emptyStyle.sheet;

        const cssText = getCSSFromSheet(emptyStyleSheet);
        expect(cssText).toBe('');
    });

    test('Invalid Input: should return an empty string for non-CSSStyleSheet input', () => {
        expect(getCSSFromSheet(null)).toBe('');
        expect(getCSSFromSheet({})).toBe('');
        expect(getCSSFromSheet('not a stylesheet')).toBe('');
    });

    test('Cross-Origin Restrictions: should handle restricted stylesheets gracefully', () => {
        // Simulate a cross-origin stylesheet
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'http://example.com/style.css';
        document.head.appendChild(link);

        // Accessing cssRules of a cross-origin stylesheet should throw an error
        const restrictedSheet = link.sheet;

        expect(() => {
            getCSSFromSheet(restrictedSheet);
        }).not.toThrow();  // The function should not throw an error

        // Simulate behavior by returning an empty string
        const cssText = getCSSFromSheet(restrictedSheet);
        expect(cssText).toBe('');
    });

    test('Style Element with Inline CSS: should return CSS from inline style element', () => {
        const styleElement = document.createElement('style');
        styleElement.textContent = 'div { font-size: 16px; }';
        document.head.appendChild(styleElement);

        const cssText = getCSSFromSheet(styleElement.sheet);
        expect(cssText).toBe('div {font-size: 16px;}');
    });
});