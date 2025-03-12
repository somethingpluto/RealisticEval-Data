/**
 * Generate a random UUID of length 36
 * The UUID contains at least one uppercase letter, one lowercase letter, and one digit.
 *
 * @returns {string} A 36-character UUID string.
 */
function generateUUID() {
    const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    const uuidLength = 36;
    let uuid = '';

    // Ensure at least one uppercase letter, one lowercase letter, and one digit
    const ensureUppercase = () => characters[Math.floor(Math.random() * 26) + 26];
    const ensureLowercase = () => characters[Math.floor(Math.random() * 26)];
    const ensureDigit = () => characters[Math.floor(Math.random() * 10) + 52];

    uuid += ensureUppercase();
    uuid += ensureLowercase();
    uuid += ensureDigit();

    // Fill the rest of the UUID with random characters
    for (let i = 3; i < uuidLength; i++) {
        uuid += characters[Math.floor(Math.random() * characters.length)];
    }

    // Shuffle the UUID to ensure randomness
    uuid = uuid.split('').sort(() => 0.5 - Math.random()).join('');

    // Insert hyphens at the correct positions
    uuid = uuid.substring(0, 8) + '-' + uuid.substring(8, 12) + '-' + uuid.substring(12, 16) + '-' + uuid.substring(16, 20) + '-' + uuid.substring(20, 32);

    return uuid;
}
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

