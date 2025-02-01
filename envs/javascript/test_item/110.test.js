/**
 * Generate a random UUID of length 36
 * The UUID At least one uppercase letter,At least one lowercase letter,At least one digit
 *
 * @returns {string} A 36-character UUID string.
 */
function generateUUID() {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let hasUpperCase = false;
    let hasLowerCase = false;
    let hasDigit = false;

    for (let i = 0; i < 36; i++) {
        const randomIndex = Math.floor(Math.random() * charactersLength);
        const randomCharacter = characters.charAt(randomIndex);
        result += randomCharacter;

        if (i === 8 || i === 13 || i === 18 || i === 23) {
            result += '-';
        }

        if (randomCharacter >= 'A' && randomCharacter <= 'Z') {
            hasUpperCase = true;
        } else if (randomCharacter >= 'a' && randomCharacter <= 'z') {
            hasLowerCase = true;
        } else if (randomCharacter >= '0' && randomCharacter <= '9') {
            hasDigit = true;
        }
    }

    if (!hasUpperCase || !hasLowerCase || !hasDigit) {
        return generateUUID(); // Recursively generate a new UUID if the conditions are not met
    }

    return result;
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

