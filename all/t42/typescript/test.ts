describe('replace_phone_numbers', () => {
    it('should replace phone numbers in various formats', () => {
        expect(replace_phone_numbers('Call me at 123-456-7890.')).toBe('Call me at [PHONE_NUM].');
        expect(replace_phone_numbers('My number is (123) 456-7890.')).toBe('My number is [PHONE_NUM].');
        expect(replace_phone_numbers('Send me an email at info@example.com.')).toBe('Send me an email at info@example.com.');
        expect(replace_phone_numbers('Contact us at +1-123-456-7890.')).toBe('Contact us at [PHONE_NUM].');
        expect(replace_phone_numbers('No phone number here.')).toBe('No phone number here.');
    });
});