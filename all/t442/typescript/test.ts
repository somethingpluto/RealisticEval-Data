describe('TestConvertStringsToNumbers', () => {
    it('test_flat_dict', () => {
        const data = { a: '1', b: '2.5', c: 'not a number' };
        const expected = { a: 1, b: 2.5, c: 'not a number' };
        expect(convertStringsToNumbers(data)).toEqual(expected);
    });

    it('test_nested_dict', () => {
        const data = { x: { y: '10', z: '3.14' }, w: '20.0' };
        const expected = { x: { y: 10, z: 3.14 }, w: 20.0 };
        expect(convertStringsToNumbers(data)).toEqual(expected);
    });

    it('test_list_of_strings', () => {
        const data = ['1', '2.5', '3', 'invalid'];
        const expected = [1, 2.5, 3, 'invalid'];
        expect(convertStringsToNumbers(data)).toEqual(expected);
    });

    it('test_mixed_structure', () => {
        const data = { numbers: ['1', '2.0', 3], more_numbers: [{ num: '4' }, '5'] };
        const expected = { numbers: [1, 2.0, 3], more_numbers: [{ num: 4 }, 5] };
        expect(convertStringsToNumbers(data)).toEqual(expected);
    });

    it('test_empty_structure', () => {
        const data = {};
        const expected = {};
        expect(convertStringsToNumbers(data)).toEqual(expected);
    });
});