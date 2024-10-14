describe('TestGetMidsFromEdges', () => {
    it('test_basic_case', () => {
        // Test with a standard range of edges
        const edges = [1, 2, 3, 4];
        const expectedMids = [1.5, 2.5, 3.5];
        expect(getMidsFromEdges(edges)).toEqual(expectedMids);
    });

    it('test_single_interval', () => {
        // Test with two edges (single interval)
        const edges = [5, 10];
        const expectedMids = [7.5];
        expect(getMidsFromEdges(edges)).toEqual(expectedMids);
    });

    it('test_multiple_intervals', () => {
        // Test with multiple intervals
        const edges = [0, 1, 2, 3, 4, 5];
        const expectedMids = [0.5, 1.5, 2.5, 3.5, 4.5];
        expect(getMidsFromEdges(edges)).toEqual(expectedMids);
    });

    it('test_negative_edges', () => {
        // Test with negative edges
        const edges = [-5, -3, -1, 1];
        const expectedMids = [-4.0, -2.0, 0.0];
        expect(getMidsFromEdges(edges)).toEqual(expectedMids);
    });

    it('test_zero_edges', () => {
        // Test with edges including zero
        const edges = [0, 1, 2];
        const expectedMids = [0.5, 1.5];
        expect(getMidsFromEdges(edges)).toEqual(expectedMids);
    });

    it('test_float_edges', () => {
        // Test with floating-point edges
        const edges = [0.0, 1.5, 3.0];
        const expectedMids = [0.75, 2.25];
        expect(getMidsFromEdges(edges)).toEqual(expectedMids);
    });

    it('test_empty_array', () => {
        // Test with an empty array
        const edges = [];
        const expectedMids = [];
        expect(getMidsFromEdges(edges)).toEqual(expectedMids);
    });
});