describe('generateUUID', () => {

    test('should generate a UUID of length 36', () => {
        const uuid = generateUUID();
        expect(uuid.length).toBe(36);
    });

    test('should generate a UUID containing only valid characters', () => {
        const uuid = generateUUID();
        const validChars = /^[A-Za-z0-9]+$/; // Regex to check only alphanumeric characters
        expect(validChars.test(uuid)).toBe(true);
    });

    test('should generate different UUIDs on multiple calls', () => {
        const uuid1 = generateUUID();
        const uuid2 = generateUUID();
        expect(uuid1).not.toBe(uuid2);
    });

    test('should generate a UUID without any special characters', () => {
        const uuid = generateUUID();
        const hasSpecialChars = /[^A-Za-z0-9]/; // Regex to find any non-alphanumeric characters
        expect(hasSpecialChars.test(uuid)).toBe(false);
    });

    test('should generate a UUID with 36 alphanumeric characters', () => {
        const uuid = generateUUID();
        const validChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        for (let i = 0; i < uuid.length; i++) {
            expect(validChars.includes(uuid[i])).toBe(true);
        }
    });

});