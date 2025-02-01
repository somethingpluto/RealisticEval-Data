/**
 * Encodes a byte array into a Base64 encoded string.
 *
 * This function takes an array of numbers (representing bytes) as input and converts it
 * into a Base64 encoded string.
 *
 * @param {number[]} data An array of numbers representing the input data to be encoded.
 * @return {string} A string containing the Base64 encoded representation of the input data.
 */
function base64Encode(data) {
    const base64Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    let result = '';
    let i = 0;

    while (i < data.length) {
        let octet1 = data[i++];
        let octet2 = i < data.length ? data[i++] : 0;
        let octet3 = i < data.length ? data[i++] : 0;

        let triple = (octet1 << 16) | (octet2 << 8) | octet3;

        result += base64Chars[(triple >> 18) & 0x3F];
        result += base64Chars[(triple >> 12) & 0x3F];
        result += base64Chars[(triple >> 6) & 0x3F];
        result += base64Chars[triple & 0x3F];
    }

    while ((result.length % 4) !== 0) {
        result += '=';
    }

    return result;
}
describe("Base64 Encode Tests", () => {

    test("Empty input should return empty string", () => {
        const input = [];
        expect(base64Encode(input)).toBe("");
    });

    test("Encoding 'hello' should return 'aGVsbG8='", () => {
        const input = [104, 101, 108, 108, 111]; // ASCII values for 'hello'
        expect(base64Encode(input)).toBe("aGVsbG8=");
    });

    test("Encoding 'world' should return 'd29ybGQ='", () => {
        const input = [119, 111, 114, 108, 100]; // ASCII values for 'world'
        expect(base64Encode(input)).toBe("d29ybGQ=");
    });

    test("Encoding 'foobar' should return 'Zm9vYmFy'", () => {
        const input = [102, 111, 111, 98, 97, 114]; // ASCII values for 'foobar'
        expect(base64Encode(input)).toBe("Zm9vYmFy");
    });

    test("Encoding 'Catch2' should return 'Q2F0Y2gy'", () => {
        const input = [67, 97, 116, 99, 104, 50]; // ASCII values for 'Catch2'
        expect(base64Encode(input)).toBe("Q2F0Y2gy");
    });

    test("Encoding single byte 'A' should return 'QQ=='", () => {
        const input = [65]; // ASCII value for 'A'
        expect(base64Encode(input)).toBe("QQ==");
    });

});
