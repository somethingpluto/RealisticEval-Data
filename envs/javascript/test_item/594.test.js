/**
 * Splits a comma-separated string into individual tokens.
 *
 * This function takes a string containing comma-separated values, trims
 * leading and trailing whitespace from each token, and stores the non-empty
 * tokens in the provided array.
 *
 * @param {string} str - The input string to be split, which may contain leading and
 *            trailing whitespace around the tokens.
 * @param {Array<string>} vect - An array where the resulting tokens will be stored. 
 *             The array will be cleared before storing the new tokens.
 */
function splitComma(str, vect) {
    vect.length = 0; // Clear the array
    const tokens = str.split(','); // Split the string by commas
    for (const token of tokens) {
        const trimmedToken = token.trim(); // Trim whitespace from each token
        if (trimmedToken !== '') { // Store non-empty tokens
            vect.push(trimmedToken);
        }
    }
}
describe("splitComma function tests", () => {
    let result;

    beforeEach(() => {
        result = [];
    });

    test("Basic comma-separated values", () => {
        splitComma("apple,banana,orange", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });

    test("Leading and trailing whitespace", () => {
        splitComma("  apple , banana , orange  ", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });

    test("Multiple consecutive commas", () => {
        splitComma("apple,,banana,,,orange", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });

    test("Empty input string", () => {
        splitComma("", result);
        expect(result.length).toBe(0);
    });

    test("Only whitespace input", () => {
        splitComma("   ", result);
        expect(result.length).toBe(0);
    });

    test("Trailing commas", () => {
        splitComma("apple,banana,orange,", result);
        expect(result.length).toBe(3);
        expect(result[0]).toBe("apple");
        expect(result[1]).toBe("banana");
        expect(result[2]).toBe("orange");
    });
});
