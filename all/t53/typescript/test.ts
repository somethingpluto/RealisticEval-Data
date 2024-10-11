describe('sizeInBytes', () => {
    it('should return the correct size for different objects', () => {
        const emptyObject = {};
        const array = [1, 2, 3];
        const string = "Hello, World!";
        const number = 42;

        expect(sizeInBytes(emptyObject)).toBe(0); // Adjust this based on your actual implementation
        expect(sizeInBytes(array)).toBeGreaterThan(0);
        expect(sizeInBytes(string)).toBeGreaterThan(0);
        expect(sizeInBytes(number)).toBeGreaterThan(0);
    });
});