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