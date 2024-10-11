describe('formatPostCount', () => {
    test('should return "01 Post" for count of 1', () => {
        expect(formatPostCount(1)).toBe('01 Post');
    });

    test('should return "02 Posts" for count of 2', () => {
        expect(formatPostCount(2)).toBe('02 Posts');
    });

    test('should return "10 Posts" for count of 10', () => {
        expect(formatPostCount(10)).toBe('10 Posts');
    });

    test('should return "99 Posts" for count of 99', () => {
        expect(formatPostCount(99)).toBe('99 Posts');
    });

    test('should return "05 Posts" for count of 5', () => {
        expect(formatPostCount(5)).toBe('05 Posts');
    });
});