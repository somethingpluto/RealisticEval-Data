describe('extractJson', () => {
    test("returns an empty string for input without '{'", () => {
        const input = "No braces here";
        expect(extractJson(input)).toBe("");
    });

    test("extracts a single JSON object", () => {
        const input = "Here is some text before { \"key\": \"value\" } and some text after.";
        expect(extractJson(input)).toBe("{ \"key\": \"value\" }");
    });

    test("handles nested JSON objects", () => {
        const input = "Some text { \"outer\": { \"inner\": \"value\" } } more text.";
        expect(extractJson(input)).toBe("{ \"outer\": { \"inner\": \"value\" } }");
    });

    test("returns an empty string for unmatched braces", () => {
        const input = "Here is an incomplete JSON { \"key\": \"value\" ";
        expect(extractJson(input)).toBe("");
    });

    test("returns the correct JSON when multiple braces are present", () => {
        const input = "Start { { \"key\": \"value\" } and some other text { \"another\": \"object\" }} end.";
        expect(extractJson(input)).toBe("{ { \"key\": \"value\" } and some other text { \"another\": \"object\" }}");
    });

    test("extracts the first JSON object when multiple are present", () => {
        const input = "Text before { \"first\": \"value1\" } text in between { \"second\": \"value2\" }";
        expect(extractJson(input)).toBe("{ \"first\": \"value1\" }");
    });
});