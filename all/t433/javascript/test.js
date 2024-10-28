describe('TestExtractParagraphsAndLines', () => {
    it('should handle a single paragraph correctly', () => {
        const inputText = "This is a single paragraph.";
        const expectedOutput = {
            paragraphs: ["This is a single paragraph."],
            lines: ["This is a single paragraph."]
        };
        expect(extractParagraphsAndLines(inputText)).toEqual(expectedOutput);
    });

    it('should handle multiple paragraphs correctly', () => {
        const inputText = "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line.";
        const expectedOutput = {
            paragraphs: [
                "First paragraph.\nThis is the second line.",
                "Second paragraph.\nAnother line."
            ],
            lines: [
                "First paragraph.",
                "This is the second line.",
                "Second paragraph.",
                "Another line."
            ]
        };
        expect(extractParagraphsAndLines(inputText)).toEqual(expectedOutput);
    });

    it('should handle leading and trailing whitespace correctly', () => {
        const inputText = "   This paragraph has leading whitespace.\nAnd a line after.\n\n   This one has trailing whitespace.   ";
        const expectedOutput = {
            paragraphs: [
                "This paragraph has leading whitespace.\nAnd a line after.",
                "This one has trailing whitespace."
            ],
            lines: [
                "This paragraph has leading whitespace.",
                "And a line after.",
                "This one has trailing whitespace."
            ]
        };
        expect(extractParagraphsAndLines(inputText)).toEqual(expectedOutput);
    });

    it('should handle an empty string correctly', () => {
        const inputText = "";
        const expectedOutput = {
            paragraphs: [],
            lines: []
        };
        expect(extractParagraphsAndLines(inputText)).toEqual(expectedOutput);
    });

    it('should handle multiple empty paragraphs correctly', () => {
        const inputText = "\n\n\n";
        const expectedOutput = {
            paragraphs: [],
            lines: []
        };
        expect(extractParagraphsAndLines(inputText)).toEqual(expectedOutput);
    });
});