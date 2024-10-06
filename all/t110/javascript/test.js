describe('generateUUID', () => {

    test('should return a string', () => {
        const result = generateUUID();
        expect(typeof result).toBe('string');
    });

    test('should return a string of length 36', () => {
        const result = generateUUID();
        expect(result.length).toBe(36);
    });


    test('should generate different UUIDs on consecutive calls', () => {
        const uuid1 = generateUUID();
        const uuid2 = generateUUID();
        expect(uuid1).not.toBe(uuid2);
    });

    test('should generate UUIDs that include uppercase', () => {
        const result = generateUUID();
        expect(/[A-Z]/.test(result)).toBe(true); // At least one uppercase letter
    });
    test('should generate UUIDs that include  lowercase letters', () => {
        const result = generateUUID();
        expect(/[a-z]/.test(result)).toBe(true); // At least one lowercase letter
    });
    test('should generate UUIDs that include digits', () => {
        const result = generateUUID();
        expect(/[0-9]/.test(result)).toBe(true); // At least one digit
    });

});
