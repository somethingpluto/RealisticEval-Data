describe('removePunctuation', () => {
    test('removes punctuation from a simple sentence', () => {
        const input = "Hello, world!";
        const expected = "hello world";
        expect(RemovePunctuation(input)).toBe(expected);
    });

    test('handles a string with no punctuation', () => {
        const input = "Hello world";
        const expected = "hello world";
        expect(RemovePunctuation(input)).toBe(expected);
    });

    test('converts mixed case letters to lowercase', () => {
        const input = "HeLLo WoRLd!";
        const expected = "hello world";
        expect(RemovePunctuation(input)).toBe(expected);
    });

    test('removes a variety of punctuation', () => {
        const input = "Life, in a nutshell: eat, sleep, code!";
        const expected = "life in a nutshell eat sleep code";
        expect(RemovePunctuation(input)).toBe(expected);
    });

    test('trims whitespace from the ends of the string', () => {
        const input = "   What a wonderful world!   ";
        const expected = "what a wonderful world";
        expect(RemovePunctuation(input)).toBe(expected);
    });
});
// Remove punctuation in a sentence. This function was written by ChatGPT on the 9th of April 2023. Thanks Chatty!
function RemovePunctuation(str) {
	const regexPonctuation = /[\u2000-\u206F\u2E00-\u2E7F\\'!"#$%&()*+,\-./:;<=>?@\[\]^_`{|}~]/g;
	str = str.replace(regexPonctuation, '') + "";
	return str.toLowerCase().trim();
}