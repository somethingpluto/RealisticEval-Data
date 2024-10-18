describe('TestExtractOutermostBrackets', () => {
    it('should extract single parentheses', () => {
        expect(extractOutermostBrackets("Text (example) more text")).toBe("example");
    });

    it('should extract nested brackets', () => {
        expect(extractOutermostBrackets("Text {with some {nested} brackets}")).toBe("with some {nested} brackets");
    });

    it('should extract square brackets', () => {
        expect(extractOutermostBrackets("Text [with [nested] brackets] and more text")).toBe("with [nested] brackets");
    });

    it('should extract mixed bracket types', () => {
        expect(extractOutermostBrackets("Mixed (types {of brackets [in use]})")).toBe("types {of brackets [in use]}");
    });

    it('should return an empty string when no brackets are present', () => {
        expect(extractOutermostBrackets("No brackets here")).toBe("");
    });
});
