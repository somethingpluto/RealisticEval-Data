describe('TestConvertToShortFormat', () => {
    it('test basic case', () => {
        // Test a standard input with mixed characters.
        expect(convertToShortFormat("f1_p1_g1_b1_c1")).toBe("fpgbc");
    });

    it('test multiple segments', () => {
        // Test input with multiple segments.
        expect(convertToShortFormat("a2_b3_c4")).toBe("abc");
    });

    it('test non-alphanumeric', () => {
        // Test input with non-alphanumeric characters.
        expect(convertToShortFormat("hello_world_test")).toBe("hwt");
    });

    it('test single segment', () => {
        // Test a single segment input.
        expect(convertToShortFormat("single")).toBe("s");
    });
});