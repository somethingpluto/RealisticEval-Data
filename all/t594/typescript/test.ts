describe('splitComma function tests', () => {
    let result: string[];

    beforeEach(() => {
        result = [];
    });

    test('Basic comma-separated values', () => {
        splitComma("apple,banana,orange", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });

    test('Leading and trailing whitespace', () => {
        splitComma("  apple , banana , orange  ", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });

    test('Multiple consecutive commas', () => {
        splitComma("apple,,banana,,,orange", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });

    test('Empty input string', () => {
        splitComma("", result);
        expect(result.length).toBe(0);
    });

    test('Only whitespace input', () => {
        splitComma("   ", result);
        expect(result.length).toBe(0);
    });

    test('Trailing commas', () => {
        splitComma("apple,banana,orange,", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });
});