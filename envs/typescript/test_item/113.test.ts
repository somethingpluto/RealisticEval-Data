// ... (previous code for context)

function getCSSFromSheet(sheet: CSSStyleSheet): string {
  if (!sheet || sheet.cssRules === null) {
    return '';
  }

  const cssRules = Array.from(sheet.cssRules);
  const mediaTypes = new Set<string>();
  const mediaQueries: { [mediaType: string]: string[] } = {};

  cssRules.forEach(rule => {
    if (rule instanceof CSSMediaRule) {
      mediaTypes.add(rule.media);
      if (!mediaQueries[rule.media]) {
        mediaQueries[rule.media] = [];
      }
      mediaQueries[rule.media].push(rule.cssText);
    } else if (rule instanceof CSSStyleRule) {
      mediaQueries['all'].push(rule.cssText);
    }
  });

  let combinedCSS = '';
  mediaTypes.forEach(mediaType => {
    combinedCSS += `@media ${mediaType} {\n${mediaQueries[mediaType].join('\n')}\n}\n`;
  });
  combinedCSS += mediaQueries['all'].join('\n');

  return combinedCSS;
}

// ... (rest of the code)
describe('getCSSFromSheet', () => {
    let styleSheet: CSSStyleSheet | null;

    beforeEach(() => {
        // Create a style element with some CSS rules for testing
        const style = document.createElement('style');
        style.appendChild(document.createTextNode(`
            body { background-color: red; }
            p { color: blue; }
        `));
        document.head.appendChild(style);
        styleSheet = style.sheet as CSSStyleSheet;
    });

    afterEach(() => {
        // Clean up the document after each test
        document.head.innerHTML = '';
    });

    test('Empty Stylesheet: should return an empty string', () => {
        const emptyStyle = document.createElement('style');
        document.head.appendChild(emptyStyle);
        const emptyStyleSheet = emptyStyle.sheet as CSSStyleSheet;

        const cssText = getCSSFromSheet(emptyStyleSheet);
        expect(cssText).toBe('');
    });

    test('Invalid Input: should return an empty string for non-CSSStyleSheet input', () => {
        expect(getCSSFromSheet(null)).toBe('');
        expect(getCSSFromSheet({} as CSSStyleSheet)).toBe('');
        expect(getCSSFromSheet('not a stylesheet' as unknown as CSSStyleSheet)).toBe('');
    });

    test('Cross-Origin Restrictions: should handle restricted stylesheets gracefully', () => {
        // Simulate a cross-origin stylesheet
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'http://example.com/style.css';
        document.head.appendChild(link);

        // Accessing cssRules of a cross-origin stylesheet should throw an error
        const restrictedSheet = link.sheet as CSSStyleSheet;

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

        const cssText = getCSSFromSheet(styleElement.sheet as CSSStyleSheet);
        expect(cssText).toBe('div {font-size: 16px;}');
    });
});
