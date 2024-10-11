describe('MyTestSuite', () => {
    let value: number;

    beforeAll(() => {
        value = 10;
    });

    afterAll(() => {
        delete value;
    });

    it('should add 5 to value and get 15', () => {
        const result = value + 5;
        expect(result).toBe(15);
    });

    it('should subtract 3 from value and get 7', () => {
        const result = value - 3;
        expect(result).toBe(7);
    });
});