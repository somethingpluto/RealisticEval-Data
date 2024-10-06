describe('generateUUID', () => {

    test('should return a string', () => {
        const result = generateUUID();
        expect(typeof result).toBe('string');
    });

    test('should return a string of length 36', () => {
        const result = generateUUID();
        expect(result.length).toBe(36);
    });

    test('should return a string containing only valid characters', () => {
        const validChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        const result = generateUUID();

        for (let char of result) {
            expect(validChars).toContain(char);
        }
    });

    test('should generate different UUIDs on consecutive calls', () => {
        const uuid1 = generateUUID();
        const uuid2 = generateUUID();
        expect(uuid1).not.toBe(uuid2);
    });

    test('should generate UUIDs that include a mix of uppercase and lowercase letters and digits', () => {
        const result = generateUUID();
        expect(/[A-Z]/.test(result)).toBe(true); // At least one uppercase letter
        expect(/[a-z]/.test(result)).toBe(true); // At least one lowercase letter
        expect(/[0-9]/.test(result)).toBe(true); // At least one digit
    });

});