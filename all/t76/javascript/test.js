describe('TestRemoveCommonIndentation', () => {
    it('should return an empty string for an empty input', () => {
        // Testing edge case with an empty string
        expect(removeCommonIndentation("")).toEqual("");
    });

    it('should return the same string as input for a single line with no indentation', () => {
        // Testing a single line with no indentation
        expect(removeCommonIndentation("No indentation here")).toEqual("No indentation here");
    });

    it('should remove common leading indentation for multiple lines with uniform indentation', () => {
        // Testing basic logic with uniform indentation across multiple lines
        const inputText = "    Line one\n    Line two\n    Line three";
        const expectedOutput = "Line one\nLine two\nLine three";
        expect(removeCommonIndentation(inputText)).toEqual(expectedOutput);
    });

    it('should remove the minimum common indentation for lines with mixed indentation', () => {
        // Testing lines with mixed indentation levels
        const inputText = "  Line one\n  Line two\n  Line three";
        const expectedOutput = "Line one\nLine two\nLine three";
        expect(removeCommonIndentation(inputText)).toEqual(expectedOutput);
    });
});
