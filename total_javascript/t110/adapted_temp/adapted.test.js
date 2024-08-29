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
/**
 * Generate a random UUID of length 36
 *
 * @returns {string} A 36-character UUID string.
 */
function generateUUID() {
    // Define the characters that can appear in the UUID
    const possibleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    // Initialize an empty string to build the UUID
    let uuid = "";

    // Generate 36 characters for the UUID
    for (let i = 0; i < 36; i++) {
        uuid += possibleChars.charAt(Math.floor(Math.random() * possibleChars.length));
    }

    // Return the generated UUID
    return uuid;
}