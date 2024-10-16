describe("floatToHex tests", () => {
    test("Test with positive float 123.456", () => {
        const input = 123.456;
        const expected = "42f6e979";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with negative float -123.456", () => {
        const input = -123.456;
        const expected = "c2f6e979";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with zero", () => {
        const input = 0.0;
        const expected = "00000000";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with small positive float 0.0001", () => {
        const input = 0.0001;
        const expected = "38d1b717";
        expect(floatToHex(input)).toBe(expected);
    });

    test("Test with large float 1e30", () => {
        const input = 1e30;
        const expected = "7149f2ca";
        expect(floatToHex(input)).toBe(expected);
    });
});