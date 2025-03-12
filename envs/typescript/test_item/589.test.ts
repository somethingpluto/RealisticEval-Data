import { parse } from 'json5';

/**
 * Extracts the first complete JSON object from a given string.
 * Now supports JSON5 syntax.
 *
 * @param response The input string from which to extract the JSON object.
 * @return A string containing the first complete JSON object, or an
 *         empty string if no complete object is found.
 */
function extractJson(response: string): string {
  let start = response.indexOf('{');
  if (start === -1) return '';

  let end = response.indexOf('}', start + 1);
  if (end === -1) return '';

  let json = response.substring(start, end + 1);
  try {
    parse(json);
    return json;
  } catch (error) {
    return '';
  }
}
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
