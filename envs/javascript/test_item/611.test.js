/**
 * Generates a random string of length 25 containing both upper case (A-Z) and lower case (a-z) letters.
 *
 * @returns {string} A randomly generated string that meets the criteria of including both upper and lower case letters.
 */
function generateRandomString() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let result = '';
    const charactersLength = characters.length;
    for (let i = 0; i < 25; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}
describe('generateRandomString', () => {
    
    test('length', () => {
        const randomString = generateRandomString();
        expect(randomString.length).toBe(25); // Equivalent of assertEqual in unittest
    });

    test('contains upper case', () => {
        const randomString = generateRandomString();
        const hasUpperCase = [...randomString].some(char => char === char.toUpperCase() && char !== char.toLowerCase());
        expect(hasUpperCase).toBe(true); // Equivalent of assertTrue in unittest
    });

    test('contains lower case', () => {
        const randomString = generateRandomString();
        const hasLowerCase = [...randomString].some(char => char === char.toLowerCase() && char !== char.toUpperCase());
        expect(hasLowerCase).toBe(true); // Equivalent of assertTrue in unittest
    });

    test('randomness', () => {
        const string1 = generateRandomString();
        const string2 = generateRandomString();
        expect(string1).not.toBe(string2); // Equivalent of assertNotEqual in unittest
    });

    test('multiple generations', () => {
        const numTests = 100;
        let hasUpperCase = false;
        let hasLowerCase = false;

        for (let i = 0; i < numTests; i++) {
            const randomString = generateRandomString();
            hasUpperCase ||= [...randomString].some(char => char === char.toUpperCase() && char !== char.toLowerCase());
            hasLowerCase ||= [...randomString].some(char => char === char.toLowerCase() && char !== char.toUpperCase());
        }

        expect(hasUpperCase).toBe(true); // Equivalent of assertTrue in unittest
        expect(hasLowerCase).toBe(true); // Equivalent of assertTrue in unittest
    });

});
