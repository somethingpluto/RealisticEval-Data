const replacePhoneNumbers = require('./yourModule'); // Replace with the correct module path

describe('replacePhoneNumbers', () => {
    test('replaces basic phone number', () => {
        const msg = "Call me at 123-456-7890.";
        const expected = "Call me at [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    test('replaces international phone number', () => {
        const msg = "Contact us at 44 123 456 789.";
        const expected = "Contact us at [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    test('replaces phone number with parentheses', () => {
        const msg = "Our office number is 123 456-7890.";
        const expected = "Our office number is [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    test('replaces phone number with dots', () => {
        const msg = "Fax us at 123.456.7890.";
        const expected = "Fax us at [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    test('no phone number', () => {
        const msg = "Hello, please reply to this email.";
        const expected = "Hello, please reply to this email.";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });
});