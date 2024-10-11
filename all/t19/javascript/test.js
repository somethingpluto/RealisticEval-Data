describe("PhoneNumberDetection", () => {
    test("should detect international prefix", () => {
        expect(containsPhoneNumber("+1-800-555-1234")).toBe(true);
    });

    test("should detect standard format with dashes", () => {
        expect(containsPhoneNumber("800-555-1234")).toBe(true);
    });

    test("should detect standard format with spaces", () => {
        expect(containsPhoneNumber("800 555 1234")).toBe(true);
    });

    test("should not detect any phone number", () => {
        expect(containsPhoneNumber("Hello, world!")).toBe(false);
    });

    test("should detect phone number in text", () => {
        expect(containsPhoneNumber("Call me at 800-555-1234 today!")).toBe(true);
    });
});