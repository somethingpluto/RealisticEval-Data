/**
 * Converts a string concatenated with underscores to a short format.
 * For example:
 *     input: f1_p1_g1_b1_c1
 *     output: fpgbc
 *
 * @param {string} inputStr - The input string with segments separated by underscores.
 * @return {string} A short format string derived from the first characters of each segment.
 */
function convertToShortFormat(inputStr) {
    const segments = inputStr.split('_');
    return segments.map(segment => segment[0]).join('');
}
describe('TestConvertToShortFormat', () => {
    it('test basic case', () => {
        /** Test a standard input with mixed characters. */
        expect(convertToShortFormat("f1_p1_g1_b1_c1")).toBe("fpgbc");
    });

    it('test multiple segments', () => {
        /** Test input with multiple segments. */
        expect(convertToShortFormat("a2_b3_c4")).toBe("abc");
    });

    it('test non-alphanumeric characters', () => {
        /** Test input with non-alphanumeric characters. */
        expect(convertToShortFormat("hello_world_test")).toBe("hwt");
    });

    it('test single segment', () => {
        /** Test a single segment input. */
        expect(convertToShortFormat("single")).toBe("s");
    });
});
