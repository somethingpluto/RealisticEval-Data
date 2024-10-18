describe('TestSplitIntoSentences', () => {
    describe('test_basic_splitting', () => {
        it('should correctly split a basic text with clear punctuation', () => {
            const text = "Hello world! How are you? I am fine.";
            const expected = ["Hello world!", "How are you?", "I am fine."];
            const result = splitIntoSentences(text);
            expect(result).toEqual(expected);
        });
    });

    describe('test_complex_punctuation', () => {
        it('should correctly split text that includes quotes and commas', () => {
            const text = 'He said, This is amazing! Then he left.';
            const expected = ['He said, This is amazing!', "Then he left."];
            const result = splitIntoSentences(text);
            expect(result).toEqual(expected);
        });
    });

    describe('test_with_no_punctuation', () => {
        it('should correctly handle text with no punctuation marks', () => {
            const text = "Hello world how are you";
            const expected = ["Hello world how are you"];
            const result = splitIntoSentences(text);
            expect(result).toEqual(expected);
        });
    });

    describe('test_empty_string', () => {
        it('should correctly handle an empty string input', () => {
            const text = "";
            const expected = [];
            const result = splitIntoSentences(text);
            expect(result).toEqual(expected);
        });
    });
});