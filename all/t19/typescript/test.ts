import { containsPhoneNumber } from './path/to/your/module'; // Adjust the import based on your file structure

describe('Phone Number Detection', () => {
    test('with international prefix', () => {
        expect(containsPhoneNumber("+1-800-555-1234")).toBe(true);
    });

    test('with standard dashes', () => {
        expect(containsPhoneNumber("800-555-1234")).toBe(true);
    });

    test('with spaces', () => {
        expect(containsPhoneNumber("800 555 1234")).toBe(true);
    });

    test('without phone number', () => {
        expect(containsPhoneNumber("Hello, world!")).toBe(false);
    });

    test('with text containing numbers', () => {
        expect(containsPhoneNumber("Call me at 800-555-1234 today!")).toBe(true);
    });
});