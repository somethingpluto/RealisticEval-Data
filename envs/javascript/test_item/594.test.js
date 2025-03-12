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
    // Clear the provided array
    vect.length = 0;

    // Split the string by commas
    const tokens = str.split(',');

    // Iterate through the tokens
    for (let token of tokens) {
        // Trim whitespace from each token
        token = token.trim();

        // Add non-empty tokens to the array
        if (token) {
            vect.push(token);
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
