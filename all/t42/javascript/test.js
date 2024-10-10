describe('replacePhoneNumbers', () => {
    it('should replace all phone numbers in the string with "[PHONE_NUM]"', () => {
        expect(replacePhoneNumbers('Call me at 123-456-7890.')).toBe('Call me at [PHONE_NUM].');
        expect(replacePhoneNumbers('Reach out at +1 (123) 456-7890 for more info.')).toBe('Reach out at [PHONE_NUM] for more info.');
        expect(replacePhoneNumbers('No phone number here!')).toBe('No phone number here!');
        expect(replacePhoneNumbers('Multiple numbers: 123-456-7890 and +1 (123) 456-7890.')).toBe('Multiple numbers: [PHONE_NUM] and [PHONE_NUM].');
    });
});