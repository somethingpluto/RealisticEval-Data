describe('checkCSSHighlightAndAdd', () => {
    beforeEach(() => {
        // Clean up the document head and ensure at least one style sheet exists before each test
        document.head.innerHTML = '<style></style>';
    });

    test('should add a new style element with the highlight CSS rule if it does not exist', () => {
        checkCSSHighlightAndAdd();

        // Check that the style element contains the correct CSS rule
        const styleElement = document.querySelector('style');
        expect(styleElement.sheet.cssRules[0].cssText).toContain("background-color: yellow;");
    });

    test('should not add a new CSS rule if the CSS rule already exists', () => {
        // Manually add the rule to simulate existing condition
        document.styleSheets[0].insertRule(".highlight { background-color: yellow; }", 0);

        checkCSSHighlightAndAdd();

        // Check that only one rule is present
        expect(document.styleSheets[0].cssRules.length).toBe(2);
    });

    test('should add only one rule even if called multiple times', () => {
        checkCSSHighlightAndAdd();
        checkCSSHighlightAndAdd();  // Call the function again

        // Check that only one rule is present
        expect(document.styleSheets[0].cssRules.length).toBe(2);
    });

    test('should correctly append the style element to the document head', () => {
        checkCSSHighlightAndAdd();

        // Check that the style element is indeed appended to the head
        const styleElement = document.head.querySelector('style');
        expect(document.head.contains(styleElement)).toBe(true);
    });
});