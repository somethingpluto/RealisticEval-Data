/**
 * @jest-environment jsdom
 *//**
 * Extract all the CSS rules from a given CSSStyleSheet and concatenate them into a string
 *
 * @param {CSSStyleSheet} sheet - The stylesheet object from which to extract CSS rules.
 * @returns {string} A single string containing all CSS rules, or an empty string if the sheet is invalid or inaccessible.
 */
function getCSSFromSheet(sheet) {
  if (!sheet || !(sheet instanceof CSSStyleSheet)) {
    return '';
  }

  let cssText = '';
  try {
    for (const rule of sheet.cssRules) {
      cssText += rule.cssText + '\n';
    }
  } catch (error) {
    console.error('Error accessing CSSStyleSheet:', error);
    return '';
  }

  return cssText;
}
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

