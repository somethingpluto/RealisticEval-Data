import { v4 as uuidv4 } from 'uuid';

/**
 * Generates a random string of length 25 containing both upper case (A-Z) 
 * and lower case (a-z) letters.
 *
 * @returns {string} A randomly generated string that meets the criteria of 
 * including both upper and lower case letters.
 */
function generateRandomString(): string {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let result = '';
    for (let i = 0; i < 25; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

/**
 * Generates a random UUID.
 *
 * @returns {string} A randomly generated UUID.
 */
function generateRandomUUID(): string {
    return uuidv4();
}
describe('generateRandomString', () => {
    test('length', () => {
        const randomString = generateRandomString();
        expect(randomString.length).toBe(25);
    });

    test('contains upper case', () => {
        const randomString = generateRandomString();
        expect(randomString.split('').some(char => char.toUpperCase() === char && char.toLowerCase() !== char)).toBe(true);
    });

    test('contains lower case', () => {
        const randomString = generateRandomString();
        expect(randomString.split('').some(char => char.toLowerCase() === char && char.toUpperCase() !== char)).toBe(true);
    });

    test('randomness', () => {
        const string1 = generateRandomString();
        const string2 = generateRandomString();
        expect(string1).not.toBe(string2);
    });

    test('multiple generations', () => {
        const numTests = 100;
        let hasUpperCase = false;
        let hasLowerCase = false;

        for (let i = 0; i < numTests; i++) {
            const randomString = generateRandomString();
            hasUpperCase ||= randomString.split('').some(char => char.toUpperCase() === char && char.toLowerCase() !== char);
            hasLowerCase ||= randomString.split('').some(char => char.toLowerCase() === char && char.toUpperCase() !== char);
        }

        expect(hasUpperCase).toBe(true);
        expect(hasLowerCase).toBe(true);
    });
});
